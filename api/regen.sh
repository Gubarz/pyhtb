#!/bin/bash
set -e

# Get the directory of the script and resolve the project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Verify the virtual environment exists
VENV_BIN="$PROJECT_ROOT/.venv/bin"
if [ ! -f "$VENV_BIN/openapi-python-client" ]; then
    echo "Error: openapi-python-client not found in $PROJECT_ROOT/.venv."
    echo "Please set up the virtual environment first."
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
"$VENV_BIN/openapi-python-client" generate \
    --meta none \
    --path "$PROJECT_ROOT/api/v4/openapi.v4.yaml" \
    --output-path "$PROJECT_ROOT/pyhtb/v4" \
    --overwrite

echo "Generating v5 client..."
"$VENV_BIN/openapi-python-client" generate \
    --meta none \
    --path "$PROJECT_ROOT/api/v5/openapi.v5.yaml" \
    --output-path "$PROJECT_ROOT/pyhtb/v5" \
    --overwrite

echo "Generating experience/v1 client..."
"$VENV_BIN/openapi-python-client" generate \
    --meta none \
    --path "$PROJECT_ROOT/api/experience/v1/openapi.experience.v1.yaml" \
    --output-path "$PROJECT_ROOT/pyhtb/experience/v1" \
    --overwrite

# Create __init__.py files if missing
touch "$PROJECT_ROOT/pyhtb/__init__.py"
touch "$PROJECT_ROOT/pyhtb/experience/__init__.py"

echo "Code generation complete!"
