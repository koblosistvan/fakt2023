SELECT 
	nev, 
	round( sum( -- 2 tizedesre kerekit
        time_to_sec(
            addtime(felkeles, subtime('24:00:00', lefekves) )
        )
    )/3600/count(*), 2) as atlag_ora
from alvas inner join diak on alvas.diakid = diak.id
group by diakid
having atlag_ora < 8