select fenyid, evszam
from kapcsolo join fenykep on kapcsolo.fenyid = fenykep.id join szemely on kapcsolo.szemid = szemely.id
group by fenyid
order by count(*) desc
limit 1