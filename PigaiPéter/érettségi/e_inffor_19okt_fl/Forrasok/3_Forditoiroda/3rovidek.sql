select count(*), sum(nyelv.egysegar)
from nyelv join doku on nyelv.id = doku.nyelvid
where doku.terjedelem <= 5000