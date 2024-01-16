-- list number f records with the same score
SELECT score, COUNT(score) AS n FROM second_table 
GROUP BY score 
ORDER BY score DESC;