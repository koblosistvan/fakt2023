select palya.ut, kesz
from palya inner join telepules on palya.ut = telepules.ut
where lcase(hatar) like "%szlovákia%"

/*
A pont jár akkor is, ha a kész autópályák közül a 0 km hosszúakat a megjelenítésből kizárta.
Például:
SELECT palya.ut, kesz
FROM palya, vege, telepules
WHERE palya.ut=vege.ut AND telepid=telepules.id AND hatar='Szlovákia';
*/