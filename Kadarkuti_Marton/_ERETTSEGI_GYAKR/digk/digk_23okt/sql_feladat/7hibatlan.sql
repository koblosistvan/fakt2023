SELECT DISTINCT nev FROM csapat INNER JOIN megoldas ON csapat.id = megoldas.csapatid INNER JOIN feladat ON feladat.id = megoldas.feladatid
WHERE megoldas.pontszam = feladat.pontszam