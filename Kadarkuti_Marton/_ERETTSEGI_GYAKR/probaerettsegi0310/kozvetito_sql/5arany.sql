select (select max(ar) from hirdetes where allapot = "meghirdetve" ) / (select min(ar) from hirdetes where allapot = "meghirdetve" ) as arany