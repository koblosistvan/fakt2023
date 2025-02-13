SELECT e.nev, d.cim, d.megjelenes
FROM eloadok as e INNER JOIN dalok as d on d.eloadoid = e.eloadoid
WHERE d.cim like '% love %'
ORDER BY d.megjelenes;