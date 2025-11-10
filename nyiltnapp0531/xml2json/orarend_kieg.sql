INSERT INTO `lessons` (`id`, `room`, `period`, `start_time`, `end_time`, `subject`, `teacher`, `day`, `class`, `grade`, `student_group`, `level`, `language`, `valid`, `last_upd`) VALUES 
 (10002, 'Aula', 2, '9:05', '9:50', 'Robotika szakkör', 'Kiss István', '1', '7.A', 7, 'Egész osztály', 'alap', 'None', 1, now()), 

UPDATE `lessons` set `subject` = 'fizika' WHERE `day` = 1 and `period` = 3 and `teacher` = 'Kovács Ildikó';
UPDATE `lessons` set `room` = 'Z5' WHERE `day` = 1 and `period` = 2 and `teacher` = 'Németh Krisztina Júlia';
UPDATE `lessons` set `room` = 'Z1' WHERE `day` = 1 and `period` = 2 and `teacher` = 'Hegedűs-Kristóf Kíra';
UPDATE `lessons` set `subject` = 'irodalom' WHERE `day` = 1 and `period` = 2 and `teacher` = 'Maller Márta';
