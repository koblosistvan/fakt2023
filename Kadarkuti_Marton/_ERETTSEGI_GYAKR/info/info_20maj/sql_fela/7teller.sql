SELECT nev, ev, elhunyt
FROM tag, tagsag
WHERE tag.id=tagid
AND ev<=( select ev from tagsag where tipus='t' and tagid = (select id from tag where nev="Teller Ede") )
AND (elhunyt>=( select elhunyt from tag where nev = "Teller Ede" ) OR elhunyt is not null )
AND tipus='t'; 