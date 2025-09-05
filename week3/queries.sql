
-- 1. Highest closing price overall
SELECT name, MAX(close) AS max_close
FROM prices p
JOIN companies c ON c.ticker = p.ticker;

-- 2. Average closing price by ticker
SELECT ticker, AVG(close) AS avg_price
FROM prices
GROUP BY ticker
ORDER BY avg_price DESC;

-- 3. Total trading volume per ticker
SELECT ticker, SUM(volume) AS total_volume
FROM prices
GROUP BY ticker
ORDER BY total_volume DESC;

-- 4. Daily average close across all tickers
SELECT date, AVG(close) AS avg_close
FROM prices
GROUP BY date
ORDER BY date ASC;

-- 5. Join companies + prices: show sector performance for a given day
SELECT c.sector, c.name, p.date, p.close
FROM companies c
JOIN prices p ON c.ticker = p.ticker
WHERE p.date = '2025-09-01'
ORDER BY p.close DESC;

-- 6. Sector-level average close (all time) (only one ticker per sector at this point, more to be added)
SELECT c.sector, AVG(p.close) AS sector_avg_close
FROM companies c
JOIN prices p ON c.ticker = p.ticker
GROUP BY c.sector
ORDER BY sector_avg_close DESC;
