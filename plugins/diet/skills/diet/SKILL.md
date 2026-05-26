---
name: diet
description: Track food intake and biometric readings against cardiometabolic targets — invoke with log, biometrics, summary, fetch, or pull
---

Read the first word of the user's message to determine the operation: `log`, `biometrics`, `summary`, `fetch`, or `pull`. Follow the instructions for that operation below.

If no operation is given or the operation is unrecognised, print:

```
Usage:
  /diet setup       — first-time setup: height, CSV files, device credentials
  /diet log         — log food intake and print a gap analysis
  /diet biometrics  — log a biometric reading (weight, BP, glucose, lipids)
  /diet summary     — print today's compliance summary
  /diet fetch       — pull Withings and FitBit data for a date and log to biometrics.csv
  /diet pull        — pull all device data (Withings, FitBit, Contour glucose, BP) for today
```

---

## Operation: setup

Walk the user through first-time configuration. Work through each step in order, skipping any that are already complete.

**Step 1 — Height (for BMI)**

Check `~/.local/share/diet/config.json` for a `height_m` key. If absent, ask the user for their height in feet and inches, convert to metres (1 inch = 0.0254 m), create `~/.local/share/diet/` if needed, and write `{"height_m": X.XXX}`.

**Step 2 — Data files**

Check that `compliance.csv` and `biometrics.csv` exist in the current directory with the correct headers. If either is missing, create it with its header row:

```
compliance.csv:  date,meal_context,food_item,amount_g,kcal,protein_g,sat_fat_g,soy_protein_g,omega3_g,soluble_fiber_g,sodium_mg,notes
biometrics.csv:  date,time,metric,value,unit,notes
```

**Step 3 — FitBit credentials**

Check for `server/secrets.json` with a `fitbit_client_id` key, and `server/tokens.json` with a `fitbit` key.

If secrets are missing, explain:
> To connect FitBit: go to dev.fitbit.com → Manage → Register an App. Set App Type to Personal, OAuth 2.0 Application Type to Personal, and Redirect URI to `http://localhost`. Note your Client ID and Client Secret, then create `server/secrets.json`:
> ```json
> {"fitbit_client_id": "...", "fitbit_client_secret": "...", "withings_client_id": "", "withings_client_secret": ""}
> ```
> Then run in your terminal: `uv run server/setup_fitbit_auth.py`

If secrets exist but tokens are missing, tell the user to run: `uv run server/setup_fitbit_auth.py`

**Step 4 — Withings credentials**

Check for `withings_client_id` in `server/secrets.json` (non-empty) and a `withings` key in `server/tokens.json`.

If secrets are missing, explain:
> To connect Withings: go to developer.withings.com → Create application. Set Callback URI to `http://localhost`, scopes to user.metrics, user.activity, user.sleepevents. Add your Client ID and Client Secret to `server/secrets.json`.
> Then run: `uv run server/setup_withings_auth.py`

If secrets exist but tokens missing: `uv run server/setup_withings_auth.py`

**Step 5 — Google Drive (optional — for BP and glucose import)**

Check for `server/gdrive_credentials.json` and `server/gdrive_tokens.json`.

If absent, explain it is optional:
> Google Drive is only needed if you import blood pressure data from Apple Health (via Simple Health Export) or Contour glucose meter CSVs. To set up: go to Google Cloud Console → APIs & Services → Credentials → Create OAuth 2.0 Client ID (Desktop app) → download the JSON → save it as `server/gdrive_credentials.json`. Then run: `uv run server/setup_gdrive_auth.py`

**Step 6 — Summary**

Print a summary table of what is and isn't configured:

```
Setup status
────────────────────────────
Height:         ✓ X.XXX m
compliance.csv: ✓ / ✗ (created)
biometrics.csv: ✓ / ✗ (created)
FitBit:         ✓ connected / ✗ credentials missing / ✗ not authorised
Withings:       ✓ connected / ✗ credentials missing / ✗ not authorised
Google Drive:   ✓ connected / — not configured (optional)
────────────────────────────
[Next step or "Setup complete — run /diet log to start tracking"]
```

