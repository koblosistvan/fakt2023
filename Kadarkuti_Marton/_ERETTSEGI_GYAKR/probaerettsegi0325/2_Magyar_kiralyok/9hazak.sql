select uralkodohaz.nev, count(distinct uralkodo_az) as uralkodok_szama
from hivatal inner join uralkodo on hivatal.uralkodo_az = uralkodo.azon inner join uralkodohaz on uralkodohaz.azon = uralkodo.uhaz_az
group by uhaz_az
order by uralkodok_szama desc