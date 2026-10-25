from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def test_generated_dataset_contract():
    path = ROOT / "data" / "raw" / "opportunities.csv"
    if not path.exists():
        import subprocess, sys
        subprocess.run([sys.executable, str(ROOT / "src" / "generate_data.py")], check=True)
    df = pd.read_csv(path)
    assert len(df) == 5000
    assert df["opportunity_id"].is_unique
    assert (df["amount"] >= 0).all()
    assert set(df["is_won"].unique()).issubset({0, 1})
    assert not ((df["is_won"] == 1) & (df["is_closed"] == 0)).any()

def test_closed_flag_consistency():
    path = ROOT / "data" / "raw" / "opportunities.csv"
    if not path.exists():
        import subprocess, sys
        subprocess.run([sys.executable, str(ROOT / "src" / "generate_data.py")], check=True)
    df = pd.read_csv(path)
    assert (df.loc[df.stage.isin(["Closed Won", "Closed Lost"]), "is_closed"] == 1).all()
