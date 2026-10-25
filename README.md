# Revenue Operations & Sales Pipeline Analytics

An end-to-end portfolio project for Data Analyst and BI Analyst roles using advanced SQL, Python, and Power BI. It examines pipeline health, win rates, booked revenue, sales-cycle duration, stage conversion, and lead-source performance.

## Project goals
- Create a reproducible synthetic CRM opportunity dataset.
- Analyze pipeline and sales KPIs with Python and SQL.
- Design a three-page Power BI dashboard using documented DAX measures.
- Validate data contracts and run automated tests with GitHub Actions.

## Data disclaimer
All data is synthetic and generated for demonstration. Revenue and performance metrics are not real company results.

## Quick start
```bash
python -m pip install -r requirements.txt
python src/generate_data.py
python src/analyze_pipeline.py
pytest -q
```

## Dashboard plan
1. Executive overview: booked revenue, open pipeline, win rate, monthly trend.
2. Pipeline diagnostics: stage distribution, funnel conversion, aging.
3. Sales effectiveness: lead-source performance, rep leaderboard, sales-cycle analysis.

The `powerbi/` folder contains DAX measures and dashboard implementation guidance. A `.pbix` file is not included; build the report in Power BI Desktop using the included CSV and instructions.
