select count(kapcsolat.keverekid)
from kapcsolat join osszetevo on kapcsolat.osszetevoid = osszetevo.id
group by kapcsolat.osszetevoid
having kapcsolat.osszetevoid in (select osszetevo.id from osszetevo where osszetevo.nev LIKE "bazsalikom")