-- Displays the max temperature of each state
SELECT temperatures.state, temperatures.value AS max_temp
FROM temperatures
WHERE (temperatures.state, temperatures.value)
IN (
	SELECT temperatures.state, MAX(temperatures.value)
	FROM temperatures 
	GROUP BY temperatures.state
)
