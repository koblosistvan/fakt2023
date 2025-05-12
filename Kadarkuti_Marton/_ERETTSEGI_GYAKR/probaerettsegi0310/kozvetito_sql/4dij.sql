select sum(ar) * 0.015 as bevetel_millio
from hirdetes
where year(datum) = 2021 and allapot = "eladva"