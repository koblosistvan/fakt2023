SELECT aerob.letszam
FROM aerob JOIN megye ON megye.kod = aerob.mkod JOIN allapot ON allapot.kod = aerob.allkod
WHERE aerob.nem = 1 AND megye.nev = 'Zala' AND allapot.nev = 'egészséges';