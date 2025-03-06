SELECT tag.nev, AVG((select tagsag.ev from tag where tagsag.tipus = 'r')-(select tagsag.ev from tag where tagsag.tipus = 'l'))
from tag
GROUP BY tag.id