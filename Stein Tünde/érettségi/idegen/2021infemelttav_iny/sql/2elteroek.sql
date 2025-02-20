SELECT keverek.nev, keverek.tomeg, keverek.ar
FROM keverek
WHERE keverek.tomeg != 20
ORDER BY keverek.tomeg DESC;