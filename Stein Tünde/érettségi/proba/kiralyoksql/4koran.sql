SELECT uralkodo.nev
FROM uralkodo JOIN hivatal ON hivatal.uralkodo_az = uralkodo.azon
WHERE hivatal.koronazas < hivatal.mettol;