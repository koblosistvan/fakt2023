SELECT DISTINCT palya.ut, palya.kesz
FROM palya JOIN telepules ON telepules.ut=palya.ut JOIN vege ON vege.ut = telepules.ut
WHERE telepules.hatar = "Szlovákia"
	AND telepules.ut = vege.ut;