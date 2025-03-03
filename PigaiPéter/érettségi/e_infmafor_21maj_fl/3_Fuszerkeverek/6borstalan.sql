SELECT keverek.nev
from keverek join kapcsolat on keverek.id = kapcsolat.keverekid join osszetevo on kapcsolat.osszetevoid = osszetevo.id
where osszetevo.nev NOT LIKE "%bors"
GROUP by kapcsolat.keverekid