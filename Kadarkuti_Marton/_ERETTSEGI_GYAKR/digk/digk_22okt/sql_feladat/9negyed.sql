
select megye.nev as Megyenév, sum(aerob.letszam)/megye.letszam as Arány
from aerob inner join megye on aerob.mkod = megye.kod
where allkod != (select kod from allapot where nev = "egészséges")
group by mkod
having Arány > 0.25