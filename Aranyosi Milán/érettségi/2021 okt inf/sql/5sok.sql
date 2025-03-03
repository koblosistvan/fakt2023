select a.nev, count(*) as telepulesek_szama
FROM alloviz as a 
	inner join helykapcs as h on a.id=h.allovizid 
	inner join telepulesgps as t ON h.gpsid=t.id
GROUP BY a.id
HAVING telepulesek_szama >= 3;