-- genres of Dexter
SELECT g.name AS name
FROM tv_genres AS g
INNER JOIN tv_show_genres AS t
ON t.genre_id = g.id
INNER JOIN tv_shows AS s
ON s.id = t.show_id
WHERE s.title = 'Dexter'
ORDER BY name;
