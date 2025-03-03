SELECT keverek.nev as Fűszerkeverék, osszetevo.nev as Összetevők
FROM keverek JOIN kapcsolat ON kapcsolat.keverekid = keverek.id JOIN osszetevo on osszetevo.id = kapcsolat.osszetevoid
ORDER BY keverek.nev, osszetevo.nev;