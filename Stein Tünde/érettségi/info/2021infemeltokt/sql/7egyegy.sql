SELECT alloviz.nev, terulet, telepulesgps.nev
FROM alloviz, helykapcs, telepulesgps
WHERE alloviz.id=allovizid And telepulesgps.id=gpsid And
	  allovizid in(SELECT allovizid FROM helykapcs GROUP BY allovizid HAVING COUNT(gpsid) = 1) And
	  gpsid in(SELECT gpsid FROM helykapcs GROUP BY gpsid HAVING COUNT(allovizid) = 1);