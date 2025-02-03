SELECT allomas.nev, allomas.tipus, hely.tav
from allomas join hely on hely.allomasid = allomas.id
WHERE hely.vonalid = 80 and allomas.mukodo
ORDER BY tav;