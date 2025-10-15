# Mock Manufacturing Test Logs (FCT/EOL + Station Events)

Time window: 2025-09-14T12:00:00 to 2025-10-14T12:00:00 (~30 days)

Files
- Fact_TestResults.csv — per-measurement results with limits and pass/fail
- Fact_StationEvents.csv — run/idle/fault/maintenance events with durations
- Fact_Throughput.csv — hourly unique units per station and gate
- Dim_Defect.csv — defect taxonomy with owner and avg_cost_usd
- Dim_LimitChange.csv — a couple of limit widening events

Highlights
- Contains a deliberately **bad lot** to create real signals
- Includes limit changes on `adc_offset_uV` and `boot_time_ms` to test yield-vs-limit analysis
- Measurements include power rails, ADC, comms, and EOL functional items
- Enough volume to do FPY/RTY, Pareto, SPC, station utilization, MTBF/MTTR

Schema (Fact_TestResults)
- timestamp (ISO8601), unit_id, product, sku, revision, station_id
- step, measurement, value, lo, hi, pass (bool), error_code, duration_ms
- firmware_ver, test_seq_ver, lot_id, vendor_id

Schema (Fact_StationEvents)
- timestamp (ISO8601), station_id, event_type [run|idle|fault|maintenance], reason_code, severity, duration_ms

Schema (Fact_Throughput)
- hour, station_id, gate, units_out, units_in

Quick-start (ADX/KQL)
- .ingest inline or upload these CSVs into tables named as the files
- Try the KQL snippets from our previous chat to compute FPY/RTY, Pareto, utilization, MTBF/MTTR, WIP aging, and limit-change impact
