SELECT doku.szakterulet, nyelv.fnyelv, nyelv.cnyelv
FROM doku JOIN nyelv ON nyelv.id = doku.nyelvid
WHERE doku.munkaido BETWEEN 7 and 9
ORDER BY nyelv.fnyelv;