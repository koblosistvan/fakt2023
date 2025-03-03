SELECT alloviz.nev, terulet, telepulesgps.nev
FROM alloviz, helykapcs, telepulesgps
WHERE alloviz.id=allovizid And telepulesgps.id=gpsid And
	  allovizid in (select allovizid from helykapcs group by allovizid having count(*)=1) And
	  gpsid in (select gpsid from helykapcs group by gpsid having count(*)=1);
