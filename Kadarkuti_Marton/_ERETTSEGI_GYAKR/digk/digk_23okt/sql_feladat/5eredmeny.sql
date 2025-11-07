SELECT nev, SUM(pontszam) AS osszpontszam FROM csapat INNER JOIN megoldas ON csapat.id = megoldas.csapatid
GROUP BY csapatid
ORDER BY osszpontszam DESC