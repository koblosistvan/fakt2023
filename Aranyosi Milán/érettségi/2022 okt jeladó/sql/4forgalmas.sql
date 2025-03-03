SELECT t.nev, count(*) as autopalyak_szama
FROM palya as p inner join telepules as t on t.ut=p.ut
where t.nev != 'Budapest'
group by t.nev  
ORDER BY count(*) DESC
limit 1;