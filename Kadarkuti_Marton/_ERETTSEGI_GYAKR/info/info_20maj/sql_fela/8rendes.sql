select ev as "megválasztás éve", nev as "tag neve", concat(szuletett,' - ',elhunyt) as "élt"
from tagsag inner join tag on tagsag.tagid = tag.id
where tipus='r' and ev between 1901 and 2000
order by ev, nev