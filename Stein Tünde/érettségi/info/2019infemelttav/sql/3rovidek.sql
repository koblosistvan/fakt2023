SELECT COUNT(doku.id) as dokumentumok_szama, SUM(nyelv.egysegar) osszar
FROM doku JOIN nyelv ON nyelv.id = doku.nyelvid
WHERE terjedelem < 5000;