SELECT hely.vonalid, max(hely.tav) as tavolsag
from hely
GROUP BY hely.vonalid;