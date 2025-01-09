SELECT diak.nev, alvas.lefekves
FROM diak JOIN alvas ON alvas.diakid = diak.id
WHERE month(diak.szuldatum) = month(alvas.datum) AND day(diak.szuldatum) = day(alvas.datum);