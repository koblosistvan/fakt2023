SELECT lista.helyezes, eloadok.nev, dalok.cim
FROM lista JOIN dalok ON dalok.dalid = lista.dalid JOIN eloadok ON eloadok.eloadoid = dalok.eloadoid
WHERE lista.helyezes >= 2000-285+1 AND lista.ev = 2019
ORDER BY lista.helyezes;