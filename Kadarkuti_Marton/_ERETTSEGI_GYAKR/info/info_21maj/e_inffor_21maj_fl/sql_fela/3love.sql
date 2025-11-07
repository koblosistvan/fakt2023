select nev, cim, megjelenes
from dalok inner join eloadok on dalok.eloadoid = eloadok.eloadoid
where
lcase(cim) like "love %" -- elejen
or
lcase(cim) like "% love %" -- kozben
or
lcase(cim) like "% love" -- vegen
or 
lcase(cim) like "love" -- cim

order by megjelenes desc