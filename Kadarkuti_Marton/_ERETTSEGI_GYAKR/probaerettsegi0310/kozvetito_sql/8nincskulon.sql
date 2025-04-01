SELECT kozterulet, hazszam
FROM ingatlan
WHERE id NOT IN (select ingatlanid from helyiseg where funkcio = "konyha")
	AND id NOT IN (select ingatlanid from helyiseg where funkcio = "WC");
