select palya.ut, kesz
from palya inner join telepules on palya.ut = telepules.ut
where lcase(hatar) like "%szlovákia%"