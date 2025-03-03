select nev,tipus,terulet
from alloviz
where 
terulet between 3 and 10
and 
vizgyujto >= terulet*10