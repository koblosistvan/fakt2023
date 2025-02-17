SELECT alloviz.nev, COUNT(helykapcs.gpsid) as telepulesszam
FROM alloviz JOIN helykapcs on helykapcs.allovizid = alloviz.id
GROUP BY alloviz.id
HAVING telepulesszam >= 3;