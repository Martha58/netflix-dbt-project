-- What countries produce the most content available on Netflix? (Top 10)
SELECT country, COUNT(DISTINCT title) AS content_count
FROM main.netflix_table
WHERE country IS NOT NULL
GROUP BY country
ORDER BY content_count DESC
LIMIT 10