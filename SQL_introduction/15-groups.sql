-- Task: List the number of records with the same score in the table second_table
-- This script will display the score and the number of records for each score, sorted by the number of records in descending order

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
