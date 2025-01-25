select palya.ut as "Autópálya", kesz as "Üzemhossz (km)", nev as "Érintett települések"
from telepules inner join palya on telepules.ut = palya.ut
where kesz
order by palya.ut, nev