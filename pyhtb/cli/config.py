import os
from pathlib import Path
from typing import Optional

CONFIG_DIR = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config")) / "pyhtb"
TOKEN_FILE = CONFIG_DIR / "token"

def load_token() -> Optional[str]:
    """
    Loads the HTB API token.
    Precedence:
    1. Environment variable HTB_TOKEN
    2. Environment variable HTB_API_KEY
    3. Stored token file in ~/.config/pyhtb/token
    """
    # Check environment variables
    env_token = os.environ.get("HTB_TOKEN") or os.environ.get("HTB_API_KEY")
    if env_token:
        return env_token.strip()

    # Check stored token file
    if TOKEN_FILE.exists():
        try:
            with open(TOKEN_FILE, "r") as f:
                return f.read().strip()
        except IOError:
            pass
    return None

def save_token(token: str) -> None:
    """
    Saves the API token securely to ~/.config/pyhtb/token with owner-only permissions.
    """
    token = token.strip()
    
    # Ensure config directory exists
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    
    # Touch/create file with owner-only read/write permissions (0600)
    # On Unix, we open with flags to set permissions during creation
    try:
        # Remove existing file to reset permissions
        if TOKEN_FILE.exists():
            TOKEN_FILE.unlink()
            
        fd = os.open(TOKEN_FILE, os.O_WRONLY | os.O_CREAT, 0o600)
        with os.fdopen(fd, "w") as f:
            f.write(token)
    except Exception as e:
        raise IOError(f"Failed to write token file: {e}")

def delete_token() -> None:
    """
    Deletes the stored API token.
    """
    if TOKEN_FILE.exists():
        try:
            TOKEN_FILE.unlink()
        except Exception as e:
            raise IOError(f"Failed to delete token file: {e}")
