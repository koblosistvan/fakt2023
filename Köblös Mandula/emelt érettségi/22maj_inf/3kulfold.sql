SELECT a.nev, a.orszag
FROM allomas as a
WHERE a.orszag != ''
ORDER BY a.nev;