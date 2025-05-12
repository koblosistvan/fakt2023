select count(*), sum(egysegar)
from doku inner join nyelv on doku.nyelvid = nyelv.id
where terjedelem <= 5000