SELECT megye.nev, aerob.letszam
FROM megye JOIN aerob ON aerob.mkod = megye.kod JOIN allapot ON allapot.kod = aerob.allkod
WHERE aerob.nem = 0 AND allapot.nev = 'egészséges'
ORDER BY aerob.letszam DESC;