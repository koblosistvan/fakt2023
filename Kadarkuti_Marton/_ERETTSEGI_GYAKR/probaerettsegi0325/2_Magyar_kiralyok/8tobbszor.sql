select nev, sum(meddig-mettol+1) as total_uralkodas
from hivatal inner join uralkodo on hivatal.uralkodo_az = uralkodo.azon
group by hivatal.uralkodo_az
having count(hivatal.uralkodo_az) > 1