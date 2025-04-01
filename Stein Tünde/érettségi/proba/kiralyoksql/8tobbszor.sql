SELECT uralkodo.nev, (SUM(hivatal.meddig)- SUM(hivatal.mettol)+ COUNT(uralkodo.azon)) as osszes
FROM uralkodo JOIN hivatal ON hivatal.uralkodo_az = uralkodo.azon
GROUP BY uralkodo.azon
HAVING COUNT(uralkodo.azon) != 1;