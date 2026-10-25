# Data dictionary

| Column | Description |
|---|---|
| opportunity_id | Unique synthetic CRM opportunity identifier |
| created_date | Date opportunity entered the pipeline |
| close_date | Close date for closed opportunities; blank for open deals |
| account_segment | SMB, Mid-Market, or Enterprise |
| lead_source | Acquisition source category |
| sales_rep | Synthetic sales representative name |
| stage | Current stage, including Closed Won and Closed Lost |
| amount | Synthetic opportunity amount in currency units |
| is_closed | 1 if closed, otherwise 0 |
| is_won | 1 if won, otherwise 0 |
| sales_cycle_days | Elapsed days for closed opportunities; missing for open deals |

The dataset is generated deterministically with seed 42 by `src/generate_data.py`.
