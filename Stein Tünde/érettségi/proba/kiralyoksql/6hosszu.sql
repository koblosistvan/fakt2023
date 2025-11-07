SELECT uralkodo.nev
FROM uralkodo JOIN hivatal ON hivatal.uralkodo_az = uralkodo.azon
ORDER BY (hivatal.meddig-hivatal.mettol+1) DESC
LIMIT 1;