# /diet — daily quick reference

## Daily workflow

| When | Command | What to say |
|---|---|---|
| Morning | `/diet log` | Smoothie, oat bowl, morning supplements |
| Midday | `/diet log` | Snacks, tofu, ta'ameya, anything eaten |
| Evening | `/diet log` | Dinner, final supplements |
| Anytime | `/diet summary` | Check where you stand without logging |
| Morning (device sync) | `/diet fetch` | Pull yesterday's Withings + FitBit data |
| Full sync | `/diet pull` | Withings + FitBit + BP + glucose for today |

`soy_milk_in_coffee` is auto-logged on your first call of the day — you never need to mention it.

---

## Operations

### `/diet log`
Describe what you ate. Grams are best; vague amounts work too.

> *"113g baked salmon, cup of roasted broccoli, slice of rugbrød, fish oil and plant sterols"*
> *"3 cup soymilk smoothie with banana and 3x psyllium"*
> *"a few bites of salmon, did all the supplements"*

Claude reads today's existing rows, skips duplicates, updates the running total, and prints a gap analysis.

### `/diet biometrics`
Report weight, BP, glucose, or lipids.

> *"weight 194 lbs"* → logs weight + auto-computes BMI
> *"BP 118/74"* → logs systolic + diastolic
> *"fasted glucose 91"* → logs blood_glucose_fasted
> *"postprandial glucose 112, 2 hours after dinner"*

### `/diet summary`
Prints today's full gap analysis from existing rows. No new logging.

### `/diet fetch [YYYY-MM-DD]`
Pulls Withings + FitBit for that date (default: yesterday) into biometrics.csv.

### `/diet pull [YYYY-MM-DD]`
Full device sync: Withings + FitBit + Omron BP + Contour glucose. Requires device connections active.

---

## Daily targets at a glance

| Metric | Target |
|---|---|
| Calories | ~1600 kcal |
| Protein | ≥60 g |
| Sat fat | <15 g |
| Soy protein | ≥22 g ← Portfolio Diet |
| Soluble fiber | ≥20 g ← Portfolio Diet |
| Omega-3 | ≥3 g (prefer EPA+DHA from fish) |
| Sodium | <1500 mg |

---

## Named recipes (log these by name)

| Name | Key contents |
|---|---|
| `standard_oat_bowl` | 40g oats + 10g flax + 20g whey + 120ml soymilk |
| `oat_bowl_no_whey` | 40g oats + 10g flax + 120ml soymilk |
| `soymilk_smoothie_3cup_base` | 720ml soymilk + 10g flax + 21g psyllium (add fruit separately) |
| `edamame_tameya_8pc` | 8 baked edamame patties, no oil |
| `psyllium_3dose` | 3 × 7g psyllium in liquid |
| `fish_oil_standard` | 3 softgels (0.9g EPA+DHA) |
| `plant_sterols_standard` | 6 Cholest-Off caps (~2.7g sterols) |

---

## Watch-outs

**Sodium spikes** — jarred herring, smoked salmon lox, and any pickled/cured fish have HIGH UNCERTAINTY sodium (700–1500 mg/100g). On days with these items, avoid other high-sodium foods and check the running total.

**Omega-3** — fish oil capsules give 0.9g EPA+DHA. You need fish (salmon or mackerel) for the remaining ~2g. ALA from flax/edamame/tofu counts but converts poorly.

**Brazil nuts** — 3/day max (selenium ceiling ~400 mcg/day).
