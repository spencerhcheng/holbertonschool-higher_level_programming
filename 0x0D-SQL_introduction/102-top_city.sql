-- Displays the avg temperature by city ordered by temperature
SELECT temperatures.city, AVG(temperatures.value) as avg_temp
FROM temperatures
WHERE temperatures.month IN (7, 8)
GROUP BY temperatures.city
ORDER BY avg_temp DESC
LIMIT 3
