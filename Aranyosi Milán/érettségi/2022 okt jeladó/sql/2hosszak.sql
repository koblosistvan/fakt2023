SELECT p.ut, (p.kesz+p.epul+p.terv) as teljes_hossz
FROM palya as p
order by teljes_hossz DESC;