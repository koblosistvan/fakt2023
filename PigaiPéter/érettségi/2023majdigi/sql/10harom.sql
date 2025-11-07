select szinesz, hang, count(distinct filmaz) as filmek_szama
from szinkron
group by szinesz, hang
having filmek_szama >= 3
order by filmek_szama desc