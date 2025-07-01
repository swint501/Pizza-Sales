-- Summarize Quantity and Total Sales for Analysis
SELECT 
    FORMAT(MIN(order_date), 'MMMM dd, yyyy') AS 'First Order',
    FORMAT(MAX(order_date), 'MMMM dd, yyyy') AS 'Last Order',
    COUNT(*) AS 'Total Orders',
    SUM(quantity) AS 'Total Pizzas Sold',
    FORMAT(SUM(total_price), 'C', 'en-US') AS 'Total Sales'
FROM CleanedPizzaSalesData;
