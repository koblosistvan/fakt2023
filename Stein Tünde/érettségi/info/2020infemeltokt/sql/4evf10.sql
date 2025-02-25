SELECT diak.osztaly as osztály, diak.nev as név, munka.datum as dátum, munka.kezdes as időpont, munka.hossz as óraszám, tevekenyseg.nev as tevékenység
FROM diak JOIN jelentkezes ON jelentkezes.diakid = diak.id JOIN munka ON munka.id = jelentkezes.munkaid JOIN tevekenyseg ON tevekenyseg.id = munka.tevekenysegid
ORDER BY diak.osztaly, diak.nev, munka.datum;