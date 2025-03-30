SELECT kozterulet, hazszam
FROM ingatlan
WHERE id NOT IN (SELECT helyiseg.ingatlanid from helyiseg where helyiseg.funkcio like "WC")
	AND id NOT IN (SELECT helyiseg.ingatlanid from helyiseg where helyiseg.funkcio like "konyha");
