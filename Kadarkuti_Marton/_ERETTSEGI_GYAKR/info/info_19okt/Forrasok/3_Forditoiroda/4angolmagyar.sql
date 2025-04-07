select terjedelem, szakterulet
from doku inner join nyelv on doku.nyelvid = nyelv.id
where fnyelv="angol" and cnyelv="magyar"
order by terjedelem desc