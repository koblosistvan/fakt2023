SELECT nevado, kituzes FROM feladatsor
WHERE date_add(hatarido, INTERVAL 1 DAY) IN (
	SELECT kituzes FROM feladatsor
)