SELECT DISTINCT tag.nev, tag.identitas, tagsag.tipus, tagsag.ev
FROM tag JOIN tagsag ON tagsag.tagid = tag.id
WHERE tag.identitas != ''
ORDER BY tagsag.ev;