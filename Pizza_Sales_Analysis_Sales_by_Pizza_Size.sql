-- Analyze Sales by Pizza Size
SELECT pizza_size AS 'Pizza Size', SUM(quantity) AS 'Total Sold'
FROM CleanedPizzaSalesData
GROUP BY pizza_size
ORDER BY 'Total Sold' DESC
