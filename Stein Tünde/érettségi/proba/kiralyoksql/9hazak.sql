SELECT uralkodohaz.nev, COUNT(DISTINCT uralkodo.azon) as uralkodok_szama
FROM uralkodohaz JOIN uralkodo ON uralkodo.uhaz_az = uralkodohaz.azon
GROUP BY uralkodohaz.azon
ORDER BY uralkodok_szama DESC;