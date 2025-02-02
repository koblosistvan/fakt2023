select vonalid, max(tav) as hossz
from hely
group by vonalid