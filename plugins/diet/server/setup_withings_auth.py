# /// script
# dependencies = ["httpx"]
# ///

import json
import time
import urllib.parse
from pathlib import Path

import httpx

SECRETS_FILE = Path(__file__).parent / "secrets.json"
TOKENS_FILE = Path(__file__).parent / "tokens.json"

secrets = json.loads(SECRETS_FILE.read_text())
CLIENT_ID = secrets["withings_client_id"]
CLIENT_SECRET = secrets["withings_client_secret"]
REDIRECT_URI = "http://localhost"
TOKEN_URL = "https://wbsapi.withings.net/v2/oauth2"

auth_url = (
    "https://account.withings.com/oauth2_user/authorize2"
    f"?response_type=code"
    f"&client_id={CLIENT_ID}"
    f"&redirect_uri={urllib.parse.quote(REDIRECT_URI, safe='')}"
    f"&scope=user.metrics,user.activity,user.sleepevents"
    f"&state=diet_setup"
)

print("\n1. Open this URL in your browser:\n")
print(f"   {auth_url}\n")
print("2. Log in and approve access.")
print("3. You'll be redirected to http://localhost — the page won't load, that's fine.")
print("4. Copy the full URL from the browser address bar and paste it here.")
print("   (or just the bare code if that's easier)\n")

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

r = httpx.post(
    TOKEN_URL,
    data={
        "action": "requesttoken",
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI,
    },
)

if not r.is_success:
    print(f"\nERROR {r.status_code}: {r.text}")
    raise SystemExit(1)

result = r.json()
if result.get("status") != 0:
    print(f"\nERROR: Withings returned status {result.get('status')}: {result}")
    raise SystemExit(1)

body = result["body"]
tokens = {
    "access_token": body["access_token"],
    "refresh_token": body["refresh_token"],
    "expires_at": time.time() + body.get("expires_in", 10800),
}

try:
    all_tokens = json.loads(TOKENS_FILE.read_text())
except (FileNotFoundError, json.JSONDecodeError):
    all_tokens = {}

all_tokens["withings"] = tokens
TOKENS_FILE.write_text(json.dumps(all_tokens, indent=2))

print("\nWithings tokens saved. Run fetch.py to test.")
