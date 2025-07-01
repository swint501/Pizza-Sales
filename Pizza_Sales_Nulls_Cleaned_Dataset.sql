-- Count nulls in columns
SELECT
    SUM(CASE WHEN order_date IS NULL THEN 1 ELSE 0 END) AS 'Missing Order Date',
    SUM(CASE WHEN order_time IS NULL THEN 1 ELSE 0 END) AS 'Missing Order Time',
    SUM(CASE WHEN quantity IS NULL THEN 1 ELSE 0 END) AS 'Missing Quantity',
    SUM(CASE WHEN pizza_size IS NULL THEN 1 ELSE 0 END) AS 'Missing Pizza Size',
    SUM(CASE WHEN total_price IS NULL THEN 1 ELSE 0 END) AS 'Missing Total Price',
    SUM(CASE WHEN pizza_category IS NULL THEN 1 ELSE 0 END) AS 'Missing Pizza Category',
    SUM(CASE WHEN pizza_name IS NULL THEN 1 ELSE 0 END) AS 'Missing Pizza Name'
FROM CleanedPizzaSalesData;
