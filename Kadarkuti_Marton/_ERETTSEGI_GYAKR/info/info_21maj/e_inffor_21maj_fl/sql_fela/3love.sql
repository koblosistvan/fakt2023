select nev, cim, megjelenes
from dalok inner join eloadok on dalok.eloadoid = eloadok.eloadoid
where
lcase(cim) like "love %" -- elejen
or
lcase(cim) like "% love %" -- kozben
or
lcase(cim) like "% love" -- vegen
order by megjelenes desc