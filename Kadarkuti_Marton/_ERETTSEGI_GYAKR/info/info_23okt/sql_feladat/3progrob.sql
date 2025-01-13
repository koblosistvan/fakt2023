SELECT nev, tanar FROM szakkor
WHERE lcase(nev) LIKE "%programoz%" OR lcase(nev) LIKE "%robotika%"