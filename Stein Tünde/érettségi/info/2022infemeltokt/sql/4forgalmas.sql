SELECT telepules.nev, COUNT(telepules.ut) as autopalyak_szama
from telepules
GROUP BY telepules.nev
HAVING telepules.nev != "Budapest"
ORDER by autopalyak_szama DESC
LIMIT 1;