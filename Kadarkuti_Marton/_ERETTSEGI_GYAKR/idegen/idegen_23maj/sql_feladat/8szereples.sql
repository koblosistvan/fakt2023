select evszam as 'Év', nev as 'Név', count(*) as 'Darab'
from kapcsolo join fenykep on kapcsolo.fenyid = fenykep.id join szemely on kapcsolo.szemid = szemely.id
where nev is not null -- vannak ilyenek valamiert
group by nev
order by evszam, nev