-- Which directors appear most frequently, and what type are they associated with? (Top 5)
SELECT director, type, COUNT(*) AS count
FROM main.netflix_table
WHERE director IS NOT NULL
GROUP BY director, type
ORDER BY count DESC
LIMIT 5