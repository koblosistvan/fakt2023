select uralkodo.nev, mettol, meddig
from hivatal inner join uralkodo on hivatal.uralkodo_az = uralkodo.azon inner join uralkodohaz on uralkodo.uhaz_az = uralkodohaz.azon
where uralkodohaz.nev = "Árpád-ház"
order by mettol