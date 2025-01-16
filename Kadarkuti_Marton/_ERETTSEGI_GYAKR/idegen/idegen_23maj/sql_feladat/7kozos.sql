set @matyi_id = (select distinct id from szemely where nev = 'Matyi');
set @anna_id = (select distinct id from szemely where nev = 'Anna');

select id, evszam
from fenykep
where 
id in (
	select fenyid from kapcsolo
    where szemid = @matyi_id
)
and
id in (
	select fenyid from kapcsolo
    where szemid = @anna_id
)
