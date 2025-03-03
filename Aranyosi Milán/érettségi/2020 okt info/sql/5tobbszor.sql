SELECT d.nev
FROM diak as d 
	INNER JOIN jelentkezes as j on d.id = j.diakid
WHERE j.elfogadva = 1 AND j.teljesitve = 0
GROUP BY d.id
HAVING COUNT(j.elfogadva) >=2;