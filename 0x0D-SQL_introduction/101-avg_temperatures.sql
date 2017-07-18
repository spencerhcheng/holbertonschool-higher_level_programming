-- Displays the avg temperature by city ordered by temperature
SELECT temperatures.city, AVG(temperatures.value) as avg_temp
FROM temperatures
GROUP BY temperatures.city
ORDER BY avg_temp DESC;
