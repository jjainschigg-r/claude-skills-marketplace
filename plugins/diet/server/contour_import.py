# /// script
# dependencies = []
# ///
"""
Import Contour Next One CSV exports into biometrics.csv.

Usage:
    uv run server/contour_import.py <path-to-contour-export.csv>

The Contour Diabetes app exports a tab-delimited file with columns:
    #  Date and Time  BGValue[mg/dL]  Meal Marker  Data Source  Notes  Activity  Meal[g]  Medication  Location

Only rows with Data Source == "Meter" are imported (skips manual entries).
Existing rows in biometrics.csv with the same date+time+metric are skipped.
"""

import csv
import sys
from datetime import datetime
from pathlib import Path

BIOMETRICS_FILE = Path(__file__).parent.parent / "biometrics.csv"

MEAL_MARKER_MAP = {
    "fasting":      ("blood_glucose_fasted",        "fasted"),
    "before meal":  ("blood_glucose_fasted",        "preprandial"),
    "after meal":   ("blood_glucose_postprandial",  "postprandial"),
    "no marker":    ("blood_glucose",               ""),
    "":             ("blood_glucose",               ""),
}


def _parse_row(row: dict) -> dict | None:
    source = row.get("Data Source", "").strip()
    if source.lower() != "meter":
        return None

    raw_dt = row.get("Date and Time", "").strip().replace(" ", " ")
    try:
        dt = datetime.strptime(raw_dt, "%m/%d/%Y %I:%M:%S %p")
    except ValueError:
        try:
            dt = datetime.strptime(raw_dt, "%m/%d/%Y %H:%M:%S")
        except ValueError:
            return None

    bg_raw = row.get("BGValue[mg/dL]", "").strip()
    if not bg_raw:
        return None
    try:
        bg = float(bg_raw)
    except ValueError:
        return None

    marker = row.get("Meal Marker", "").strip().lower()
    metric, time_label = MEAL_MARKER_MAP.get(marker, ("blood_glucose", ""))
    if not time_label:
        h = dt.hour
        time_label = "morning" if h < 12 else "midday" if h < 17 else "evening"

    notes_parts = [f"Contour Next One"]
    if row.get("Meal Marker", "").strip():
        notes_parts.append(row["Meal Marker"].strip())
    if row.get("Notes", "").strip():
        notes_parts.append(row["Notes"].strip())
    if row.get("Medication", "").strip():
        notes_parts.append(f"med: {row['Medication'].strip()}")

    return {
        "date": dt.strftime("%Y-%m-%d"),
        "time": dt.strftime("%H:%M"),
        "metric": metric,
        "value": int(bg) if bg == int(bg) else bg,
        "unit": "mg/dL",
        "notes": "; ".join(notes_parts),
    }


def _load_existing() -> set[tuple]:
    existing = set()
    try:
        with BIOMETRICS_FILE.open() as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing.add((row["date"], row["time"], row["metric"]))
    except FileNotFoundError:
        pass
    return existing


def _import_parsed(parsed: list[dict]):
    existing = _load_existing()
    new_rows = [
        r for r in parsed
        if (r["date"], r["time"], r["metric"]) not in existing
    ]

    if not new_rows:
        print(f"No new rows to import ({len(parsed)} parsed, all already present).")
        return

    with BIOMETRICS_FILE.open("a") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["date", "time", "metric", "value", "unit", "notes"],
            lineterminator="\n",
        )
        for row in new_rows:
            writer.writerow(row)

    print(f"Imported {len(new_rows)} new row(s) from {len(parsed)} parsed:")
    for r in new_rows:
        print(f"  {r['date']} {r['time']}  {r['metric']:35s}  {r['value']} mg/dL  ({r['notes']})")


def main(csv_path: str):
    path = Path(csv_path)
    if not path.exists():
        print(f"ERROR: file not found: {csv_path}")
        raise SystemExit(1)

    with path.open(encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=",")
        parsed = [r for r in (_parse_row(row) for row in reader) if r is not None]

    _import_parsed(parsed)


def main_from_text(content: str):
    import io
    reader = csv.DictReader(io.StringIO(content), delimiter=",")
    parsed = [r for r in (_parse_row(row) for row in reader) if r is not None]
    _import_parsed(parsed)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: uv run server/contour_import.py <contour-export.csv>")
        raise SystemExit(1)
    main(sys.argv[1])
