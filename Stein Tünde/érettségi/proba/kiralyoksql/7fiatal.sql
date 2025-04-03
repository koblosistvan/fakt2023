SELECT uralkodo.nev, (hivatal.mettol-uralkodo.szul + 1) as hany_evesen
FROM uralkodo JOIN hivatal ON hivatal.uralkodo_az = uralkodo.azon
WHERE (hivatal.mettol-uralkodo.szul + 1) < 15
ORDER BY hany_evesen;