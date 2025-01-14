SELECT nev, tanar, mk, count(*) as jelentkezok_szama FROM szakkor JOIN jelentkezes on szakkor.azon = jelentkezes.szakazon
GROUP BY szakazon
HAVING jelentkezok_szama >= 10