---

## Operation: log

The user logs food incrementally throughout the day — a morning smoothie, a snack, dinner, supplements. Each invocation adds new items to today's date. This is not OMAD; expect 2–5 separate log calls per day.

**Steps:**
1. Run `date +%F` to get today's date.
2. Read `compliance.csv` and identify all rows already logged for today's date — do not re-log items already present.
3. If `soy_milk_in_coffee` is not already logged for today, add it as the first new row (standing daily habit — see Standing Daily Habits below).
4. Parse each food item and amount from the user's message. For vague amounts, apply the defaults in the table below and note the estimate in the `notes` column.
5. Look up nutritional values from the reference tables; use your general knowledge for unlisted items.
6. Flag HIGH UNCERTAINTY items (see below) in the `notes` column before logging.
7. Append one row per new food item.
8. Compute updated running totals across all today's non-`daily_total` rows; append or replace the `daily_total` row.
9. Print the gap analysis.

**Vague amount defaults:**

| User says | Log as | Note |
|---|---|---|
| "a handful" (nuts) | 30g | est. |
| "a few bites" (protein) | 45g | est. |
| "a slice" (dense rye / rugbrød) | 30g | est. |
| "a scoop" (whey protein powder) | 30g | est. |
| "a tablespoon" (oil, condiment) | 14g | est. |
| "a cup" (liquid) | 240ml | est. |
| "a small handful" (berries, edamame) | 40g | est. |

**CSV schema — file: `compliance.csv`**

Header: `date,meal_context,food_item,amount_g,kcal,protein_g,sat_fat_g,soy_protein_g,omega3_g,soluble_fiber_g,sodium_mg,notes`

- `date` — YYYY-MM-DD
- `meal_context` — see vocabulary below
- `food_item` — snake_case (e.g., `baked_salmon`, `rolled_oats`)
- `amount_g` — grams; for liquids measured by volume, convert: 1ml water-density liquid ≈ 1g; note volume in `notes`
- `kcal` — kilocalories
- `protein_g` — total protein
- `sat_fat_g` — saturated fat only (not total fat)
- `soy_protein_g` — soy-derived protein only; 0 for non-soy foods; for edamame and tofu, soy_protein_g = protein_g (all protein is soy-derived)
- `omega3_g` — EPA+DHA for marine sources; ALA for plant sources; note source type in `notes`
- `soluble_fiber_g` — soluble fiber only (not total fiber); 0 if unknown or negligible
- `sodium_mg` — sodium in mg; 0 for unsalted preparations
- `notes` — preparation method, sourcing, substitutions, caveats; append `HIGH UNCERTAINTY sodium ~Xmg` for pickled/cured/restaurant items

**meal_context vocabulary:**
- `incidental` — coffee, tea, casual drinks; standing daily habits
- `main` — primary food courses of any meal
- `finisher` — oat/grain-based or dessert-style final course
- `snack` — between-meal items (nuts, fruit, cheese, etc.)
- `supplement` — fish oil capsules, plant sterols, psyllium doses, vitamins
- `daily_total` — one summary row per day; `food_item` = `TOTAL`; leave `amount_g` blank; `notes` format: `"kcal X/1600 ✓; protein X/60g ✓; sat fat X/15g ✓; soy X/22g ✓; omega3 X/3g ✓; sol fiber X/20g ✓; sodium X/1500mg ✓ — CLEAN SWEEP"` (replace ✓ with ✗ for misses; append miss count)

**Standing Daily Habits — auto-log if not already present for today:**

| food_item | amount_g | meal_context | kcal | protein_g | sat_fat_g | soy_protein_g | omega3_g | soluble_fiber_g | sodium_mg | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| soy_milk_in_coffee | 120 | incidental | 40 | 3.5 | 0.2 | 3.5 | 0 | 0 | 46 | ~120ml/day in coffee; standing daily habit |

