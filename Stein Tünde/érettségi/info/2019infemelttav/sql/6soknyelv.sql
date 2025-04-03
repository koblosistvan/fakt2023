SELECT szemely.nev
FROM szemely JOIN fordito ON fordito.szemelyid = szemely.id JOIN nyelv ON nyelv.id = fordito.nyelvid
WHERE nyelv.fnyelv = "magyar"
GROUP BY szemely.id
ORDER BY count(nyelv.cnyelv)

limit 1;