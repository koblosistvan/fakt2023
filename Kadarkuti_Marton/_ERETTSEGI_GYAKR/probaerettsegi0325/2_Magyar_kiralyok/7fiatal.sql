select nev, 1+mettol-szul as eletkor
from hivatal inner join uralkodo on hivatal.uralkodo_az = uralkodo.azon
where 1+mettol-szul < 15
order by eletkor