SELECT vonalid, MAX(tav) - MIN(tav) AS hossz
FROM hely
GROUP BY vonalid;
