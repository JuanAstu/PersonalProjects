/*
Here are some querys implemented to transform the data given by the raw database, and to extract partial information
*/


-- As it cames from an excel written in spanish, first we have to translate some values

UPDATE Exports
SET Payment = CASE Payment
WHEN 'Contra entrega' THEN 'Upon delivery'
WHEN 'Anticipado a la entrega' THEN 'Anticipated'
ELSE 'Forward'
END

UPDATE Exports
SET Deal = CASE Deal
WHEN 'Compraventa' THEN 'Purchase'
ELSE 'Trade'
END

UPDATE Exports
SET Quality = CASE Quality
WHEN 'Cámara con condiciones' THEN 'Conditioned Storage Room'
WHEN 'Proteína 10.5%' THEN 'Protein 10.5%'
WHEN 'Otra' THEN 'Other'
WHEN 'Fábrica' THEN 'Industrial'
WHEN 'Art. 12' THEN '12° Art.'
ELSE 'Storage Room'
END

UPDATE Exports
SET Product = CASE Product
WHEN 'SOJA' THEN 'Soybean'
WHEN 'MAIZ' THEN 'Corn'
ELSE 'Wheat'
END


-- Currency types and frequency

SELECT Currency, COUNT(Currency) as Counts
FROM Exports
GROUP BY Currency
ORDER BY Counts desc

-- Payment methods availables

SELECT Payment, COUNT(Payment) as Payment_Count
FROM Exports
GROUP BY Payment
ORDER BY Payment_Count desc

-- How is the frequency of each Payment method? Grouped by Crop

SELECT Product, Payment, COUNT(Payment) as Payment_Count
FROM Exports
WHERE Product is not NULL
GROUP BY Product, Payment
ORDER BY Product, Payment_Count desc

-- Monthly average price and standard deviation

SELECT Product, month(Operation_date) as Export_month, AVG(Price) as Average_price, STDEV(Price) as Desvio
FROM Exports
GROUP BY month(Operation_date), Product
ORDER BY Product, Export_month

-- Soybean price evolution

SELECT Product, MONTH(Operation_date) as Op_Month, DAY(Operation_date) as Operation_day, AVG(Price) as Avg_Price
FROM Exports
WHERE Product like 'Soybean'
GROUP BY DAY(Operation_date), MONTH(Operation_date)
ORDER BY Op_Month, Operation_day

--Most important provinces

SELECT Product, Procedence_province, SUM(Quantity) as Total_Qt_Exported
FROM Exports
GROUP BY Product, Procedence_province
HAVING SUM(Quantity) > 1000000
ORDER BY Product, Total_Qt_Exported desc