SELECT fenykep.id, fenykep.evszam-szemely.szulev AS eletkor, fenykep.meret_x*fenykep.meret_y AS meret
FROM fenykep JOIN kapcsolo ON kapcsolo.fenyid = fenykep.id JOIN szemely ON szemely.id = kapcsolo.szemid
WHERE szemely.nev LIKE "%Vince%" ORDER BY `evszam` ASC 