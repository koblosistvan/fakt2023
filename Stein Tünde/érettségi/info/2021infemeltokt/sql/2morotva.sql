SELECT alloviz.nev, alloviz.terulet
FROM alloviz
WHERE alloviz.nev LIKE "%morotva%"
ORDER BY alloviz.terulet DESC;