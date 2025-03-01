select datum, kezdes, hossz, nev
from munka inner join tevekenyseg on munka.tevekenysegid = tevekenyseg.id
where datum between "2016-10-29" and "2016-11-06"
and munka.id not in (select munkaid from jelentkezes)
order by datum, kezdes