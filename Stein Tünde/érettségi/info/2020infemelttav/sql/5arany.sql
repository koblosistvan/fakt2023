SELECT count(*) / (select count(*) from tag)
FROM tag
WHERE tag.nem = 'n';