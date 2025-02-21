SELECT COUNT(kapcsolat.keverekid) as mennyi
FROM kapcsolat JOIN osszetevo ON osszetevo.id = kapcsolat.osszetevoid
WHERE osszetevo.id = (SELECT osszetevo.id FROM osszetevo WHERE osszetevo.nev = "bazsalikom")