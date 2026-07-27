import os
from pathlib import Path

import spotipy
from dotenv import load_dotenv
from spotipy.cache_handler import CacheFileHandler
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


load_dotenv()

USER_SCOPES = "user-read-private user-read-email user-read-recently-played"


class CredentialsManager:
    @staticmethod
    def _require(*names: str) -> list[str]:
        values = []
        missing = []
        for name in names:
            legacy_name = name.replace("SPOTIPY_", "SPOTIFY_")
            value = os.getenv(name) or os.getenv(legacy_name)
            if value:
                values.append(value)
            else:
                missing.append(name)
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
        return values

    @classmethod
    def build_client_credentials_spotify(cls) -> spotipy.Spotify:
        client_id, client_secret = cls._require(
            "SPOTIPY_CLIENT_ID", "SPOTIPY_CLIENT_SECRET"
        )
        return spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(
                client_id=client_id,
                client_secret=client_secret,
            )
        )

    @classmethod
    def build_user_oauth_spotify(
        cls, cache_path: str | Path = ".spotify_token_cache"
    ) -> spotipy.Spotify:
        client_id, client_secret, redirect_uri = cls._require(
            "SPOTIPY_CLIENT_ID", "SPOTIPY_CLIENT_SECRET", "SPOTIPY_REDIRECT_URI"
        )
        auth_manager = SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=USER_SCOPES,
            cache_handler=CacheFileHandler(cache_path=str(cache_path)),
        )
        return spotipy.Spotify(auth_manager=auth_manager)

    @staticmethod
    def get_recently_played(sp: spotipy.Spotify, limit: int = 50) -> dict:
        if not 1 <= limit <= 50:
            raise ValueError("limit must be between 1 and 50")
        return sp.current_user_recently_played(limit=limit)

    @staticmethod
    def get_audio_features(sp: spotipy.Spotify, track_ids: list[str]) -> list[dict | None]:
        return sp.audio_features(track_ids)

    @staticmethod
    def aggregate_listening_data(recently_played: dict) -> list[dict]:
        items = []
        for item in recently_played.get("items", []):
            track = item.get("track") or {}
            artists = track.get("artists") or []
            items.append(
                {
                    "played_at": item.get("played_at"),
                    "track_name": track.get("name"),
                    "artist": artists[0].get("name") if artists else None,
                    "track_id": track.get("id"),
                    "duration_ms": track.get("duration_ms"),
                }
            )
        return items


def get_recently_played(sp: spotipy.Spotify, limit: int = 50) -> dict:
    return CredentialsManager.get_recently_played(sp, limit=limit)


def get_audio_features(sp: spotipy.Spotify, track_ids: list[str]) -> list[dict | None]:
    return CredentialsManager.get_audio_features(sp, track_ids)


def aggregate_listening_data(recently_played: dict) -> list[dict]:
    return CredentialsManager.aggregate_listening_data(recently_played)
