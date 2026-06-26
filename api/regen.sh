#!/bin/bash
set -e

# Get the directory of the script and resolve the project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Prefer the project virtualenv, but allow an active environment/PATH install.
if [ -x "$PROJECT_ROOT/.venv/bin/openapi-python-client" ]; then
    OPENAPI_PYTHON_CLIENT="$PROJECT_ROOT/.venv/bin/openapi-python-client"
elif command -v openapi-python-client >/dev/null 2>&1; then
    OPENAPI_PYTHON_CLIENT="$(command -v openapi-python-client)"
else
    echo "Error: openapi-python-client not found."
    echo "Please install it in .venv or activate an environment that provides it."
    exit 1
fi

echo "Cleaning previous generated clients..."
rm -rf "$PROJECT_ROOT/pyhtb/v4"
rm -rf "$PROJECT_ROOT/pyhtb/v5"
rm -rf "$PROJECT_ROOT/pyhtb/experience/v1"

# Create directories in case they don't exist
mkdir -p "$PROJECT_ROOT/pyhtb/v4"
mkdir -p "$PROJECT_ROOT/pyhtb/v5"
mkdir -p "$PROJECT_ROOT/pyhtb/experience/v1"

echo "Generating v4 client..."
"$OPENAPI_PYTHON_CLIENT" generate \
    --meta none \
    --path "$PROJECT_ROOT/api/v4/openapi.v4.yaml" \
    --output-path "$PROJECT_ROOT/pyhtb/v4" \
    --overwrite

echo "Generating v5 client..."
"$OPENAPI_PYTHON_CLIENT" generate \
    --meta none \
    --path "$PROJECT_ROOT/api/v5/openapi.v5.yaml" \
    --output-path "$PROJECT_ROOT/pyhtb/v5" \
    --overwrite

echo "Generating experience/v1 client..."
"$OPENAPI_PYTHON_CLIENT" generate \
    --meta none \
    --path "$PROJECT_ROOT/api/experience/v1/openapi.experience.v1.yaml" \
    --output-path "$PROJECT_ROOT/pyhtb/experience/v1" \
    --overwrite

# Create __init__.py files if missing
touch "$PROJECT_ROOT/pyhtb/__init__.py"
touch "$PROJECT_ROOT/pyhtb/experience/__init__.py"

echo "Generating public facade and typing stub..."
python "$PROJECT_ROOT/scripts/generate_init_stub.py"

echo "Code generation complete!"
