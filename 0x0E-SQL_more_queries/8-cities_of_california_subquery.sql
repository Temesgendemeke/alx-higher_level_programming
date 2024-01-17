-- lists all the cities of california
SELECT id, name FROM WHERE state_id = (SELECT id FROM states WHERE name='California') ORDER BY cities.id ASC;
