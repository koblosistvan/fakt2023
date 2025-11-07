select diak.osztaly as "osztály", diak.nev as "név", munka.datum as "dátum", munka.kezdes as "időpont", munka.hossz as "óraszám", tevekenyseg.nev as "tevékenység"
from diak join jelentkezes on diak.id = jelentkezes.diakid join munka on jelentkezes.munkaid = munka.id join tevekenyseg on munka.tevekenysegid = tevekenyseg.id
where diak.osztaly like "10%" and jelentkezes.teljesitve
order by diak.osztaly asc, diak.nev asc, munka.datum asc