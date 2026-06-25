import pkgutil
import importlib
import functools
from typing import Optional
import httpx

from .v4.client import AuthenticatedClient as AuthenticatedClientV4Gen, Client as ClientV4Gen
from .v5.client import AuthenticatedClient as AuthenticatedClientV5Gen, Client as ClientV5Gen
from .experience.v1.client import AuthenticatedClient as AuthenticatedClientV1Gen, Client as ClientV1Gen

# Import the API modules for binding
from .v4 import api as api_v4
from .v5 import api as api_v5
from .experience.v1 import api as api_exp_v1

# Subclass the generated clients so they support dynamic attribute/method binding
# (since attrs classes with slots=True don't have a __dict__ by default)
class ClientV4(ClientV4Gen):
    pass

class AuthenticatedClientV4(AuthenticatedClientV4Gen):
    pass

class ClientV5(ClientV5Gen):
    pass

class AuthenticatedClientV5(AuthenticatedClientV5Gen):
    pass

class ClientV1(ClientV1Gen):
    pass

class AuthenticatedClientV1(AuthenticatedClientV1Gen):
    pass

def _bind_api_methods(client_instance, api_package):
    """
    Dynamically scans an API subpackage and attaches its endpoints as methods
    directly on the client instance, automatically injecting the client parameter.
    """
    for _, module_name, is_pkg in pkgutil.walk_packages(api_package.__path__, api_package.__name__ + "."):
        if is_pkg:
            continue
        try:
            mod = importlib.import_module(module_name)
        except Exception:
            continue
        
        endpoint_name = module_name.split(".")[-1]
        
        # We bind the following:
        # - sync -> client.endpoint_name()
        # - sync_detailed -> client.endpoint_name_detailed()
        # - asyncio -> client.endpoint_name_async()
        # - asyncio_detailed -> client.endpoint_name_async_detailed()
        for attr_name, bound_name in [
            ("sync", endpoint_name),
            ("asyncio", f"{endpoint_name}_async"),
            ("sync_detailed", f"{endpoint_name}_detailed"),
            ("asyncio_detailed", f"{endpoint_name}_async_detailed"),
        ]:
            func = getattr(mod, attr_name, None)
            if func and callable(func):
                def make_wrapper(f):
                    @functools.wraps(f)
                    def wrapper(*args, **kwargs):
                        kwargs["client"] = client_instance
                        return f(*args, **kwargs)
                    return wrapper

                setattr(client_instance, bound_name, make_wrapper(func))

class PyHTB:
    """
    Main entrypoint wrapper for the Hack The Box Python SDK.
    Manages API clients for:
    - v4 (via client.v4)
    - v5 (via client.v5)
    - experience/v1 (via client.experience_v1)

    All generated endpoints are bound directly as methods on the client instances
    so you don't need to import them manually or pass the client parameter.
    For example:
        client = PyHTB(token="my_token")
        machines = client.v5.get_machines()
    """
    def __init__(
        self,
        token: Optional[str] = None,
        base_url_v4: str = "https://labs.hackthebox.com/api/v4",
        base_url_v5: str = "https://labs.hackthebox.com/api/v5",
        base_url_experience_v1: str = "https://labs.hackthebox.com/api/experience/v1",
        timeout: Optional[float] = None,
        verify_ssl: bool = True,
    ):
        httpx_timeout = httpx.Timeout(timeout) if timeout is not None else None

        if token:
            self.v4 = AuthenticatedClientV4(
                base_url=base_url_v4,
                token=token,
                timeout=httpx_timeout,
                verify_ssl=verify_ssl,
            )
            self.v5 = AuthenticatedClientV5(
                base_url=base_url_v5,
                token=token,
                timeout=httpx_timeout,
                verify_ssl=verify_ssl,
            )
            self.experience_v1 = AuthenticatedClientV1(
                base_url=base_url_experience_v1,
                token=token,
                timeout=httpx_timeout,
                verify_ssl=verify_ssl,
            )
        else:
            self.v4 = ClientV4(
                base_url=base_url_v4,
                timeout=httpx_timeout,
                verify_ssl=verify_ssl,
            )
            self.v5 = ClientV5(
                base_url=base_url_v5,
                timeout=httpx_timeout,
                verify_ssl=verify_ssl,
            )
            self.experience_v1 = ClientV1(
                base_url=base_url_experience_v1,
                timeout=httpx_timeout,
                verify_ssl=verify_ssl,
            )

        # Bind API methods directly to client instances for ultimate developer simplicity
        _bind_api_methods(self.v4, api_v4)
        _bind_api_methods(self.v5, api_v5)
        _bind_api_methods(self.experience_v1, api_exp_v1)

__all__ = ["PyHTB"]
