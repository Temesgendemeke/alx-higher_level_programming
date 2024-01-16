-- list number f records with the same score
SELECT score, COUNT(*) FROM second_table 
GROUP BY score 
ORDER BY score DESC;