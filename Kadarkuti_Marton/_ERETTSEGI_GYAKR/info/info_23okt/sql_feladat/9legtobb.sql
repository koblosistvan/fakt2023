SELECT DISTINCT evfolyam, betujel, count(distinct szakazon) as szakkorok_szama FROM jelentkezes INNER JOIN diak ON diak.azon = jelentkezes.diakazon
GROUP BY evfolyam, betujel
ORDER BY szakkorok_szama DESC
LIMIT 1