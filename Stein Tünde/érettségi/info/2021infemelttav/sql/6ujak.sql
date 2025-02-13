SELECT DISTINCT lista.helyezes, eloadok.nev, dalok.cim
FROM eloadok JOIN dalok ON dalok.eloadoid = eloadok.eloadoid JOIN lista ON lista.dalid = dalok.dalid
WHERE lista.dalid in (
	SELECT lista.dalid FROM lista WHERE lista.ev = 2019)
    and lista.dalid not in (
	SELECT lista.dalid FROM lista WHERE lista.ev = 2018)
ORDER BY lista.helyezes;