select count(*) from megye
where letszam < (select letszam from megye where nev = "Heves")