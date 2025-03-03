select nev
from keverek
where id not in 
(
select keverekid
from kapcsolat inner join osszetevo on kapcsolat.osszetevoid = osszetevo.id
where osszetevo.nev like "%bors"
)