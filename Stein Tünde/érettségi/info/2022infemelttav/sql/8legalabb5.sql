SELECT allomas.nev, count(vonalid) as vonalak
FROM allomas join hely on hely.allomasid=allomas.id
GROUP BY allomas.id
HAVING vonalak >=5
ORDER BY vonalak desc;