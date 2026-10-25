"""Generate reproducible synthetic CRM opportunity data."""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw" / "opportunities.csv"

def main(n: int = 5000) -> None:
    rng = np.random.default_rng(42)
    start = pd.Timestamp("2023-01-01")
    created = start + pd.to_timedelta(rng.integers(0, 1000, n), unit="D")
    stage = rng.choice(["Prospecting", "Qualification", "Proposal", "Negotiation", "Closed Won", "Closed Lost"], n,
                       p=[.14, .16, .15, .12, .26, .17])
    won = stage == "Closed Won"
    lost = stage == "Closed Lost"
    closed = won | lost
    amount = np.round(np.clip(rng.lognormal(10.2, .8, n), 1000, 250000), 2)
    cycle = rng.integers(7, 121, n)
    close_date = pd.Series(pd.NaT, index=np.arange(n), dtype="datetime64[ns]")
    close_date.loc[closed] = created[closed] + pd.to_timedelta(cycle[closed], unit="D")
    df = pd.DataFrame({
        "opportunity_id": [f"OPP-{i:05d}" for i in range(1, n + 1)],
        "created_date": created.date.astype(str),
        "close_date": close_date.dt.strftime("%Y-%m-%d"),
        "account_segment": rng.choice(["SMB", "Mid-Market", "Enterprise"], n, p=[.48,.34,.18]),
        "lead_source": rng.choice(["Inbound", "Outbound", "Partner", "Paid Search", "Referral"], n),
        "sales_rep": rng.choice(["Alex Morgan", "Sam Lee", "Jordan Patel", "Taylor Kim", "Casey Brown", "Riley Chen"], n),
        "stage": stage,
        "amount": amount,
        "is_closed": closed.astype(int),
        "is_won": won.astype(int),
        "sales_cycle_days": np.where(closed, cycle, np.nan),
    })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False)
    print(f"Wrote {len(df):,} synthetic opportunities to {OUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
