-- lists all the cities of california
SELECT id, name FROM WHERE id = (SELECT id FROM states WHERE name='California');
