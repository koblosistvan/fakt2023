set @egeszkod = (select kod from allapot where nev = "egészséges");
select megye.nev as Megyenév, sum(aerob.letszam)/megye.letszam as Arány
from aerob inner join megye on aerob.mkod = megye.kod
where allkod != @egeszkod
group by mkod
having Arány > 0.25