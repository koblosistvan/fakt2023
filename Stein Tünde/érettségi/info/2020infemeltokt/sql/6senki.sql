SELECT munka.datum, munka.kezdes, munka.hossz
FROM munka
WHERE munka.id not in (
    SELECT jelentkezes.munkaid
    FROM jelentkezes
    )
    AND (MONTH(munka.datum) = 10 AND DAY(munka.datum) >=29) OR (MONTH(munka.datum) = 11 AND DAY(munka.datum) <= 6)
ORDER BY munka.datum, munka.kezdes;