**daily_total row format:**

`YYYY-MM-DD,daily_total,TOTAL,,<kcal>,<protein_g>,<sat_fat_g>,<soy_protein_g>,<omega3_g>,<soluble_fiber_g>,<sodium_mg>,"<gap summary>"`

Mark the day PARTIAL if the user has not yet reported dinner or supplements. Mark CLEAN SWEEP only when all targets are met.

**Daily targets:**

| Metric | Target | Rationale |
|---|---|---|
| kcal | ~1600 | caloric deficit for weight loss |
| protein_g | ≥60 g | muscle preservation |
| sat_fat_g | <15 g | AHA cardiovascular |
| soy_protein_g | ≥22 g | Portfolio Diet — LDL reduction |
| omega3_g | ≥3 g | AHA / PREDIMED; prefer EPA+DHA sources |
| soluble_fiber_g | ≥20 g | Portfolio Diet — LDL reduction |
| sodium_mg | <1500 mg | DASH — blood pressure |

**HIGH UNCERTAINTY items:**

Flag these in `notes` with `HIGH UNCERTAINTY sodium ~Xmg`. On days where any HIGH UNCERTAINTY item is present and sodium is already above ~1200mg, warn the user explicitly.

| food_item | key uncertainty | typical sodium est./100g |
|---|---|---|
| herring_jarred | brine varies by brand and lot | 700–1100 mg |
| smoked_salmon_lox | cure varies | 1100–1500 mg |
| mackerel_sashimi_salted | varies by prep/sourcing | 400–900 mg |
| any restaurant or prepared dish | recipe unknown | flag as HIGH UNCERTAINTY |

**Nutritional reference values (per 100g unless noted):**

