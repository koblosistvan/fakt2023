SELECT allomas.nev, hely.tav
FROM allomas JOIN hely on hely.allomasid=allomas.id
WHERE vonalid = 140 AND hely.tav <= 100;