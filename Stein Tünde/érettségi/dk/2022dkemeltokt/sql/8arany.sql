SELECT megye.nev, SUM(aerob.letszam)/megye.letszam
FROM aerob JOIN megye ON megye.kod = aerob.mkod
GROUP BY megye.kod
ORDER BY SUM(aerob.letszam)/megye.letszam DESC
LIMIT 1;