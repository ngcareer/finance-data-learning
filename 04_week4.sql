-- Average closing price per ticker
SELECT
  Ticker,
  ROUND(AVG(Close), 2) AS avg_close_raw,           -- numeric version for calculations
  printf('%.2f', AVG(Close)) AS avg_close_formatted  -- formatted as string
FROM prices
GROUP BY Ticker;

-- Max volume per ticker
SELECT
  Ticker,
  MAX(Volume) AS max_volume_raw,
  printf('%,d', MAX(Volume)) AS max_volume_formatted
FROM prices
GROUP BY Ticker;

-- Percent change of closing price
SELECT date, ticker,
  ROUND(100.0 * (Close / Prev_Close - 1), 2) AS Daily_Pct_Change_raw, -- percent change for calculations
  printf('%.2f%%', 100.0 * (Close / Prev_Close - 1)) AS Daily_Pct_Change_fmt --percent change for printed results
FROM (
  SELECT
    Date,
    Ticker,
    Close,
    LAG(Close) OVER (PARTITION BY Ticker ORDER BY Date) AS Prev_Close
  FROM prices
)
WHERE Prev_Close IS NOT NULL
ORDER BY Ticker, Date;