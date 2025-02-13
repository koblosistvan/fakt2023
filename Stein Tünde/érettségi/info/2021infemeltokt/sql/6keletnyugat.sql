SELECT alloviz.nev
FROM alloviz JOIN helykapcs on helykapcs.allovizid = alloviz.id JOIN telepulesgps ON telepulesgps.id = helykapcs.gpsid
GROUP BY alloviz.id
ORDER BY max(telepulesgps.hosszusag)-min(telepulesgps.hosszusag) DESC
LIMIT 1;