set @nagypetra_id = (select id from diak where nev = "Nagy Petra");
set @min_felkeles = ( -- 06:00:00
    select felkeles from alvas 
    where diakid = @nagypetra_id 
    order by felkeles 
    limit 1
);
select nev
from diak
where id not in (
	select diakid
    from alvas
    where felkeles >= @min_felkeles
)