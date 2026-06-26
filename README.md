# Unofficial Hack The Box (HTB) Python SDK & API Client (`pyhtb`)

[![PyPI Version](https://img.shields.io/pypi/v/pyhtb.svg?color=blue)](https://pypi.org/project/pyhtb/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/pyhtb.svg)](https://pypi.org/project/pyhtb/)
[![License](https://img.shields.io/github/license/Gubarz/pyhtb.svg)](LICENSE)
[![Code Style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

An unofficial, modern Python SDK and API client wrapper for the **Hack The Box (HTB)** platform. This library exposes synchronous and asynchronous interfaces with generated typed request and response models for interacting programmatically with HTB APIs.

Whether you are automating machine status checking, managing teams, tracking starting point progression, or scripting challenge submissions, `pyhtb` provides a single unified interface.

`pyhtb` is an independent project and is not affiliated with, endorsed by, or sponsored by Hack The Box.

---

## Key Features

* **Broad API coverage**: Clients generated from v4, v5, and Experience v1 specifications.
* **Synchronous and asynchronous APIs**: Built on HTTPX.
* **Typed data models**: Generated request and response models using attrs.
* **Unified authentication**: Configure one token across supported API clients.
* **Optional CLI**: Common machine, challenge, VPN, search, and profile workflows.

---

## Installation

Install the package via `pip` from PyPI:

```bash
pip install pyhtb
```

For local development or running modifications, clone the repository and install in editable mode:

```bash
pip install -e .
```

---

## Quick Start

### 1. Basic Client Initialization

Initialize the `PyHTB` client wrapper. If you want to access protected endpoints, provide your Hack The Box API token (generated on the app.hackthebox.com settings page).

```python
from pyhtb import PyHTB

# Initialize authenticated SDK
client = PyHTB(token="YOUR_HTB_API_TOKEN")

# The unified client organizes endpoints by API version:
# - client.v4
# - client.v5
# - client.experience_v1
```

### 2. Accessing Endpoints (v5 Example)

All OpenAPI operations are dynamically bound as callable methods directly on the version clients.

#### Synchronous Call
```python
from pyhtb import PyHTB

client = PyHTB(token="YOUR_HTB_API_TOKEN")

# Call any endpoint directly. Client authentication parameters are injected automatically!
machines_response = client.v5.get_machines()

for machine in machines_response.data:
    print(f"Machine: {machine.name} | OS: {machine.os} | Difficulty: {machine.difficulty}")
```

#### Asynchronous Call
All asynchronous methods share the same name as sync ones but are postfixed with `_async`.

```python
import asyncio
from pyhtb import PyHTB

async def main():
    client = PyHTB(token="YOUR_HTB_API_TOKEN")
    
    # Asynchronous endpoint invocation
    machines_response = await client.v5.get_machines_async()
    
    for machine in machines_response.data:
        print(f"Async loaded: {machine.name}")

asyncio.run(main())
```

#### Accessing Detailed Responses (Metadata & Headers)
If you need to inspect HTTP status codes or response headers, append `_detailed` or `_async_detailed` to the method name:

```python
response = client.v5.get_machines_detailed()
print(f"HTTP Status: {response.status_code}")
print(f"Response Headers: {response.headers}")
print(f"Parsed Body Model: {response.parsed}")
```

---

## Supported APIs and Specs

The SDK is compiled from official and community-maintained reverse-engineered OpenAPI specifications:

| Version | Description | Target Submodule |
| :--- | :--- | :--- |
| **API v4** | Primary platform endpoints (User, Teams, Challenges, Tracks, etc.) | `client.v4` |
| **API v5** | Modern dashboard & user activity endpoints (Machines status, University, User dashboard) | `client.v5` |
| **Experience v1** | Experience, Levels, and Streak endpoints | `client.experience_v1` |

---

## CLI Tool (Proof of Concept)

`pyhtb` ships with an experimental command-line interface that wraps the SDK into a quick-fire workflow tool. After installing the package, the `pyhtb` command is available globally.

### Authentication

```bash
# Store your HTB App Token (generates from app.hackthebox.com → Settings → App Tokens)
pyhtb auth set

# Verify your credentials
pyhtb auth status

# You can also export the token as an environment variable
export HTB_TOKEN="eyJ..."
```

Interactive token input is hidden. Environment variables take precedence over the stored token. If you store a token with `pyhtb auth set`, it is written as plaintext to `$XDG_CONFIG_HOME/pyhtb/token`, or `~/.config/pyhtb/token` when `XDG_CONFIG_HOME` is not set. On Unix-like systems, the token file is created with owner-only `0600` permissions.

### Machines

```bash
# List active machines
pyhtb machine list

# List retired machines, filtered by difficulty
pyhtb machine list --retired --difficulty hard --os linux

# Show detailed info for a machine (by name or ID)
pyhtb machine info Checkpoint

# Start a machine and wait for IP assignment
pyhtb machine start Checkpoint

# Check your active machine
pyhtb machine active

# Submit a flag
pyhtb machine own Checkpoint <flag>

# Stop or reset the active machine
pyhtb machine stop
pyhtb machine reset
```

### Challenges

```bash
# List challenges, optionally filtered by category
pyhtb challenge list --category Web --search void

# Show challenge details (docker status, ports, etc.)
pyhtb challenge info spookifier

# Start/stop a Docker container (by name or ID)
pyhtb challenge start spookifier
pyhtb challenge stop spookifier

# Submit a flag
pyhtb challenge own spookifier <flag>
```

### VPN

```bash
# Check active VPN connections
pyhtb vpn status

# List available VPN servers
pyhtb vpn servers --pool labs

# Switch to a different VPN server
pyhtb vpn switch 113

# Download an .ovpn config file
pyhtb vpn download 113 -o lab.ovpn
pyhtb vpn download 113 --tcp
```

### Search & Profile

```bash
# Global search across machines and challenges
pyhtb search void

# Display your authenticated profile
pyhtb whoami
```

Commands exit with a nonzero status on failure (missing token, unresolved target, API errors, rejected flags), so they compose cleanly in scripts:

```bash
pyhtb machine own Checkpoint "$FLAG" && echo "owned!" || echo "submission failed"
```

> **Note**: The CLI is a proof-of-concept companion to the SDK. It covers the most common workflows but does not expose every API endpoint. Use the SDK directly for broader endpoint access.

---

## Code Regeneration

The SDK contains a build pipeline to automatically compile clients from raw OpenAPI YAML specs and refresh the generated public facade plus typing stub. To regenerate the submodules after modifying any specification, execute:

```bash
./api/regen.sh
```

This requires the code generation extra:

```bash
python -m pip install -e '.[codegen]'
```

---

## License

This project is released under the [Unlicense](LICENSE) — dedicated to the public domain. See the [LICENSE](LICENSE) file for details.
