SELECT uralkodo.nev, hivatal.mettol, hivatal.meddig
FROM hivatal JOIN uralkodo ON uralkodo.azon = hivatal.uralkodo_az JOIN uralkodohaz ON uralkodohaz.azon = uralkodo.uhaz_az
WHERE uralkodohaz.nev= "Árpád-ház"
ORDER BY hivatal.mettol;