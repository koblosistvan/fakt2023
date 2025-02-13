SELECT megye.nev as Megyenév, SUM(aerob.letszam)/megye.letszam as Arány
FROM aerob JOIN allapot ON allapot.kod = aerob.allkod JOIN megye ON megye.kod = aerob.mkod
WHERE allapot.nev != 'egeszseges'
GROUP BY megye.kod
HAVING Arány > 0.25;