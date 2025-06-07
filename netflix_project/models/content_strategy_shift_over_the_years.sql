-- What type of movies are most popular on Netflix?
SELECT type, year_added, COUNT(*) AS count
FROM main.netflix_table
WHERE year_added IS NOT NULL
GROUP BY type, year_added