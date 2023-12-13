-- number of shows per genre
SELECT g.name AS genre, COUNT(g.name) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS t
ON t.genre_id = g.id
GROUP BY g.name
ORDER BY number_of_shows DESC;
