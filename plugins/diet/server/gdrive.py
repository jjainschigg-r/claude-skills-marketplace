# /// script
# dependencies = ["httpx"]
# ///
"""
Google Drive accessor for Contour CSV exports.

Handles OAuth2 token management (lazy refresh) and exposes:
  list_contour_files()  -> list of {id, name, modified} dicts, newest first
  fetch_file(file_id)   -> file content as str
  fetch_contour(date)   -> content of ContourCSVReport file for date (YYYY-MM-DD),
                           or most recent if date is None
"""

import json
import time
import urllib.parse
from pathlib import Path

import httpx

CREDENTIALS_FILE = Path(__file__).parent / "gdrive_credentials.json"
TOKENS_FILE = Path(__file__).parent / "gdrive_tokens.json"
TOKEN_URL = "https://oauth2.googleapis.com/token"
FILES_URL = "https://www.googleapis.com/drive/v3/files"
DOWNLOAD_URL = "https://www.googleapis.com/drive/v3/files/{file_id}?alt=media"
FILE_PREFIX = "ContourCSVReport"


def _load_credentials() -> dict:
    raw = json.loads(CREDENTIALS_FILE.read_text())
    return raw.get("installed") or raw.get("web") or raw


def _load_tokens() -> dict:
    try:
        return json.loads(TOKENS_FILE.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _save_tokens(tokens: dict):
    TOKENS_FILE.write_text(json.dumps(tokens, indent=2))


def refresh() -> dict:
    creds = _load_credentials()
    tokens = _load_tokens()
    r = httpx.post(
        TOKEN_URL,
        data={
            "grant_type": "refresh_token",
            "client_id": creds["client_id"],
            "client_secret": creds["client_secret"],
            "refresh_token": tokens["refresh_token"],
        },
    )
    if not r.is_success:
        raise RuntimeError(f"GDrive token refresh failed {r.status_code}: {r.text}")
    result = r.json()
    tokens = {
        "access_token": result["access_token"],
        "refresh_token": tokens["refresh_token"],  # Google doesn't rotate refresh tokens
        "expires_at": time.time() + result.get("expires_in", 3600),
    }
    _save_tokens(tokens)
    return tokens


def _access_token() -> str:
    tokens = _load_tokens()
    if not tokens or time.time() > tokens.get("expires_at", 0) - 300:
        tokens = refresh()
    return tokens["access_token"]


def list_contour_files() -> list[dict]:
    """Return all ContourCSVReport files on Drive, newest first."""
    token = _access_token()
    q = f"name contains '{FILE_PREFIX}' and trashed=false"
    r = httpx.get(
        FILES_URL,
        headers={"Authorization": f"Bearer {token}"},
        params={
            "q": q,
            "orderBy": "name desc",
            "fields": "files(id,name,modifiedTime)",
            "pageSize": 50,
        },
    )
    r.raise_for_status()
    return r.json().get("files", [])


def fetch_file(file_id: str) -> str:
    """Download a Drive file by ID and return its content as a string."""
    token = _access_token()
    r = httpx.get(
        DOWNLOAD_URL.format(file_id=file_id),
        headers={"Authorization": f"Bearer {token}"},
        follow_redirects=True,
    )
    r.raise_for_status()
    return r.text


def fetch_contour(date: str | None = None) -> tuple[str, str]:
    """
    Find and download the Contour export for a given date (YYYY-MM-DD),
    or the most recent file if date is None.

    Returns (filename, content).
    Raises FileNotFoundError if no matching file exists.
    """
    files = list_contour_files()
    if not files:
        raise FileNotFoundError("No ContourCSVReport files found on Google Drive")

    if date is not None:
        # filename pattern: ContourCSVReport_YYYY_MM_DD.csv
        date_slug = date.replace("-", "_")
        matches = [f for f in files if date_slug in f["name"]]
        if not matches:
            raise FileNotFoundError(
                f"No ContourCSVReport file found for {date} on Google Drive\n"
                f"Available: {[f['name'] for f in files[:5]]}"
            )
        target = matches[0]
    else:
        target = files[0]

    content = fetch_file(target["id"])
    return target["name"], content
