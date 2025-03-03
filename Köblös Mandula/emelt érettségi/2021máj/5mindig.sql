SELECT e.nev, d.cim
FROM eloadok as e INNER JOIN dalok as d on d.eloadoid = e.eloadoid
					INNER JOIN lista as l on l.dalid = d.dalid
GROUP BY l.dalid
HAVING count(*) = 21;