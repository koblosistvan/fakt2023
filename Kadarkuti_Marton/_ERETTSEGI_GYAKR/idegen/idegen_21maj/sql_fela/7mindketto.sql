SELECT nev
FROM keverek
WHERE 
id in 
(
select keverekid
from kapcsolat inner join osszetevo on kapcsolat.osszetevoid = osszetevo.id
where osszetevo.nev = "chili"
)
and
id in (
select keverekid
from kapcsolat inner join osszetevo on kapcsolat.osszetevoid = osszetevo.id
where osszetevo.nev = "paradicsom" 
)