# Unofficial Hack The Box (HTB) Python SDK & API Client (`pyhtb`)

[![PyPI Version](https://img.shields.io/pypi/v/pyhtb.svg?color=blue)](https://pypi.org/project/pyhtb/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/pyhtb.svg)](https://pypi.org/project/pyhtb/)
[![License](https://img.shields.io/github/license/Gubarz/pyhtb.svg)](LICENSE)
[![Code Style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

An unofficial, modern, and type-safe Python SDK and API client wrapper for the **Hack The Box (HTB)** platform. This library exposes fully type-hinted synchronous and asynchronous interfaces to interact programmatically with HTB APIs.

Whether you are automating machine status checking, managing teams, tracking starting point progression, or scripting challenge submissions, `pyhtb` provides a single unified interface.

---

## Key Features

* **Complete API Coverage**: Seamlessly combines the HTB API `v4`, `v5`, and `experience/v1` specifications.
* **Cookie-Simple Developer Experience**: No deep package imports or manually passing connection objects. Endpoints are dynamically bound directly onto the version clients.
* **Modern Async & Sync Backend**: Powered by `httpx` for fast, lightweight HTTP execution with full async support out of the box.
* **Type Safety & IDE Autocomplete**: Generated with strict model definitions utilizing `attrs` and type hints for robust code completion.
* **Zero Overhead Boilerplate**: Authenticate once, and credentials automatically propagate across all supported API versions.

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

`pyhtb` ships with an experimental command-line interface that wraps the SDK into a quick-fire workflow tool. After installing the package, the `yahtbcli` command is available globally.

### Authentication

```bash
# Store your HTB App Token (generates from app.hackthebox.com → Settings → App Tokens)
yahtbcli auth set

# Or pass it inline
yahtbcli auth set --token eyJ...

# Verify your credentials
yahtbcli auth status

# You can also export the token as an environment variable
export HTB_TOKEN="eyJ..."
```

### Machines

```bash
# List active machines
yahtbcli machine list

# List retired machines, filtered by difficulty
yahtbcli machine list --retired --difficulty hard --os linux

# Show detailed info for a machine (by name or ID)
yahtbcli machine info Checkpoint

# Start a machine and wait for IP assignment
yahtbcli machine start Checkpoint

# Check your active machine
yahtbcli machine active

# Submit a flag
yahtbcli machine own Checkpoint <flag>

# Stop or reset the active machine
yahtbcli machine stop
yahtbcli machine reset
```

### Challenges

```bash
# List challenges, optionally filtered by category
yahtbcli challenge list --category Web --search void

# Show challenge details (docker status, ports, etc.)
yahtbcli challenge info spookifier

# Start/stop a Docker container (by name or ID)
yahtbcli challenge start spookifier
yahtbcli challenge stop spookifier

# Submit a flag
yahtbcli challenge own spookifier <flag>
```

### VPN

```bash
# Check active VPN connections
yahtbcli vpn status

# List available VPN servers
yahtbcli vpn servers --pool labs

# Switch to a different VPN server
yahtbcli vpn switch 113

# Download an .ovpn config file
yahtbcli vpn download 113 -o lab.ovpn
yahtbcli vpn download 113 --tcp
```

### Search & Profile

```bash
# Global search across machines and challenges
yahtbcli search void

# Display your authenticated profile
yahtbcli whoami
```

> **Note**: The CLI is a proof-of-concept companion to the SDK. It covers the most common workflows but does not expose every API endpoint. Use the SDK directly for full coverage.

---

## Code Regeneration

The SDK contains a build pipeline to automatically compile clients from raw OpenAPI YAML specs. To regenerate the submodules after modifying any specification, execute:

```bash
./api/regen.sh
```

This requires `openapi-python-client` to be installed in your active Python environment.

---

## License

This project is released under the [Unlicense](LICENSE) — dedicated to the public domain. See the [LICENSE](LICENSE) file for details.
