SELECT eloadok.nev, dalok.cim
FROM eloadok JOIN dalok ON dalok.eloadoid = eloadok.eloadoid JOIN lista ON lista.dalid = dalok.dalid
GROUP BY dalok.dalid
HAVING COUNT(lista.helyezes) = 21;