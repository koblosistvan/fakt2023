select distinct rendezo as "Színész-Rendező"
from film
where rendezo in (
	select szinesz from szinkron
)