SELECT keverek.nev, (1000*keverek.ar)/keverek.tomeg as kiloar
FROM keverek
ORDER BY kiloar DESC
LIMIT 1;