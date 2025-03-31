select nev from hivatal inner join uralkodo on hivatal.uralkodo_az = uralkodo.azon
where koronazas is null or mettol < koronazas
