-- lists all records with a score >= 10 in second_tabl
SELECT score, name
  FROM second_table
  WHERE score >= 10
  ORDER BY score DESC;
