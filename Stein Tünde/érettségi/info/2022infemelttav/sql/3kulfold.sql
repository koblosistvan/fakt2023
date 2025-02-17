SELECT allomas.nev, allomas.orszag
FROM allomas
WHERE allomas.orszag != ""
ORDER BY allomas.nev;