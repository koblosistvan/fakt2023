SELECT doku.terjedelem, doku.szakterulet
FROM doku JOIN nyelv ON nyelv.id = doku.nyelvid
WHERE nyelv.fnyelv = "angol" AND nyelv.cnyelv = "magyar"
ORDER BY doku.terjedelem DESC;