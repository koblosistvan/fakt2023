SELECT SUM(aerob.letszam)
FROM aerob JOIN megye ON megye.kod = aerob.mkod
WHERE megye.nev = 'Somogy';