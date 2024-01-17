-- displays the number of shows linked to each.
SELECT tv_show_genres.title AS genre, COUNT(*) AS number_of_shows FROM tv_genres
INNER JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
GROUP BY tv_shows.show_id 
ORDER BY number_of_shows DESC;