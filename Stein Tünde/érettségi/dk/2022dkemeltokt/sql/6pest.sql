SELECT SUM(aerob.letszam)/megye.letszam AS hanyadresz
FROM aerob JOIN megye ON megye.kod = aerob.mkod
WHERE megye.nev = 'Pest';