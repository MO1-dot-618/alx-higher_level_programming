-- genres of Dexter
SELECT s.title AS title, g.name AS name
FROM tv_genres AS g
INNER JOIN tv_show_genres AS t
ON t.genre_id = g.id
RIGHT JOIN tv_shows AS s
ON s.id = t.show_id
ORDER BY title, name;
