SELECT h.vonalid, MAX(h.tav)-MIN(h.tav) as hossz
FROM hely as h
GROUP BY h.vonalid;