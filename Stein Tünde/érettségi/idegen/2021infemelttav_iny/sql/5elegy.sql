SELECT keverek.nev, count(osszetevoid) as osszetevok_szama FROM keverek JOIN kapcsolat ON kapcsolat.keverekid = keverek.id
GROUP BY keverek.id
ORDER BY osszetevok_szama DESC;