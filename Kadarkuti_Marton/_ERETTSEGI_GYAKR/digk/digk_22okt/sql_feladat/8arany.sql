select megye.nev, sum(aerob.letszam)/megye.letszam as arany
from aerob inner join megye on aerob.mkod = megye.kod
group by mkod
order by arany
limit 1