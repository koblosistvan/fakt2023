SELECT nevado, ag, SUM(pontszam) AS osszpont FROM feladat INNER JOIN feladatsor ON feladatsor.id = feladat.feladatsorid
GROUP BY feladatsorid
HAVING osszpont != 150