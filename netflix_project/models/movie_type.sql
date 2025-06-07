-- What type of movies are most popular on Netflix?
SELECT "listed_in", COUNT(*) AS total
FROM main.netflix_table
WHERE "type" = 'Movie'
GROUP BY "listed_in"
LIMIT 10