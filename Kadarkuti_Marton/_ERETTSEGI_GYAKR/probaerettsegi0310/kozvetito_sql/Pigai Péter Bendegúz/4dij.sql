select sum(hirdetes.ar*0.015)
from hirdetes
where hirdetes.allapot like "eladva" and hirdetes.datum like "2021%"
