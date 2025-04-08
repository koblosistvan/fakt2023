SELECT doku.szakterulet as Szakterulet, nyelv.fnyelv as Forrasnyelv, nyelv.cnyelv as Celnyelv
FROM doku JOIN nyelv on nyelv.id = doku.nyelvid  
ORDER BY doku.szakterulet, nyelv.fnyelv;