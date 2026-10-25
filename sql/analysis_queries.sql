-- 1. Executive KPI snapshot
SELECT COUNT(*) AS opportunities,
       SUM(is_closed) AS closed_opportunities,
       SUM(is_won) AS won_opportunities,
       ROUND(100.0 * SUM(is_won) / NULLIF(SUM(is_closed), 0), 2) AS win_rate_pct,
       SUM(CASE WHEN is_won = 1 THEN amount ELSE 0 END) AS booked_revenue_proxy,
       SUM(CASE WHEN is_closed = 0 THEN amount ELSE 0 END) AS open_pipeline_value
FROM opportunities;

-- 2. Monthly booked revenue and prior-month comparison (window function)
WITH monthly AS (
  SELECT DATE_TRUNC('month', close_date)::date AS month,
         SUM(amount) AS booked_revenue
  FROM opportunities
  WHERE is_won = 1 AND close_date IS NOT NULL
  GROUP BY 1
)
SELECT month, booked_revenue,
       LAG(booked_revenue) OVER (ORDER BY month) AS prior_month_revenue,
       ROUND(100.0 * (booked_revenue - LAG(booked_revenue) OVER (ORDER BY month))
         / NULLIF(LAG(booked_revenue) OVER (ORDER BY month), 0), 2) AS mom_change_pct
FROM monthly ORDER BY month;

-- 3. Stage funnel
SELECT stage, COUNT(*) AS opportunity_count,
       SUM(amount) AS pipeline_value,
       ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS share_of_opportunities_pct
FROM opportunities GROUP BY stage ORDER BY opportunity_count DESC;

-- 4. Lead source performance
SELECT lead_source, COUNT(*) AS leads,
       SUM(is_won) AS wins,
       ROUND(100.0 * SUM(is_won) / NULLIF(COUNT(*), 0), 2) AS win_rate_pct,
       SUM(CASE WHEN is_won = 1 THEN amount ELSE 0 END) AS booked_revenue
FROM opportunities GROUP BY lead_source ORDER BY booked_revenue DESC;

-- 5. Rep leaderboard with dense ranking
WITH rep AS (
  SELECT sales_rep, SUM(CASE WHEN is_won = 1 THEN amount ELSE 0 END) AS booked_revenue,
         SUM(is_won) AS wins
  FROM opportunities GROUP BY sales_rep
)
SELECT *, DENSE_RANK() OVER (ORDER BY booked_revenue DESC) AS revenue_rank
FROM rep ORDER BY revenue_rank;

-- 6. Data contract checks: IDs, amounts, impossible flags
SELECT
  COUNT(*) FILTER (WHERE opportunity_id IS NULL) AS null_ids,
  COUNT(*) - COUNT(DISTINCT opportunity_id) AS duplicate_ids,
  COUNT(*) FILTER (WHERE amount < 0) AS negative_amounts,
  COUNT(*) FILTER (WHERE is_won = 1 AND is_closed = 0) AS won_but_open
FROM opportunities;
