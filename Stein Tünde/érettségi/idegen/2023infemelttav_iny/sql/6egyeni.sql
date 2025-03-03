SELECT nev, fenyid
FROM szemely, kapcsolo
WHERE id = szemid AND
	fenyid not in(
        	SELECT fenyid
        	FROM fenykep JOIN kapcsolo ON kapcsolo.fenyid = fenykep.id
        	GROUP BY fenyid
        	HAVING count(szemid) > 1
        );