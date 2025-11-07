SELECT nevado, count(*) as be_nem_kuldott_szama FROM feladat inner join feladatsor 
on feladat.feladatsorid = feladatsor.id
WHERE feladat.id NOT IN (
	SELECT feladatid FROM megoldas inner join csapat on megoldas.csapatid = csapat.id
    WHERE csapat.nev LIKE "%#win%"
)
group by nevado