SELECT diak.osztaly, COUNT(DISTINCT diak.id) as letszam
FROM diak JOIN jelentkezes ON jelentkezes.diakid = diak.id
WHERE jelentkezes.teljesitve
GROUP BY diak.osztaly;