--- top cites temprature during july and augest
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month IN (6,8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;