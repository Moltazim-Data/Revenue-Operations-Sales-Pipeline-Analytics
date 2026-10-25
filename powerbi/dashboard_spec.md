# Power BI dashboard specification

## Model
Import `data/raw/opportunities.csv`. Create a dedicated Date table and mark it as the date table. Relate Date[Date] to opportunities[created_date]; use an inactive relationship to close_date when building closed-date measures. Keep the opportunity table at one row per opportunity.

## Page 1 — Executive Overview
- KPI cards: Booked Revenue Proxy, Open Pipeline Value, Win Rate %, Won Opportunities.
- Line chart: monthly booked revenue by close date.
- Stacked column: stage count by account segment.
- Slicers: date, segment, lead source, sales rep.

## Page 2 — Pipeline Health
- Funnel/bar: opportunity count and value by stage.
- Matrix: stage by segment.
- Table: open opportunities and amount; add age buckets based on created date.

## Page 3 — Sales Effectiveness
- Ranked bar: booked revenue by sales rep.
- Scatter: opportunity count vs win rate by lead source.
- Distribution: sales-cycle days for won deals.

Use consistent currency formatting, meaningful titles, accessible contrast, and tooltips with denominator definitions. The DAX file contains starter measures; validate date relationships and measure behavior in Power BI Desktop. No PBIX is included.
