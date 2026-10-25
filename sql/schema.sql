-- PostgreSQL-compatible analytical table for the generated CSV.
CREATE TABLE opportunities (
    opportunity_id VARCHAR(16) PRIMARY KEY,
    created_date DATE NOT NULL,
    close_date DATE,
    account_segment VARCHAR(32),
    lead_source VARCHAR(32),
    sales_rep VARCHAR(64),
    stage VARCHAR(32) NOT NULL,
    amount NUMERIC(14,2) NOT NULL CHECK (amount >= 0),
    is_closed SMALLINT NOT NULL CHECK (is_closed IN (0,1)),
    is_won SMALLINT NOT NULL CHECK (is_won IN (0,1)),
    sales_cycle_days INTEGER
);
