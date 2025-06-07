-- Which movie type are being added most frequently in recent years?
SELECT type, year_added, COUNT(*) AS count
FROM main.netflix_table
WHERE date_added IS NOT NULL
GROUP BY year_added, type
ORDER BY year_added DESC, count DESC