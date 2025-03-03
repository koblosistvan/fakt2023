SELECT lista.ev, lista.helyezes, eloadok.nev, dalok.cim, dalok.megjelenes
FROM eloadok JOIN dalok ON dalok.eloadoid = eloadok.eloadoid JOIN lista ON lista.dalid = dalok.dalid
WHERE lista.helyezes <= 10
ORDER BY lista.ev, lista.helyezes;