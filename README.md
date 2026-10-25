# Revenue Operations & Sales Pipeline Analytics

An end-to-end portfolio project for Data Analyst and BI Analyst roles using advanced SQL, Python, and Power BI. It analyzes pipeline health, win rates, booked revenue, sales-cycle duration, stage conversion, and lead-source performance.

## Quick start
```bash
python -m pip install -r requirements.txt
python src/generate_data.py
python src/analyze_pipeline.py
pytest -q
```

## Dashboard assets
- **Interactive browser preview:** [dashboard_preview.html](powerbi/dashboard_preview.html)
- **Power BI build specification:** [dashboard_spec.md](powerbi/dashboard_spec.md)
- **Starter DAX measures:** [measures.dax](powerbi/measures.dax)

The HTML preview is a browser-based companion, not a native Power BI report. To create the native report, import `data/raw/opportunities.csv` in Power BI Desktop and follow the build spec and DAX measures. A `.pbix` file is not included.

## Analytics included
- KPI definitions with win-rate denominator made explicit
- SQL CTEs and window functions for monthly trends and rankings
- Python-generated synthetic CRM data and source summaries
- Data contract checks, automated tests, and GitHub Actions CI

## Data disclaimer
All records and values are synthetic and generated for demonstration. Revenue values are opportunity amount proxies, not accounting revenue or actual business performance.
