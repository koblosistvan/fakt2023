SELECT DISTINCT keverek.nev
FROM keverek JOIN kapcsolat ON kapcsolat.keverekid = keverek.id JOIN osszetevo ON osszetevo.id = kapcsolat.osszetevoid
WHERE keverek.id not in (
    SELECT keverek.id FROM keverek JOIN kapcsolat ON kapcsolat.keverekid = keverek.id JOIN osszetevo ON osszetevo.id = kapcsolat.osszetevoid
    GROUP BY keverek.id HAVING osszetevo.nev LIKE "%bors"
    );