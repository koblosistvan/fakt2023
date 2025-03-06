select nev, min(ev) as eloszor
from tagsag inner join tag on tagsag.tagid = tag.id
group by tagid