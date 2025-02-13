SELECT fenykep.id, fenykep.evszam
FROM fenykep JOIN kapcsolo ON kapcsolo.fenyid = fenykep.id JOIN szemely ON szemely.id = kapcsolo.szemid
GROUP BY fenykep.id
ORDER BY COUNT(szemely.id) DESC
LIMIT 1;