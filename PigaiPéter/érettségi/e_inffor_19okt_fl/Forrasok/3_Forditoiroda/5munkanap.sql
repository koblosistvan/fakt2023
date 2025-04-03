SELECT doku.szakterulet, nyelv.fnyelv, nyelv.cnyelv
from doku join nyelv on doku.nyelvid = nyelv.id
where doku.munkaido BETWEEN 7 and 9
order by nyelv.fnyelv desc