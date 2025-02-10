select nev, count(*) as telepulesek_szama
from helykapcs inner join alloviz on helykapcs.allovizid = alloviz.id
group by helykapcs.allovizid
having telepulesek_szama >= 3