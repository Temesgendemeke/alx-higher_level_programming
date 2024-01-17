-- lists all the cities of california
USE hbtn_0d_usa;
SELECT id, cities FROM states WHERE NAME='California' ORDER BY cities.id ASC;
