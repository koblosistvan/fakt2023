SELECT alloviz.tipus, alloviz.nev, alloviz.terulet
FROM alloviz
WHERE alloviz.tipus != ""
ORDER BY alloviz.tipus;