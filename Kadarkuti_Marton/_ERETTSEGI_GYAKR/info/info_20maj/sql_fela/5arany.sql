select count(*) / (select count(*) from tag) as arany
from tag
where nem = 'n'