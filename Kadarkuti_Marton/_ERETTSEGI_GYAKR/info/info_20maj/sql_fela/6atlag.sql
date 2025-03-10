select avg(rendes.ev-levele.ev) as atlag
from tagsag as rendes, tagsag as levele
where 
rendes.tagid = levele.tagid
and
rendes.tipus = 'r' and levele.tipus = 'l'