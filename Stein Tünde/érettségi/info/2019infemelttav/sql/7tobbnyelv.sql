SELECT nev 
FROM nyelv, fordito, szemely 
WHERE nyelv.id=nyelvid AND szemelyid=szemely.id AND 
 nyelv.fnyelv = "magyar" and nyelv.cnyelv = "angol" and szemely.id in(SELECT szemely.id FROM szemely JOIN fordito ON fordito.szemelyid = szemely.id JOIN nyelv ON nyelv.id = fordito.nyelvid WHERE nyelv.fnyelv = "magyar" and nyelv.cnyelv = "orosz");