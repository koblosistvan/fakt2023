SELECT tag.nev, min(tagsag.ev) as eloszor
from tag JOIN tagsag on tagsag.tagid = tag.id
GROUP BY tag.id;