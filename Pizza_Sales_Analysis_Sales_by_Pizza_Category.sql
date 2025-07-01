-- Analyze Sales by Pizza Category
SELECT pizza_category as 'Pizza Category', SUM(quantity) AS 'Total Sold'
FROM CleanedPizzaSalesData
GROUP BY pizza_category;
