select alloviz.nev, alloviz.terulet
FROM alloviz
where alloviz.tipus like '%morotva%'
order by alloviz.terulet DESC;