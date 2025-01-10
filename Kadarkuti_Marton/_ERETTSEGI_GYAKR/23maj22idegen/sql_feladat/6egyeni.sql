SELECT nev, fenyid
FROM szemely, kapcsolo
WHERE id = szemid AND
fenyid in (
	select fenyid
    from kapcsolo join szemely on kapcsolo.szemid = szemely.id
    group by fenyid
    having count(*)=1
)