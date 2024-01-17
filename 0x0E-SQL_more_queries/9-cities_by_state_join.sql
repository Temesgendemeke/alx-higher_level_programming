-- list all cities 
USE hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities 
INNER JOIN states ON cities.id=states.state_id ORDER BY cities.id ASC;