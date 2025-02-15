SELECT eloadok.nev, dalok.cim, dalok.megjelenes
FROM eloadok JOIN dalok on dalok.eloadoid = eloadok.eloadoid
WHERE dalok.cim = "love"
	or dalok.cim like "% love"
    or dalok.cim like "love %"
    or dalok.cim like "% love %"
order by dalok.megjelenes DESC;