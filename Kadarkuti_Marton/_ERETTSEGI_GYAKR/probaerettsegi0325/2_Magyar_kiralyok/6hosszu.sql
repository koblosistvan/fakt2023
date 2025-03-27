select nev, 1+meddig-mettol as hany_ev
from hivatal inner join uralkodo on hivatal.uralkodo_az = uralkodo.azon
order by hany_ev desc
limit 1