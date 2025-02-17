SELECT fenykep.id, fenykep.evszam
FROM fenykep
WHERE fenykep.id in (
    SELECT fenykep.id
    FROM fenykep JOIN kapcsolo ON kapcsolo.fenyid = fenykep.id JOIN szemely ON szemely.id = kapcsolo.szemid
    WHERE szemely.szulev = fenykep.evszam
    );