select distinct munka.datum, munka.kezdes, munka.hossz, tevekenyseg.nev
from munka join tevekenyseg on tevekenyseg.id = munka.tevekenysegid
where munka.datum between "2016-10-29" and "2016-11-06" and munka.id not in (SELECT munkaid from jelentkezes)
order by munka.datum, munka.kezdes