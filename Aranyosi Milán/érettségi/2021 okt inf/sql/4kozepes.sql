select alloviz.nev, alloviz.tipus, alloviz.terulet
FROM alloviz
WHERE alloviz.id in (SELECT alloviz.id FROM alloviz WHERE alloviz.terulet BETWEEN 3 and 10)
AND (10 * alloviz.vizgyujto) >= alloviz.terulet;