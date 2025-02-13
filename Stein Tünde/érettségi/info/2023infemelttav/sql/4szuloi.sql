SELECT naptar.datum
FROM naptar
WHERE naptar.datum > "2022-09-07" AND naptar.melynap = 2
ORDER BY naptar.datum
LIMIT 1;