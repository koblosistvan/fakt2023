select szakterulet, fnyelv, cnyelv
from doku inner join nyelv on doku.nyelvid = nyelv.id
where munkaido between 7 and 9
order by fnyelv