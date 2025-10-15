
import sys, pandas as pd, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

# Expected columns per CSV
SCHEMA = {
    "Fact_TestResults.csv": [
        "timestamp","unit_id","product","sku","revision","station_id",
        "step","measurement","value","lo","hi","pass","error_code",
        "duration_ms","firmware_ver","test_seq_ver","lot_id","vendor_id"
    ],
    "Fact_StationEvents.csv": [
        "timestamp","station_id","event_type","reason_code","severity","duration_ms"
    ],
    "Fact_Throughput.csv": [
        "hour","station_id","gate","units_out","units_in"
    ],
    "Dim_Defect.csv": [
        "error_code","defect_desc","owner","avg_cost_usd"
    ],
    "Dim_LimitChange.csv": [
        "step","measurement","effective_from","old_lo","old_hi","new_lo","new_hi","owner"
    ],
}

def check_file(path, expected_cols):
    df = pd.read_csv(path)
    missing = [c for c in expected_cols if c not in df.columns]
    extra = [c for c in df.columns if c not in expected_cols]
    return {"file": path.name, "rows": len(df), "missing": missing, "extra": extra}

def main():
    results = []
    failures = 0
    for fn, cols in SCHEMA.items():
        p = DATA / fn
        if not p.exists():
            results.append({"file": fn, "error": "missing file"})
            failures += 1
            continue
        res = check_file(p, cols)
        if res["missing"] or res["extra"]:
            failures += 1
        results.append(res)
    print(json.dumps(results, indent=2))
    sys.exit(1 if failures else 0)

if __name__ == "__main__":
    main()
