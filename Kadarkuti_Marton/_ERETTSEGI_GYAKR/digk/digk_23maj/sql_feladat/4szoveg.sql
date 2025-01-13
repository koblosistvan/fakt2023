select distinct magyarszoveg, cim
from film
where 
	rendezo like "%Christopher Nolan%" and
	studio like "%Mafilm Audio Kft.%"
order by magyarszoveg