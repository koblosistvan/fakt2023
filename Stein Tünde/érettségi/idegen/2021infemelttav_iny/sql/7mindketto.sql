SELECT nev 
FROM keverek 
WHERE 
id in 
(SELECT keverekid FROM osszetevo JOIN kapcsolat ON kapcsolat.osszetevoid = osszetevo.id WHERE osszetevo.nev = "paradicsom") 
and 
id in 
(SELECT keverekid FROM osszetevo JOIN kapcsolat ON kapcsolat.osszetevoid = osszetevo.id WHERE osszetevo.nev = "chili");