# diet

A Claude Code plugin for tracking daily food intake and biometric readings against evidence-based cardiometabolic targets. Implements a Portfolio Diet + Mediterranean-DASH hybrid targeting LDL reduction, blood pressure control, insulin resistance, and metabolic aging — with per-meal nutritional accounting and gap analysis on the metrics that matter most.

---

## Prerequisites

### Data files

Two CSV files must exist in your project directory before using the skills. Create them with these exact headers:

**compliance.csv**
```
date,meal_context,food_item,amount_g,kcal,protein_g,sat_fat_g,soy_protein_g,omega3_g,soluble_fiber_g,sodium_mg,notes
```

**biometrics.csv**
```
date,time,metric,value,unit,notes
```

### Device credentials (optional — required for `fetch` and `pull` only)

`/diet log`, `/diet biometrics`, and `/diet summary` work with no credentials. The `fetch` and `pull` operations pull data from Withings, FitBit, and optionally Google Drive, and require OAuth credentials set up once per device.

Run `/diet setup` after installation — it will walk you through each service interactively.

**What you'll need:**

| Service | Where to register | Notes |
|---|---|---|
| FitBit | [dev.fitbit.com](https://dev.fitbit.com) → Manage → Register an App | App type: Personal; OAuth 2.0 Application Type: Personal; Redirect URI: `http://localhost` |
| Withings | [developer.withings.com](https://developer.withings.com) → Create application | Callback URI: `http://localhost`; Scopes: user.metrics, user.activity, user.sleepevents |
| Google Drive | [Google Cloud Console](https://console.cloud.google.com) → APIs & Services → Credentials → OAuth 2.0 Client ID | Application type: Desktop; download the JSON file |

Once you have your client IDs and secrets, create `server/secrets.json` in the plugin directory:

```json
{
  "fitbit_client_id": "YOUR_FITBIT_CLIENT_ID",
  "fitbit_client_secret": "YOUR_FITBIT_CLIENT_SECRET",
  "withings_client_id": "YOUR_WITHINGS_CLIENT_ID",
  "withings_client_secret": "YOUR_WITHINGS_CLIENT_SECRET"
}
```

For Google Drive, place the downloaded credentials JSON at `server/gdrive_credentials.json`.

Then run the interactive auth scripts (in your terminal, not via Claude):

```bash
uv run server/setup_fitbit_auth.py
uv run server/setup_withings_auth.py
uv run server/setup_gdrive_auth.py   # only if using BP/glucose import
```

Each script opens a browser URL, asks you to approve access, and saves the resulting tokens. Tokens refresh automatically — you only do this once.

---

## Install

If you haven't added the marketplace yet:

```
/plugin marketplace add https://jjainschigg-r.github.io/claude-skills-marketplace/marketplace.json
```

Then install the plugin:

```
/plugin install diet@mirantis-plugins
```

## Use

### Log food intake

```
/diet log
```

Describe what you ate. Gram amounts are precise but not required — vague measures are resolved automatically: "a handful" of nuts → 30g, "a few bites" of protein → 45g, "a slice" of rugbrød → 30g, "a cup" of liquid → 240ml, and so on. Anything outside the standard defaults gets a best-guess estimate noted in the log.

Claude looks up nutritional values, appends rows to `compliance.csv`, and prints a gap analysis against your daily targets (calories, protein, saturated fat, soy protein, soluble fiber, omega-3, sodium).

Examples:
- *"300g roast broccoli, 177g baked salmon, 25g walnuts, 40g rolled oats with 100g kefir"*
- *"a handful of walnuts, a few bites of salmon, slice of rugbrød"*
- *"a bowl of lentil soup, some edamame, did all the supplements"*

### Log a biometric reading

```
/diet biometrics
```

Report weight, blood pressure, glucose, or lipid values. Claude appends each reading as a row to `biometrics.csv` and automatically computes BMI whenever weight is given.

Example: *"weight 197 lbs, BP 122/76"*

### Show today's summary

```
/diet summary
```

Reads today's rows from `compliance.csv` and prints a full gap analysis — useful for checking where you stand mid-day or at the end of the day without re-logging anything.

### Pull device data

```
/diet fetch [YYYY-MM-DD]
```

Pulls Withings (body composition, sleep, steps) and FitBit (activity, sleep, weight) data for a date and appends it to `biometrics.csv`. Defaults to yesterday if no date given.

```
/diet pull [YYYY-MM-DD]
```

Full device pull: Withings + FitBit via `fetch.py`, blood pressure via `bp_import.py`, and glucose via `contour_gdrive.py`. Requires the MCP server and supporting Python scripts in `server/`.

---

## How it works

Each skill embeds the full CSV schema, metric vocabulary, daily target table, and nutritional reference values in its definition. No conversation history is required — every invocation is self-contained and produces consistent output regardless of prior context. The skills are prompt-only: Claude reads and appends files using its built-in file tools.

Logging is incremental — you can call `/diet log` multiple times throughout the day, once per meal or supplement dose. Claude reads existing rows for today, skips anything already logged, and updates the running daily total each time.

The daily targets are derived from the Portfolio Diet (Jenkins et al.), DASH dietary pattern, and Mediterranean diet literature:

| Metric | Target | Source |
|---|---|---|
| Calories | ~1600 kcal | Personalised for insulin resistance |
| Soy protein | ≥22 g/day | Portfolio Diet |
| Soluble fiber | ≥20 g/day | Portfolio Diet |
| Omega-3 (EPA+DHA) | ≥3 g/day | AHA / PREDIMED |
| Sodium | <1500 mg/day | DASH |
| Saturated fat | <15 g/day | AHA |

---

## Details

| | |
|---|---|
| **Version** | 1.0.0 |
| **Maintained by** | Mirantis |
