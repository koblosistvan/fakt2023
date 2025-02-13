SELECT DISTINCT telepules.nev, telepules.ut
FROM telepules JOIN vege ON vege.ut = telepules.ut
WHERE telepules.nev in(
    SELECT telepules.nev FROM telepules as t1 JOIN telepules as t2 ON t1.nev=t2.nev
    WHERE t1.ut=t2.ut
	);