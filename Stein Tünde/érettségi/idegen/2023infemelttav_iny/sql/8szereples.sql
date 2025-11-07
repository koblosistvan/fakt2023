SELECT fenykep.evszam, szemely.nev, COUNT(fenykep.evszam)
FROM fenykep JOIN kapcsolo ON kapcsolo.fenyid=fenykep.id JOIN szemely ON szemely.id=kapcsolo.szemid
GROUP BY szemely.nev
HAVING szemely.nev != "NULL"
ORDER BY fenykep.evszam, szemely.nev;