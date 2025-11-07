SELECT p.ut, p.kesz
FROM palya as p inner join telepules as t on t.ut=p.ut inner join vege as v on v.ut = p.ut
where t.hatar = 'Szlovákia';