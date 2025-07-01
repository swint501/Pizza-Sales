-- Analyze Top Selling Pizzas
SELECT TOP 10 pizza_name as 'Pizza Name', SUM(quantity) AS 'Total Sold'
FROM CleanedPizzaSalesData
GROUP BY pizza_name
ORDER BY 'Total Sold' DESC;

