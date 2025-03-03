SELECT alloviz.nev, terulet, telepulesgps.nev
FROM alloviz, helykapcs, telepulesgps
WHERE alloviz.id=allovizid And telepulesgps.id=gpsid And
 allovizid in (
select alloviz.id
FROM alloviz as a 
	inner join helykapcs as h on a.id=h.allovizid 
	inner join telepulesgps as t ON h.gpsid=t.id
GROUP by h.allovizid
HAVING count(*) = 1
 ) And
 gpsid IN ( 
select t.id
FROM alloviz as a 
	inner join helykapcs as h on a.id=h.allovizid 
	inner join telepulesgps as t ON h.gpsid=t.id
GROUP by h.gpsid
HAVING count(*) = 1);