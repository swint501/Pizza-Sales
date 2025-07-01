-- 1. Use the database Pizza_DA in Azure Data Studio
USE Pizza_DA;
GO

-- 2. Create the cleaned table.
IF NOT EXISTS (
    SELECT * FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME = 'CleanedPizzaSalesData'
)
BEGIN
    CREATE TABLE CleanedPizzaSalesData (
        order_date DATE,
        order_time TIME,
        quantity INT,
        pizza_size VARCHAR(50),
        total_price DECIMAL(10, 2),
        pizza_category VARCHAR(100),
        pizza_name VARCHAR(100)
    );
END;
GO

-- 3. Insert only the necessary columns from PSD (old table) into the new cleaned table
INSERT INTO CleanedPizzaSalesData (
    order_date, 
    order_time, 
    quantity, 
    pizza_size, 
    total_price, 
    pizza_category, 
    pizza_name
)
SELECT
    order_date,
    order_time,
    quantity,
    pizza_size,
    total_price,
    pizza_category,
    pizza_name
FROM
    PSD;
GO

-- 4. Verify the data is correct
SELECT * FROM CleanedPizzaSalesData;
