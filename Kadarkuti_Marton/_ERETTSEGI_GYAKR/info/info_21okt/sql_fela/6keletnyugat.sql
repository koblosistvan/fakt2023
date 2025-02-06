select alloviz.nev
from helykapcs inner join alloviz on helykapcs.allovizid = alloviz.id inner join telepulesgps on helykapcs.gpsid = telepulesgps.id
group by allovizid, alloviz.nev
order by max(hosszusag)-min(hosszusag) desc
limit 1