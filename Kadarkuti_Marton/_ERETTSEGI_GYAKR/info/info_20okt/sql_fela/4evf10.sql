select osztaly as "osztály", diak.nev as "név", datum as "dátum", kezdes as "időpont", hossz as "óraszám", tevekenyseg.nev as "tevékenység"
from jelentkezes inner join diak on jelentkezes.diakid = diak.id inner join munka on jelentkezes.munkaid = munka.id inner join tevekenyseg on munka.tevekenysegid = tevekenyseg.id
where osztaly like "10/%" and jelentkezes.teljesitve
order by osztaly, diak.nev, datum, kezdes