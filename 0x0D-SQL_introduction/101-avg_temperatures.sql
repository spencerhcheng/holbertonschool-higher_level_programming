-- Displays the average temperatures by city ordered by temperature (descending)
SELECT city, AVG(value) as avg_temp
FROM temperatures
ORDER BY avg_temp DESC;
