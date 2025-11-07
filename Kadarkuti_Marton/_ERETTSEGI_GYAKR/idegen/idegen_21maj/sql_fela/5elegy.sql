select nev, count(*) as osszetevok_szama
from kapcsolat inner join keverek on kapcsolat.keverekid = keverek.id
group by keverekid
order by osszetevok_szama desc