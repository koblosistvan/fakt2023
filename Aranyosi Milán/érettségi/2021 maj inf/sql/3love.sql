SELECT e.nev, d.cim, d.megjelenes
FROM dalok as d 
	INNER JOIN eloadok as e on e.eloadoid = d.eloadoid
WHERE d.cim Like "%love%"  
ORDER BY d.megjelenes DESC;