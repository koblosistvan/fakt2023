SELECT alloviz.nev, alloviz.tipus, alloviz.terulet
FROM alloviz
WHERE (alloviz.terulet BETWEEN 3 AND 10)
	AND alloviz.vizgyujto >= alloviz.terulet*10;