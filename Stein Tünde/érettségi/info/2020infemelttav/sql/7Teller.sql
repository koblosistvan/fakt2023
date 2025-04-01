SELECT nev, ev, elhunyt
FROM tag, tagsag
WHERE tag.id=tagid
AND ev<= (SELECT tagsag.ev FROM tagsag JOIN tag ON tag.id = tagsag.tagid WHERE tag.nev = "Teller Ede" AND tagsag.tipus = 't') 
AND (elhunyt>=( SELECT tag.elhunyt FROM tagsag JOIN tag ON tag.id = tagsag.tagid WHERE tag.nev = "Teller Ede") OR NOT elhunyt = "" )
AND tipus='t';