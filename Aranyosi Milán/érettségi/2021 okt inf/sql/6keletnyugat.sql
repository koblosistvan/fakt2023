select a.nev
FROM alloviz as a 
	inner join helykapcs as h on a.id=h.allovizid 
	inner join telepulesgps as t ON h.gpsid=t.id
ORDER BY t.hosszusag
limit 1;