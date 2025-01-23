set @egeszkod = (select kod from allapot where nev = "egészséges");
select megye.nev, sum(aerob.letszam) as letszam
from aerob inner join megye on aerob.mkod = megye.kod
where not nem and allkod = @egeszkod
group by mkod