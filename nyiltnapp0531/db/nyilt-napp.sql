drop table if exists lessons;
create table lessons(
	id	int not null,
	room	varchar(255) not null,
	period	tinyint not null,
	start_time	varchar(255) not null,
	end_time	varchar(255) not null,
	subject		varchar(255) not null,
	teacher	varchar(255) not null,
	day		varchar(255) not null,
	class	varchar(255) not null,
	grade	int not null,
	student_group 	varchar(255) not null,
	level	varchar(255) not null,
	language	varchar(255),
	valid	bit not null default 1,
	last_upd	timestamp not null default now(),
	primary key (id)
	);
	
INSERT INTO 
lessons(id, room, period, start_time, end_time, subject, teacher, day, class, grade, student_group, level, language) 
VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]','[value-7]','[value-8]','[value-9]','[value-10]','[value-11]','[value-12]','[value-13]','[value-14]','[value-15]');

INSERT INTO 
lessons(id, room, period, start_time, end_time, subject, teacher, day, class, grade, student_group, level, language, deleted, last_upd) 
VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]','[value-7]','[value-8]','[value-9]','[value-10]','[value-11]','[value-12]','[value-13]','[value-14]','[value-15]');

INSERT INTO 
lessons(id, room, period, start_time, end_time, subject, teacher, day, class, grade, student_group, level, language, deleted, last_upd) 
VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]','[value-7]','[value-8]','[value-9]','[value-10]','[value-11]','[value-12]','[value-13]','[value-14]','[value-15]');

