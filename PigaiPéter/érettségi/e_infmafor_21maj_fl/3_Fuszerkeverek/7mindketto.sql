SELECT nev
FROM keverek
WHERE
	id in (
        select kapcsolat.keverekid 
        from kapcsolat 
        	join osszetevo on kapcsolat.osszetevoid = osszetevo.id 
       	where osszetevo.nev like "paradicsom" )
    and id in (
        select kapcsolat.keverekid 
        from kapcsolat 
        	join osszetevo on kapcsolat.osszetevoid = osszetevo.id
        where osszetevo.nev like "chili")
