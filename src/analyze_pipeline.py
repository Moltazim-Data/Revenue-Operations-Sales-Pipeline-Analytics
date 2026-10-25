"""Create portfolio KPI outputs from generated CRM data."""
from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "raw" / "opportunities.csv"
OUT = ROOT / "data" / "processed"

def main() -> None:
    df = pd.read_csv(SOURCE)
    closed = df[df["is_closed"] == 1]
    won = df[df["is_won"] == 1]
    kpis = {
        "opportunities": int(len(df)),
        "closed_opportunities": int(len(closed)),
        "won_opportunities": int(len(won)),
        "open_opportunities": int((df["is_closed"] == 0).sum()),
        "win_rate_pct": round(100 * len(won) / len(closed), 2) if len(closed) else 0,
        "booked_revenue_proxy": round(float(won["amount"].sum()), 2),
        "open_pipeline_value": round(float(df.loc[df["is_closed"] == 0, "amount"].sum()), 2),
        "average_won_deal": round(float(won["amount"].mean()), 2) if len(won) else 0,
        "median_sales_cycle_days": float(won["sales_cycle_days"].median()) if len(won) else None,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "kpi_summary.json").write_text(json.dumps(kpis, indent=2))
    by_source = df.groupby("lead_source").agg(
        opportunities=("opportunity_id", "count"),
        won=("is_won", "sum"),
        total_amount=("amount", "sum"),
    ).reset_index()
    by_source["win_rate_pct"] = (100 * by_source["won"] / by_source["opportunities"]).round(2)
    by_source.to_csv(OUT / "source_performance.csv", index=False)
    print(json.dumps(kpis, indent=2))

if __name__ == "__main__":
    main()
