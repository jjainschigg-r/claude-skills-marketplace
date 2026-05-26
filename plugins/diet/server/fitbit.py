import base64
import json
import time
from pathlib import Path

import httpx

SECRETS_FILE = Path(__file__).parent / "secrets.json"
TOKENS_FILE = Path(__file__).parent / "tokens.json"
TOKEN_URL = "https://api.fitbit.com/oauth2/token"
API_BASE = "https://api.fitbit.com"


def _load_secrets() -> dict:
    return json.loads(SECRETS_FILE.read_text())


def _load_tokens() -> dict:
    return json.loads(TOKENS_FILE.read_text()).get("fitbit", {})


def _save_tokens(tokens: dict):
    path = TOKENS_FILE
    try:
        all_tokens = json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        all_tokens = {}
    all_tokens["fitbit"] = tokens
    path.write_text(json.dumps(all_tokens, indent=2))


def refresh() -> dict:
    secrets = _load_secrets()
    refresh_token = _load_tokens()["refresh_token"]
    auth = base64.b64encode(
        f"{secrets['fitbit_client_id']}:{secrets['fitbit_client_secret']}".encode()
    ).decode()
    r = httpx.post(
        TOKEN_URL,
        headers={
            "Authorization": f"Basic {auth}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={"grant_type": "refresh_token", "refresh_token": refresh_token},
    )
    if not r.is_success:
        raise RuntimeError(f"FitBit token refresh failed {r.status_code}: {r.text}")
    result = r.json()
    tokens = {
        "access_token": result["access_token"],
        "refresh_token": result["refresh_token"],
        "expires_at": time.time() + result.get("expires_in", 28800),
    }
    _save_tokens(tokens)
    print("  [fitbit] tokens refreshed")
    return tokens


def _access_token() -> str:
    tokens = _load_tokens()
    if not tokens or time.time() > tokens.get("expires_at", 0) - 300:
        tokens = refresh()
    return tokens["access_token"]


def fetch(date: str) -> dict:
    """Return FitBit daily metrics for date (YYYY-MM-DD)."""
    token = _access_token()
    headers = {"Authorization": f"Bearer {token}"}

    def get(url):
        r = httpx.get(url, headers=headers)
        r.raise_for_status()
        return r.json()

    activity = get(f"{API_BASE}/1/user/-/activities/date/{date}.json")["summary"]
    sleep_raw = get(f"{API_BASE}/1.2/user/-/sleep/date/{date}.json")["summary"]
    weight_raw = get(f"{API_BASE}/1/user/-/body/log/weight/date/{date}.json")
    weight_entry = (weight_raw.get("weight") or [None])[0]

    return {
        "date": date,
        "steps": activity.get("steps"),
        "calories_out": activity.get("caloriesOut"),
        "sedentary_minutes": activity.get("sedentaryMinutes"),
        "lightly_active_minutes": activity.get("lightlyActiveMinutes"),
        "fairly_active_minutes": activity.get("fairlyActiveMinutes"),
        "very_active_minutes": activity.get("veryActiveMinutes"),
        "sleep_minutes": sleep_raw.get("totalMinutesAsleep"),
        "time_in_bed": sleep_raw.get("totalTimeInBed"),
        "weight_lbs": weight_entry.get("weight") if weight_entry else None,
        "body_fat_pct": weight_entry.get("fat") if weight_entry else None,
    }
