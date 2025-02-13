SELECT palya.ut, sum(palya.kesz + palya.epul + palya.terv) as hossz
FROM palya
GROUP BY palya.ut
ORDER BY hossz DESC;