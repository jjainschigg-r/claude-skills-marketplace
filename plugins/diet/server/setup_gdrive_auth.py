# /// script
# dependencies = ["httpx"]
# ///

import json
import time
import urllib.parse
from pathlib import Path

import httpx

CREDENTIALS_FILE = Path(__file__).parent / "gdrive_credentials.json"
TOKENS_FILE = Path(__file__).parent / "gdrive_tokens.json"
TOKEN_URL = "https://oauth2.googleapis.com/token"
REDIRECT_URI = "http://localhost"
SCOPE = "https://www.googleapis.com/auth/drive.readonly"

if not CREDENTIALS_FILE.exists():
    print(f"\nERROR: {CREDENTIALS_FILE} not found.")
    print("Download it from Google Cloud Console → APIs & Services → Credentials")
    print("(OAuth 2.0 Client ID → Desktop app → Download JSON)")
    raise SystemExit(1)

raw = json.loads(CREDENTIALS_FILE.read_text())
creds = raw.get("installed") or raw.get("web") or raw
CLIENT_ID = creds["client_id"]
CLIENT_SECRET = creds["client_secret"]

auth_url = (
    "https://accounts.google.com/o/oauth2/v2/auth"
    f"?response_type=code"
    f"&client_id={CLIENT_ID}"
    f"&redirect_uri={urllib.parse.quote(REDIRECT_URI, safe='')}"
    f"&scope={urllib.parse.quote(SCOPE, safe='')}"
    f"&access_type=offline"
    f"&prompt=consent"
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

r = httpx.post(
    TOKEN_URL,
    data={
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
if "access_token" not in result:
    print(f"\nERROR: unexpected response: {result}")
    raise SystemExit(1)

tokens = {
    "access_token": result["access_token"],
    "refresh_token": result["refresh_token"],
    "expires_at": time.time() + result.get("expires_in", 3600),
}

TOKENS_FILE.write_text(json.dumps(tokens, indent=2))
print("\nGDrive tokens saved. Run contour_gdrive.py to test.")
