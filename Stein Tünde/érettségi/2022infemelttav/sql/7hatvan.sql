SELECT allomas.nev, hely.vonalid
FROM allomas JOIN hely ON hely.allomasid = allomas.id
WHERE vonalid in (
    SELECT vonalid
    from allomas join hely on hely.allomasid = allomas.id
    WHERE allomas.nev = "Hatvan"
    )
AND allomas.nev != "Hatvan";