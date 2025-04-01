SELECT tagsag.ev as megválasztás_éve, tag.nev as tag_neve, concat(tagsag.ev,"-",tag.elhunyt) as élt
FROM tagsag JOIN tag ON tag.id = tagsag.tagid
WHERE tagsag.tipus = "r" AND tagsag.ev BETWEEN 1901 AND 2000
ORDER BY tagsag.ev, tag.nev;