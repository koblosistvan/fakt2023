select fenyid, evszam-szulev as eletkor, meret_x*meret_y as meret
from kapcsolo join fenykep on kapcsolo.fenyid = fenykep.id join szemely on kapcsolo.szemid = szemely.id
where nev = 'Vince'