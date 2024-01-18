use hbtn_0d_tvshows;
SELECT tv_genres.name from tv_shows  inner join tv_show_genres on tv_shows.id = tv_show_genres.show_id 
inner join tv_genres on tv_genres.id = tv_show_genres.genre_id where tv_shows.title = "Dexter"