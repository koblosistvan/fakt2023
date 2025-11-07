select count(*) as "keverekek_szama"
from kapcsolat inner join keverek on kapcsolat.keverekid = keverek.id
where osszetevoid = (select id from osszetevo where nev = "bazsalikom")