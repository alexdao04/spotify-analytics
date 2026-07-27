from .spotify_api import CredentialsManager

__all__ = ["CredentialsManager", "DataWriter"]


def __getattr__(name: str):
    if name == "DataWriter":
        from .datawrite import DataWriter

        return DataWriter
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
