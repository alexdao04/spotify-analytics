import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from .spotify_api import CredentialsManager


class DataWriter:
    @staticmethod
    def save_recently_played(
        user_id: str, recently_played: dict, output_root: Path = Path("data/raw")
    ) -> Path:
        if not user_id.startswith("user_"):
            raise ValueError(
                "user_id must use the anonymous format user_01, user_02, etc."
            )

        output_dir = output_root / user_id
        output_dir.mkdir(parents=True, exist_ok=True)
        collected_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
        output_file = output_dir / f"{collected_at}-recently-played.json"

        with output_file.open("x", encoding="utf-8") as file:
            json.dump(recently_played, file, indent=2, ensure_ascii=False)
            file.write("\n")

        return output_file


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch and save a participant's recently played Spotify tracks."
    )
    parser.add_argument("--user-id", required=True, help="Anonymous ID, e.g. user_01")
    parser.add_argument("--limit", type=int, default=50, help="Tracks to fetch (1–50)")
    args = parser.parse_args()

    token_cache = Path(".spotify_tokens") / f"{args.user_id}.json"
    token_cache.parent.mkdir(parents=True, exist_ok=True)
    spotify = CredentialsManager.build_user_oauth_spotify(cache_path=token_cache)
    recently_played = CredentialsManager.get_recently_played(spotify, limit=args.limit)
    output_file = DataWriter.save_recently_played(args.user_id, recently_played)
    print(f"Saved raw Spotify data to {output_file}")


if __name__ == "__main__":
    main()
