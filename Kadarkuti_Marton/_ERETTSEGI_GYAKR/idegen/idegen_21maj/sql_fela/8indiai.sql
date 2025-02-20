select keverek.nev as "Fűszerkeverék", osszetevo.nev as "Összetevők"
from kapcsolat inner join keverek on kapcsolat.keverekid = keverek.id inner join osszetevo on kapcsolat.osszetevoid = osszetevo.id
where ajanlat like "%india%"
order by keverek.nev, osszetevo.nev