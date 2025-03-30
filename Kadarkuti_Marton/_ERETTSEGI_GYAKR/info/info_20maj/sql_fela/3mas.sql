select nev, identitas, tipus, ev
from tagsag inner join tag on tagsag.tagid = tag.id
where length(identitas) and tipus in ('r','l')
order by ev