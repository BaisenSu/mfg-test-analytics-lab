
# mfg-test-analytics-lab

A hands-on lab to practice a real manufacturing test analytics workflow end to end:
- Ingest **FCT/EOL** and **station event** logs
- Query with **KQL** (Azure Data Explorer / Log Analytics)
- Track core KPIs (FPY, RTY, Pareto, utilization, MTBF/MTTR, WIP aging, limit-change impact)
- Use a **GitHub** workflow for basic schema checks

## Folder layout
```
mfg-test-analytics-lab/
├── data/                  # mock CSV datasets ready to ingest
├── kql/                   # KQL query files grouped by topic
├── scripts/               # helper scripts for local validation and CSV checks
├── notebooks/             # optional exploration (empty)
├── .github/workflows/     # CI that validates CSV schema
├── .gitignore
├── LICENSE
└── README.md
```

## Data
This repo includes small, realistic mock datasets:
- `Fact_TestResults.csv` per-measurement results with limits and pass/fail
- `Fact_StationEvents.csv` run/idle/fault/maintenance events with durations
- `Fact_Throughput.csv` hourly unique units per gate/station
- `Dim_Defect.csv` defect taxonomy (owner, avg_cost_usd)
- `Dim_LimitChange.csv` a couple of limit widenings

Time window: ~30 days ending 2025-10-14.

## Quick start
1. **Create the repo locally**
```
git init
git checkout -b main
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r scripts/requirements.txt
git add .
git commit -m "init: project scaffold + mock data + KQL + CI"
```

2. **Push to remote**
```
git remote add origin <your-remote-url>
git push -u origin main
```

3. **Make a feature branch (practice PR)**
```
git checkout -b feat/kql-fpy-dashboard
# edit kql/fpy_by_day.kql, run scripts/check_schema.py
git add .
git commit -m "feat(kql): FPY by day + station utilization query"
git push -u origin feat/kql-fpy-dashboard
# open a Pull Request on the remote
```

4. **Ingest to ADX/Log Analytics (manual)**
- Create tables named like the CSV files and ingest `/data/*.csv`
- Run queries from `/kql/*.kql` to build metrics and charts

5. **CI checks**
- On every push/PR, GitHub Actions runs lightweight schema checks
- You can extend CI to publish artifacts, data profiles, or lint KQL

## KPIs included
- FPY/RTY, Top-N failures (by cost and count), Throughput, Utilization, MTBF/MTTR, WIP aging, Limit-change impact, Vendor/Lot FPY.

## Notes
- Mock data includes a deliberately **bad lot** and **limit changes** to verify analytics catch them.
- Definitions matter. Adjust KQL to match your factory’s KPI definitions.
