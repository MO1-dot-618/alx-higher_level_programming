-- genres of Dexter
SELECT s.title
FROM tv_genres AS g
INNER JOIN tv_show_genres AS t
ON t.genre_id = g.id
INNER JOIN tv_shows AS s
ON s.id = t.show_id
WHERE g.name = 'Comedy'
ORDER BY s.title;
