select nev, count(nev) as autopalyak from telepules
where lcase(nev) not like "%budapest%"
group by nev
order by autopalyak desc
limit 1