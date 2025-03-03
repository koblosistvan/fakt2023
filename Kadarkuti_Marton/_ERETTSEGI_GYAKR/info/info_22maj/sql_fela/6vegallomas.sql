SELECT indulasi.vonalid, indulasi.nev, veg.nev
FROM 
	(
		SELECT nev, vonalid 
			FROM allomas, hely 
			WHERE allomas.id=allomasid 
			AND tav = 0
	) AS indulasi,
	(
		SELECT nev, vonalid, tav 
			FROM allomas, hely 
			WHERE allomas.id=allomasid
	) AS veg,
	(
		SELECT vonalid, Max(tav) as maxtav
			FROM hely 
			GROUP BY vonalid
	) AS tulso
WHERE indulasi.vonalid=veg.vonalid
	AND veg.vonalid=tulso.vonalid
	AND veg.tav =tulso.maxtav;
