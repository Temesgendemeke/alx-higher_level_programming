-- list all cities 
SELECT cities.id, cities.name, state_id FROM cities 
INNER JOIN states ON cities.id = state.id;