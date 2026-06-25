import click

from pyhtb import PyHTB
from pyhtb.v4.models.get_connections_servers_product import GetConnectionsServersProduct

from .. import formatter
from ..common import fail, fail_api, get_sdk, handle_errors


def get_all_servers(sdk: PyHTB, product: GetConnectionsServersProduct):
    res = sdk.v4.get_connections_servers(product=product)
    if not res or not res.data or not res.data.options:
        return []

    servers = []
    options = res.data.options
    for loc_prop in options.additional_properties.values():
        for group_name, group_obj in loc_prop.additional_properties.items():
            if not group_obj.servers:
                continue
            for srv_obj in group_obj.servers.additional_properties.values():
                servers.append(
                    {
                        "id": srv_obj.id,
                        "name": srv_obj.friendly_name,
                        "location": srv_obj.location,
                        "clients": srv_obj.current_clients,
                        "full": srv_obj.full,
                        "group": group_name,
                    }
                )
    return servers


def find_vpn_server(sdk: PyHTB, target: str):
    pools = [
        GetConnectionsServersProduct.LABS,
        GetConnectionsServersProduct.STARTING_POINT,
        GetConnectionsServersProduct.COMPETITIVE,
    ]
    target_lower = target.lower()
    for pool in pools:
        try:
            servers = get_all_servers(sdk, pool)
            for s in servers:
                if str(s["id"]) == target or s["name"].lower() == target_lower:
                    return s
        except Exception:
            pass
    return None


@click.group(name="vpn", help="Manage Hack The Box VPN configurations")
def vpn_group():
    pass


@vpn_group.command(name="status", help="Show current VPN connection status")
@handle_errors("retrieve status")
def vpn_status():
    sdk = get_sdk()
    formatter.print_info("Retrieving connection status...")
    response = sdk.v4.get_connection_status()
    if not response:
        formatter.print_warning("No active VPN connections reported.")
        return

    rows = []
    for item in response:
        conn = getattr(item, "connection", None)
        srv = getattr(item, "server", None)

        ip = getattr(conn, "ip4", "N/A") if conn else "N/A"
        srv_name = getattr(srv, "friendly_name", "N/A") if srv else "N/A"
        loc = getattr(item, "location_type_friendly", "N/A")

        rows.append([srv_name, ip, loc, getattr(item, "connection_type", "N/A")])

    headers = ["Server Name", "IP Address", "Location Type", "Connection Type"]
    formatter.render_table("Active Connections", headers, rows)


@vpn_group.command(name="servers", help="List available VPN servers")
@click.option(
    "--pool",
    type=click.Choice(["labs", "starting_point", "competitive"], case_sensitive=False),
    default="labs",
    help="Server pool to list (default: labs)",
)
@handle_errors("list servers")
def vpn_servers(pool):
    sdk = get_sdk()
    prod_map = {
        "labs": GetConnectionsServersProduct.LABS,
        "starting_point": GetConnectionsServersProduct.STARTING_POINT,
        "competitive": GetConnectionsServersProduct.COMPETITIVE,
    }
    product = prod_map[pool.lower()]

    formatter.print_info(f"Retrieving servers for pool '{pool}'...")
    servers = get_all_servers(sdk, product)
    if not servers:
        formatter.print_warning("No servers found.")
        return

    rows = []
    for s in servers:
        status = "[error]Full[/error]" if s["full"] else "[success]Available[/success]"
        rows.append([s["id"], s["name"], s["location"], s["group"], s["clients"], status])

    headers = ["ID", "Server Name", "Location", "Group", "Clients", "Status"]
    formatter.render_table(f"VPN Servers: {pool}", headers, rows)


@vpn_group.command(name="switch", help="Switch your active VPN server")
@click.argument("target")
@handle_errors("switch server")
def vpn_switch(target):
    sdk = get_sdk()
    formatter.print_info(f"Resolving VPN server '{target}'...")
    server = find_vpn_server(sdk, target)
    if not server:
        fail(f"Could not resolve server '{target}' to a valid VPN server ID.")

    formatter.print_info(f"Switching to server '{server['name']}' (ID: {server['id']})...")
    detailed = sdk.v4.post_connections_servers_switch_detailed(vpn_id=server["id"])
    if detailed.status_code == 200:
        formatter.print_success(f"Successfully switched to server '{server['name']}'!")
    else:
        fail_api("switch server", detailed)


@vpn_group.command(name="download", help="Download .ovpn configuration file")
@click.argument("target")
@click.option("--tcp", is_flag=True, help="Download TCP config instead of UDP")
@click.option("--output", "-o", help="Output path (default: <server_name>.ovpn)")
@handle_errors("download config")
def vpn_download(target, tcp, output):
    sdk = get_sdk()
    formatter.print_info(f"Resolving VPN server '{target}'...")
    server = find_vpn_server(sdk, target)
    if not server:
        fail(f"Could not resolve server '{target}' to a valid VPN server ID.")

    if not output:
        output = f"{server['name'].replace(' ', '_').lower()}.ovpn"

    formatter.print_info(f"Downloading VPN config for '{server['name']}'...")
    if tcp:
        detailed = sdk.v4.get_access_ovpnfile_vpn_id_tcp_detailed(vpn_id=server["id"])
    else:
        detailed = sdk.v4.get_access_ovpnfile_vpn_id_udp_detailed(vpn_id=server["id"])

    if detailed.status_code != 200:
        fail_api("download config", detailed)

    ovpn_data = _extract_ovpn_payload(detailed.parsed)
    if not ovpn_data:
        fail("Empty or invalid config payload received.")

    with open(output, "w") as f:
        f.write(ovpn_data)

    formatter.print_success(f"Config downloaded and saved to [success]{output}[/success]!")


def _extract_ovpn_payload(res) -> str:
    """Extract the .ovpn text from a response payload (file-like or raw bytes/str)."""
    payload = getattr(res, "payload", None)
    if payload is None:
        return ""
    if hasattr(payload, "getvalue"):
        val = payload.getvalue()
    elif hasattr(payload, "read"):
        val = payload.read()
    else:
        val = payload
    return val.decode() if isinstance(val, bytes) else val
