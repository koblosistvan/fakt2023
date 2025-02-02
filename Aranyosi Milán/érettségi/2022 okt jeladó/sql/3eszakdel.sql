SELECT p.ut
FROM palya as p inner join europa as eu on eu.ut=p.ut
where eu.eurout LIKE 'E%5';