SELECT ut
FROM telepules
WHERE nev in (
select nev from telepules where ut = "M6"
) AND
ut != "M6";
