SELECT fenykep.id, fenykep.evszam
FROM fenykep JOIN kapcsolo ON kapcsolo.fenyid=fenykep.id JOIN szemely ON szemely.id=kapcsolo.szemid
WHERE szemely.nev = "Anna" AND
	fenykep.id IN (
        SELECT fenykep.id
        FROM fenykep JOIN kapcsolo ON kapcsolo.fenyid=fenykep.id JOIN szemely ON szemely.id=kapcsolo.szemid
        WHERE szemely.nev = "Matyi"
        );