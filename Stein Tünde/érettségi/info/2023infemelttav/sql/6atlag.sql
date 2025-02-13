SELECT diak.nev, (SUM(24-hour(alvas.lefekves)) -SUM((60-minute(alvas.lefekves))/60) -SUM((60-second(alvas.lefekves))/3600) +SUM(hour(alvas.felkeles)) -SUM((60-minute(alvas.felkeles))/60) -SUM((60-second(alvas.felkeles))/3600) )/ (COUNT(alvas.lefekves)) as atlagos_alvasi_ido
FROM diak JOIN alvas ON alvas.diakid = diak.id
GROUP BY diak.nev
HAVING atlagos_alvasi_ido < 8;