| Food | kcal | protein_g | sat_fat_g | soy_protein_g | omega3_g | soluble_fiber_g | sodium_mg |
|---|---|---|---|---|---|---|---|
| Atlantic salmon, raw | 142 | 19.8 | 1.7 | 0 | 2.2 (EPA+DHA) | 0 | 59 |
| Atlantic salmon, baked | 208 | 20.4 | 1.6 | 0 | 2.15 (EPA+DHA) | 0 | 59 |
| Atlantic mackerel, raw | 205 | 18.6 | 4.9 | 0 | 2.6 (EPA+DHA) | 0 | 90 |
| Herring, jarred/pickled | 170 | 14.0 | 2.5 | 0 | 1.5 (EPA+DHA) | 0 | 850 HIGH UNCERTAINTY |
| Chicken breast, baked | 165 | 31.0 | 1.0 | 0 | 0 | 0 | 74 |
| Ground chicken, cooked (lean) | 148 | 25.0 | 1.5 | 0 | 0 | 0 | 95 |
| Pork loin, baked | 175 | 27.0 | 3.5 | 0 | 0.1 | 0 | 70 |
| Broccoli, roasted | 34 | 2.8 | 0 | 0 | 0.05 | 0.8 | 30 |
| Brussels sprouts, roasted | 43 | 3.4 | 0.1 | 0 | 0.1 | 1.5 | 25 |
| Sweet potato / Korean batata, baked | 86 | 1.6 | 0 | 0 | 0 | 0.8 | 55 |
| Russet potato, baked | 93 | 2.5 | 0 | 0 | 0 | 0.5 | 10 |
| Rolled oats, dry | 379 | 13.1 | 0.7 | 0 | 0.1 | 4.5 | 6 |
| Dark rye bread / rugbrød | 230 | 8.5 | 0.3 | 0 | 0 | 2.3 | 300 |
| Walnuts | 654 | 15.2 | 6.1 | 0 | 9.1 (ALA) | 1.5 | 2 |
| Almonds | 579 | 21.2 | 3.7 | 0 | 0 | 1.0 | 1 |
| Brazil nuts | 659 | 14.3 | 15.1 | 0 | 0.1 | 0.3 | 3 |
| Soy milk, unsweetened | 33 | 2.9 | 0.2 | 2.9 | 0 | 0 | 38 |
| Psyllium husk | 200 | 0 | 0 | 0 | 0 | 71 | 0 |
| Tofu, firm | 144 | 17.3 | 1.2 | 17.3 | 0.6 (ALA) | 0.3 | 14 |
| Edamame, shelled | 122 | 11.2 | 0.68 | 11.2 | 0.19 (ALA) | 1.8 | 9 |
| Chickpeas, cooked | 164 | 8.9 | 0.1 | 0 | 0 | 1.3 | 7 |
| Lentils, cooked | 116 | 9.0 | 0.1 | 0 | 0 | 1.0 | 2 |
| Barley, cooked | 123 | 2.3 | 0.1 | 0 | 0 | 0.8 | 3 |
| Flaxseed / flaxseed meal | 534 | 18.3 | 3.7 | 0 | 22.8 (ALA) | 3.5 | 30 |
| Whey protein powder | 394 | 78.8 | 1.5 | 0 | 0 | 0 | ~300 |
| Kefir, whole milk | 61 | 3.3 | 1.9 | 0 | 0.05 | 0 | 40 |
| EVOO | 884 | 0 | 13.8 | 0 | 0.8 | 0 | 0 |
| Banana, raw | 89 | 1.1 | 0.1 | 0 | 0 | 0.7 | 1 |
| Blueberries | 57 | 0.7 | 0 | 0 | 0 | 0.6 | 1 |
| Blackberries | 43 | 1.4 | 0 | 0 | 0 | 1.2 | 1 |
| Kiwi with skin | 61 | 1.1 | 0 | 0 | 0 | 1.2 | 3 |
| Apple, raw | 52 | 0.3 | 0 | 0 | 0 | 0.5 | 1 |
| Mango, frozen | 60 | 0.8 | 0 | 0 | 0 | 0.5 | 1 |
| Dried tart cherries, no sugar | 330 | 3.0 | 0 | 0 | 0 | 0 | 10 |
| Garlic | 149 | 6.4 | 0.1 | 0 | 0 | 0.6 | 17 |
| Whole milk | 61 | 3.2 | 2.0 | 0 | 0 | 0 | 43 |

*Whey protein powder: values extrapolated from label (33g = 130 kcal, 26g protein); sat fat and sodium vary by brand.*
*Brazil nuts: 3 nuts ≈ 15g ≈ ~270 mcg selenium; the upper tolerable limit is 400 mcg/day — flag if the user logs more than 3/day.*
*Rolled oats: sol fiber reflects beta-glucan content (~1.8g per 40g dry) plus residual soluble fractions.*

**Named recipes (log by name; add fruit and other add-ins as separate rows):**

| Recipe | Weight | kcal | protein_g | sat_fat_g | soy_protein_g | omega3_g | soluble_fiber_g | sodium_mg | Contents |
|---|---|---|---|---|---|---|---|---|---|
| standard_oat_bowl | 190g | 323 | 26.3 | 1.2 | 3.5 | 2.3 (ALA) | 2.5 | 111 | 40g oats + 10g flaxseed + 20g whey + 120ml soymilk |
| oat_bowl_no_whey | 170g | 247 | 10.5 | 0.9 | 3.5 | 2.3 (ALA) | 2.4 | 49 | 40g oats + 10g flaxseed + 120ml soymilk |
| soymilk_smoothie_3cup_base | ~760g | 332 | 22.8 | 1.8 | 20.9 | 2.3 (ALA) | 15.6 | 277 | 720ml soymilk + 10g flaxseed + 21g psyllium; add fruit separately |
| edamame_tameya_8pc | 216g | 261 | 24.2 | 1.5 | 24.2 | 0.4 (ALA) | 3.9 | 50 | Ground edamame + garlic + herbs; baked no oil; all protein = soy protein |
| fish_oil_standard | 9g | 27 | 0 | 0.3 | 0 | 0.9 (EPA+DHA) | 0 | 0 | 3 standard softgels |
| plant_sterols_standard | 6 caps | 10 | 0 | 0 | 0 | 0 | 0 | 0 | Cholest-Off; ~2.7g plant sterols (not tracked in columns) |
| psyllium_3dose | 21g | 42 | 0 | 0 | 0 | 0 | 15.0 | 5 | 3 × 7g doses in liquid |

