-- lists geners that are not linked to the show
SELECT tv_genres.name FROM tv_genres
WHERE tv_genres.name NOT IN (SELECT tv_genres.name FROM tv_shows
JOIN tv_show_genres On tv_show_genres.show_id = tv_genres.id
JOIN tv_genres on tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = "Dexter")


