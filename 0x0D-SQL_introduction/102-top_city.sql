--- top cites temprature during july and augest
SELECT city, TOP 3 AVG(value) AS avg_temp FROM temperatures WHERE month BETWEEN 6 and 9 GROUP BY city ORDER BY avg_temp DESC;