*sol fiber in standard_oat_bowl and oat_bowl_no_whey updated from prior 1.7g to 2.5g to reflect measured beta-glucan content in 40g oats (~1.8g) plus flaxseed mucilage (~0.7g).*

**Output format:**

```
[YYYY-MM-DD] — Day log updated
─────────────────────────────
Calories:       XXXX / ~1600 kcal
Protein:        XX.X / ≥60 g
Sat fat:        X.X / <15 g
Soy protein:    X.X / ≥22 g   ← Portfolio Diet
Soluble fiber:  X.X / ≥20 g   ← Portfolio Diet
Omega-3:        X.X / ≥3 g
Sodium:         XXX / <1500 mg
─────────────────────────────
[One sentence on biggest gap or win; note any HIGH UNCERTAINTY items]
```

---

## Operation: biometrics

The user will report one or more biometric readings. Append each as a separate row to `biometrics.csv` in this project directory, then confirm what was logged.

**CSV schema — file: `biometrics.csv`**

Header: `date,time,metric,value,unit,notes`

- `date` — YYYY-MM-DD; use today's date unless the user specifies otherwise
- `time` — `morning` | `midday` | `evening` | `fasted` | `postprandial` | HH:MM; default to `morning` if unspecified
- `metric` — snake_case; see vocabulary below
- `value` — numeric only
- `unit` — as listed in the vocabulary
- `notes` — context such as "left arm seated", "2h after dinner", "fasted 14h"

**Metric vocabulary:**

| metric | unit | notes |
|---|---|---|
| weight | lbs | |
| bmi | kg/m² | auto-compute when weight is given; see rule below |
| bp_systolic | mmHg | log with bp_diastolic as a separate row |
| bp_diastolic | mmHg | |
| heart_rate | bpm | |
| blood_glucose_fasted | mg/dL | |
| blood_glucose_postprandial | mg/dL | note hours post-meal in `notes` |
| ldl | mg/dL | |
| hdl | mg/dL | |
| triglycerides | mg/dL | |
| total_cholesterol | mg/dL | |

**BMI auto-compute rule:**

When the user reports weight, automatically compute BMI and append it as an additional row.

Formula: `weight_kg / height_m²` — convert lbs to kg by dividing by 2.205. Round to one decimal place.

Height source: read `~/.local/share/diet/config.json` and use the `height_m` value. If the file does not exist or `height_m` is not set, ask the user for their height in feet and inches, convert to metres, write it to `~/.local/share/diet/config.json` as `{"height_m": X.XXX}` (create the directory if needed), then proceed.

**Output:** one confirmation line per row appended:

```
Logged: [metric] [value] [unit] ([date] [time])
```

---

## Operation: fetch

Pull device data from Withings and FitBit for a date and append each metric to `biometrics.csv`.

**If a date is given** (e.g. `/diet fetch 2026-04-25`), use that date. **Otherwise** use yesterday's date.

**Steps:**
1. Determine the target date
2. Call the `get_withings_data(date)` MCP tool — this returns Withings body composition and sleep
3. Call the `get_fitbit_data(date)` MCP tool — this returns FitBit activity, sleep, and weight
4. For each non-null value returned, append one row to `biometrics.csv` with `time = morning`
5. For Withings weight, also compute and append BMI (same formula as biometrics operation)
6. Print a summary of what was logged

**MCP tool result → biometrics.csv mapping:**

