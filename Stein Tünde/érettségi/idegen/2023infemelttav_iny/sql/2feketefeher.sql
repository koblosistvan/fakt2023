SELECT fenykep.evszam, fenykep.meret_x as szelesseg, fenykep.meret_y as magassag
FROM fenykep
WHERE fenykep.szines = 0
ORDER BY fenykep.evszam DESC;