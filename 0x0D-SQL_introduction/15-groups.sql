-- Lists the number of records with the same score in the table second_table in the database hbtn_0c_0
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score DESC;