| Field | metric | unit | source |
|---|---|---|---|
| weight_kg | weight_kg | kg | Withings |
| weight_lbs | weight | lbs | Withings |
| bmi | bmi | kg/m² | Withings |
| fat_ratio_pct | fat_ratio_pct | % | Withings |
| fat_mass_kg | fat_mass_kg | kg | Withings |
| muscle_mass_kg | muscle_mass_kg | kg | Withings |
| water_mass_kg | water_mass_kg | kg | Withings |
| bone_mass_kg | bone_mass_kg | kg | Withings |
| sleep_minutes (Withings) | sleep_minutes | minutes | Withings |
| steps (Withings) | steps | steps | Withings |
| calories_active | calories_burned_active | kcal | Withings |
| steps (FitBit) | steps | steps | FitBit |
| calories_out | calories_burned | kcal | FitBit |
| sleep_minutes (FitBit) | sleep_minutes | minutes | FitBit |
| weight_lbs (FitBit) | weight | lbs | FitBit |

**Deduplication rule:** if a row with the same `date` + `metric` already exists, skip it (do not append a duplicate).

**Output:**

```
[YYYY-MM-DD] — Device data fetched
────────────────────────────────────
Withings: weight X.X kg (X.X lbs), BMI XX.X, fat X.X%, muscle X.X kg
          sleep Xh Xm, steps XXXX
FitBit:   steps XXXXX, calories XXXX kcal, sleep Xh Xm
────────────────────────────────────
Logged N rows to biometrics.csv
```

---

## Operation: pull

Pull all device data for today (or a specified date) and import into biometrics.csv.

**If a date is given** (e.g. `/diet pull 2026-04-27`), use that date. **Otherwise** use today's date.

**Steps — run all three in sequence:**

1. **Withings + FitBit:** run `uv run server/fetch.py <date>` from the project root
2. **Blood pressure (Omron via Apple Health):** run `uv run server/bp_import.py` from the project root
3. **Glucose (Contour via Google Drive):** run `uv run server/contour_gdrive.py <date>` from the project root

For step 1, parse the fetch.py output and append any new metrics to biometrics.csv (same mapping as the `fetch` operation). For steps 2 and 3, the scripts handle their own import and deduplication directly.

**Output:**

```
[YYYY-MM-DD] — Data pull complete
────────────────────────────────
Withings:  [summary of what was logged or "no new data"]
FitBit:    [summary of what was logged or "no new data"]
BP:        [X new reading(s) or "no new data"]
Glucose:   [X new reading(s) or "no new data"]
────────────────────────────────
Total: X new rows added to biometrics.csv
```

---

## Operation: summary

Read `compliance.csv`, filter for today's date, sum the nutrient columns, and print a gap analysis against the daily targets.

If no rows exist for today, say so and suggest using `/diet log` to start logging.

**Daily targets:** same table as in the `log` operation above.

**Steps:**
1. Run `date +%F` to get today's date
2. Read `compliance.csv`
3. Filter all rows where `date` = today and `meal_context` ≠ `daily_total`
4. Sum each numeric column across those rows
5. Compare sums against targets
6. Print the report

**Output format:**

```
[YYYY-MM-DD] — Diet summary
─────────────────────────────
Foods logged:
  [meal_context]  [food_item] ([amount_g]g) — [kcal] kcal
  ...

Totals vs targets:
  Calories:       XXXX / ~1600 kcal   [under budget / OVER budget]
  Protein:        XX.X / ≥60 g        [met / short Xg]
  Sat fat:        X.X / <15 g         [under limit / OVER by Xg]
  Soy protein:    X.X / ≥22 g         [met / short Xg]  ← Portfolio Diet
  Soluble fiber:  X.X / ≥20 g         [met / short Xg]  ← Portfolio Diet
  Omega-3:        X.X / ≥3 g          [met / short Xg]
  Sodium:         XXX / <1500 mg       [under limit / OVER by Xmg]
─────────────────────────────
[One sentence on biggest gap or win today]
```
