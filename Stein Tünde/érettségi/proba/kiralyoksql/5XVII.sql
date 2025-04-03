SELECT COUNT(uralkodo.azon) as hany_kiraly
FROM uralkodo JOIN hivatal ON hivatal.uralkodo_az = uralkodo.azon
WHERE hivatal.mettol BETWEEN 1601 AND 1700 OR hivatal.meddig BETWEEN 1601 AND 1700;