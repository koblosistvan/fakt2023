select keverek.nev, osszetevo.nev, count(kapcsolat.osszetevoid)
from keverek join kapcsolat on keverek.id = kapcsolat.keverekid join osszetevo on kapcsolat.osszetevoid = osszetevo.id
group by kapcsolat.keverekid
order by count(kapcsolat.osszetevoid) desc