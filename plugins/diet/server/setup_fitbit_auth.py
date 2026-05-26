# /// script
# dependencies = ["httpx"]
# ///

import base64
import json
import time
import urllib.parse
from pathlib import Path

import httpx

SECRETS_FILE = Path(__file__).parent / "secrets.json"
TOKENS_FILE = Path(__file__).parent / "tokens.json"

secrets = json.loads(SECRETS_FILE.read_text())
CLIENT_ID = secrets["fitbit_client_id"]
CLIENT_SECRET = secrets["fitbit_client_secret"]
REDIRECT_URI = "http://localhost"
TOKEN_URL = "https://api.fitbit.com/oauth2/token"

auth_url = (
    "https://www.fitbit.com/oauth2/authorize"
    f"?response_type=code"
    f"&client_id={CLIENT_ID}"
    f"&redirect_uri={urllib.parse.quote(REDIRECT_URI, safe='')}"
    f"&scope=activity%20heartrate%20nutrition%20profile%20settings%20sleep%20weight"
    f"&state=diet_setup"
)

print("\n1. Open this URL in your browser:\n")
print(f"   {auth_url}\n")
print("2. Log in and approve access.")
print("3. You'll be redirected to http://localhost — the page won't load, that's fine.")
print("4. Copy the full URL from the browser address bar and paste it here.\n")

redirect = input("Paste the redirect URL (or just the code): ").strip()

if redirect.startswith("http"):
    parsed = urllib.parse.urlparse(redirect)
    params = urllib.parse.parse_qs(parsed.query)
    if "code" not in params:
        print(f"\nERROR: no 'code' found in URL. Got params: {params}")
        raise SystemExit(1)
    code = params["code"][0]
else:
    code = redirect
print(f"\nGot code: {code[:12]}...")

auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
r = httpx.post(
    TOKEN_URL,
    headers={
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded",
    },
    data={
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    },
)

if not r.is_success:
    print(f"\nERROR {r.status_code}: {r.text}")
    raise SystemExit(1)

result = r.json()
tokens = {
    "access_token": result["access_token"],
    "refresh_token": result["refresh_token"],
    "expires_at": time.time() + result.get("expires_in", 28800),
}

try:
    all_tokens = json.loads(TOKENS_FILE.read_text())
except (FileNotFoundError, json.JSONDecodeError):
    all_tokens = {}

all_tokens["fitbit"] = tokens
TOKENS_FILE.write_text(json.dumps(all_tokens, indent=2))

print("\nFitBit tokens saved. Run fetch.py to test.")
