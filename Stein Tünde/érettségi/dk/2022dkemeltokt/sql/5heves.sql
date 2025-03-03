SELECT COUNT(megye.kod) as megyek_szama
FROM megye
WHERE megye.letszam < (
    SELECT megye.letszam
    FROM megye
    WHERE megye.nev = 'Heves'
    );