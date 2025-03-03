select id, evszam
from fenykep
where id in (
	select distinct fenyid
    from kapcsolo join szemely on kapcsolo.szemid = szemely.id join fenykep on kapcsolo.fenyid = fenykep.id
    where szulev = evszam
)