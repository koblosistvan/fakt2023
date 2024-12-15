SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

DROP DATABASE IF EXISTS `szakkorok`;
CREATE TABLE `szakkorok`;
USE `szakkorok`;


CREATE TABLE `diak` (
  `azon` int(11) NOT NULL,
  `nev` varchar(255) DEFAULT NULL,
  `evfolyam` int(11) DEFAULT NULL,
  `betujel` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `jelentkezes` (
  `azon` int(11) NOT NULL,
  `diakazon` int(11) DEFAULT NULL,
  `szakazon` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `szakkor` (
  `azon` int(11) NOT NULL,
  `mk` varchar(255) DEFAULT NULL,
  `nev` varchar(255) DEFAULT NULL,
  `tanar` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO `diak` (`azon`, `nev`, `evfolyam`, `betujel`) VALUES
(1, 'Kis Lilla Laura', 11, 'D'),
(2, 'Hídvégi Antal', 11, 'B'),
(3, 'Illés Anna Noémi', 11, 'F'),
(4, 'Aszódi Anna', 10, 'B'),
(5, 'Aszódi Kitti', 7, 'A'),
(6, 'Adonyi Iringó', 10, 'A'),
(7, 'Kossa Barnabás', 11, 'B'),
(8, 'Füstös Zsófi', 10, 'B'),
(9, 'Tatay Eszter Anna', 11, 'E'),
(10, 'Keleti Viktória Lilla', 9, 'N'),
(11, 'Dede Anna Róza', 10, 'B'),
(12, 'Pintér Veronika', 9, 'E'),
(13, 'Borbély Antal', 9, 'B'),
(14, 'Sárdi Emma Krisztina', 10, 'E'),
(15, 'Moldvay Eszter', 9, 'N'),
(16, 'Beke Fanni', 11, 'E'),
(17, 'Bódy Judit', 10, 'E'),
(18, 'Olasz Réka', 11, 'D'),
(19, 'Kocsiss Ákos', 11, 'D'),
(20, 'Ujvári Botond Rudolf', 11, 'F'),
(21, 'Baross Angéla', 11, 'D'),
(22, 'Tóth Gábor Ábris', 11, 'B'),
(23, 'Tőke Csaba', 12, 'C'),
(24, 'Tétényi Orsolya Anna', 11, 'F'),
(25, 'Kovács Éva Réka', 12, 'A'),
(26, 'Vete Roland István', 12, 'D'),
(27, 'Kis Kinga Anna', 12, 'A'),
(28, 'Veti Milán', 12, 'A'),
(29, 'Piski Petra', 11, 'F'),
(30, 'Csűrös Panna', 12, 'A'),
(31, 'Bezerédi Heléna', 11, 'F'),
(32, 'Kis Csenge', 8, 'A'),
(33, 'Serédi Dorka', 8, 'A'),
(34, 'Nemesi Máté', 8, 'A'),
(35, 'Juhász Jónás', 8, 'A'),
(36, 'Tury Anna Klára', 8, 'A'),
(37, 'Piros Anikó', 8, 'A'),
(38, 'Márkus Andrea', 8, 'A'),
(39, 'Nagy Mátyás', 8, 'A'),
(40, 'Kiss Orsolya', 8, 'B'),
(41, 'Kiss Éva', 12, 'D'),
(42, 'Mátyus Bertalan', 12, 'D'),
(43, 'Szabadi Anna Luca', 12, 'B'),
(44, 'Tóth Zsófia', 12, 'D'),
(45, 'Rebak Lili', 12, 'B'),
(46, 'Márton Bence', 12, 'B'),
(47, 'Hajdú Viola Erzsébet', 12, 'C'),
(48, 'Bene Borbála', 12, 'B'),
(49, 'Vete Gréta', 12, 'D'),
(50, 'Széki Dorka', 12, 'D'),
(51, 'Vete Kinga', 12, 'B'),
(52, 'Balogh Eszter', 12, 'B'),
(53, 'Dede Áron Andrea', 12, 'B'),
(54, 'Dana Éva', 12, 'D'),
(55, 'Ada Zsófia Zsuzsanna', 12, 'D'),
(56, 'Tóti Anna Vilma', 12, 'D'),
(57, 'Nagy Réka Lilla', 12, 'B'),
(58, 'Papp Bálint Kende', 12, 'B'),
(59, 'Őry Boglárka', 12, 'D'),
(60, 'Tamás Dániel', 9, 'D'),
(61, 'Kovács Bálint', 9, 'A'),
(62, 'Szén Lili', 9, 'D'),
(63, 'Molnár Máté Bendegúz', 9, 'D'),
(64, 'Cseh Natália', 10, 'D'),
(65, 'Nagy Dániel Gábor', 9, 'D'),
(66, 'Veréb Nóra Emília', 9, 'D'),
(67, 'Derék Szilvia Boglárka', 10, 'C'),
(68, 'Vörös Rebeka Anna', 9, 'D'),
(69, 'Danka Balázs', 9, 'D'),
(70, 'Papp Noémi Orsolya', 9, 'D'),
(71, 'Gara Artúr Géza', 9, 'A'),
(72, 'Korándi Laura', 8, 'B'),
(73, 'Lévai András László', 8, 'A'),
(74, 'Ábel Félix', 8, 'B'),
(75, 'Lengyel Szabolcs', 8, 'A'),
(76, 'Budai Ádám András', 8, 'A'),
(77, 'Halász Tamás András', 8, 'A'),
(78, 'Nagy Zsombor Zoltán', 8, 'B'),
(79, 'Lampé Szabolcs Ákos', 8, 'A'),
(80, 'Molnár Zsombor', 8, 'A'),
(81, 'Máté Dániel Erik', 8, 'B'),
(82, 'Pap Marcell', 8, 'B'),
(83, 'Fecske László Márton', 8, 'A'),
(84, 'Simon András Márk', 8, 'B'),
(85, 'Györgyi Péter', 8, 'A'),
(86, 'Surányi Gergő Márton', 8, 'B'),
(87, 'Bíró Dávid', 8, 'B'),
(88, 'Sás Bernát', 8, 'A'),
(89, 'Sas Lili Anna', 11, 'E'),
(90, 'Garami Panna', 12, 'A'),
(91, 'Újhelyi Zita', 12, 'A'),
(92, 'Bende Soma Tamás', 11, 'E'),
(93, 'Kolonics András', 12, 'A'),
(94, 'Péti Ilona Sára', 11, 'C'),
(95, 'Csiba Krisztina Terézia', 12, 'E'),
(96, 'Vete Laura Jelica', 11, 'F'),
(97, 'Pintér Zsófia', 12, 'E'),
(98, 'Gábos Flóra Anna', 11, 'D'),
(99, 'Szabó Bernadett Viktória', 12, 'E'),
(100, 'Némedi Dóra', 12, 'E'),
(101, 'Takács András', 11, 'F'),
(102, 'Pogány Lilla', 12, 'E'),
(103, 'Ballai Emma', 11, 'E'),
(104, 'Babos Éva', 12, 'E'),
(105, 'Schmitt Petra', 11, 'E'),
(106, 'Vivien Noémi', 11, 'E'),
(107, 'Bornemissza Réka', 11, 'E'),
(108, 'Prókai Áron István', 11, 'E'),
(109, 'Széki Levente', 11, 'E'),
(110, 'Katona Dániel', 12, 'C'),
(111, 'Szabó Andrea', 11, 'B'),
(112, 'Szabó István', 11, 'A'),
(113, 'Vete Pál Patrik', 12, 'C'),
(114, 'Halasi Tamás', 12, 'C'),
(115, 'Goda Ádám Gyula', 12, 'C'),
(116, 'Vécsey Roland', 11, 'A'),
(117, 'Teréki Barnabás', 12, 'C'),
(118, 'Olasz Marcell', 11, 'B'),
(119, 'Zora Doma Bence', 11, 'A'),
(120, 'Bedő Botond', 12, 'A'),
(121, 'Salántay Adrián Tamás', 12, 'E'),
(122, 'Ember Attila József', 11, 'B'),
(123, 'Kalla Gábor', 11, 'D'),
(124, 'Perényi Anita Csenge', 11, 'C'),
(125, 'Csaba Márton', 10, 'B'),
(126, 'Réti Mihály', 11, 'D'),
(127, 'Hegedűs Andrea', 9, 'B'),
(128, 'Molnár Ivett Luca', 9, 'N'),
(129, 'Szabó Eszter', 9, 'N'),
(130, 'Soós Andrea', 9, 'C'),
(131, 'Szakács Márton László', 9, 'D'),
(132, 'Olasz Viktória', 9, 'A'),
(133, 'Szele Attila Vilmos', 9, 'D'),
(134, 'Helga Adél', 9, 'B'),
(135, 'Pere Attila Csaba', 9, 'D'),
(136, 'Szűcs Adél Judit', 9, 'D'),
(137, 'Dél Áron Balázs', 9, 'D'),
(138, 'Kabai Enikő', 9, 'D'),
(139, 'Akartó Domonkos', 9, 'B'),
(140, 'Deme Melinda', 11, 'E'),
(141, 'Szász Anna', 11, 'B'),
(142, 'Molnár András', 7, 'B'),
(143, 'Fonay Emma', 9, 'C'),
(144, 'Sági Anna', 9, 'C'),
(145, 'Érdi Marcell', 8, 'B'),
(146, 'Sebe Péter Ábel', 10, 'F'),
(147, 'Pintér Johanna Réka', 7, 'B'),
(148, 'Lakat András', 7, 'B'),
(149, 'Létay Dániel', 10, 'E'),
(150, 'Ózdi Vince', 9, 'C'),
(151, 'Koppány Zétény', 9, 'F'),
(152, 'Szerdei Marcell', 10, 'C'),
(153, 'Dobó Kinga', 9, 'C'),
(154, 'Kerék Levente Bán', 9, 'C'),
(155, 'Végh Levente', 10, 'D'),
(156, 'Vete Villő Eleonóra', 9, 'F'),
(157, 'Téli Patrik Zoltán', 10, 'D'),
(158, 'Szabó Lilla', 9, 'F'),
(159, 'Kandó Áron', 7, 'B'),
(160, 'Dóri Patrik', 7, 'B'),
(161, 'Darabont Andrea', 9, 'C'),
(162, 'Hegedüs-Pékó Dóra', 9, 'F'),
(163, 'Bor András Márton', 9, 'D'),
(164, 'Bérdy Máté', 10, 'C'),
(165, 'Borbély Judit', 9, 'N'),
(166, 'Bab Balázs', 11, 'C'),
(167, 'Gerai Róza', 7, 'B'),
(168, 'Hetei Dániel', 7, 'A'),
(169, 'Tóth Dániel Márk', 7, 'A'),
(170, 'Kesztyűs Panna', 9, 'C'),
(171, 'Szőcs Barnabás', 9, 'D'),
(172, 'Magyar Mátyás', 7, 'A'),
(173, 'Róka Károly', 7, 'A'),
(174, 'Radó Márton', 7, 'A'),
(175, 'Baranyi Márton', 9, 'C'),
(176, 'Gera Balázs', 7, 'A'),
(177, 'Vete Ákos Gábor', 9, 'B'),
(178, 'Zada Levente', 9, 'C'),
(179, 'Luca Gabriel', 9, 'D'),
(180, 'Léti András', 7, 'B'),
(181, 'Hunor Olivér', 7, 'A'),
(182, 'Kóka András Balázs', 9, 'C'),
(183, 'Rozina Antal', 10, 'A'),
(184, 'Toma Mátyás János', 9, 'N'),
(185, 'Pesti Tamás János', 9, 'A'),
(186, 'Csonka Dóra', 9, 'C'),
(187, 'Hajdu Bence', 9, 'C'),
(188, 'Népi Ákos', 7, 'A'),
(189, 'Vörös Balázs', 9, 'A'),
(190, 'Népi Máté', 9, 'C'),
(191, 'Tétényi Dániel', 7, 'B'),
(192, 'Lengyel Dániel', 7, 'A'),
(193, 'Szabó Roland', 9, 'N'),
(194, 'Benke Roland', 7, 'B'),
(195, 'Bárdy Dávid', 7, 'B'),
(196, 'Line Benjamin Woodbridge', 9, 'N'),
(197, 'Jenei László', 9, 'B'),
(198, 'Györgyi Donát Móric', 9, 'N'),
(199, 'Gerai Márton', 11, 'A'),
(200, 'Vörös Máté', 11, 'C'),
(201, 'Török Csongor', 11, 'C'),
(202, 'Csoók Áron', 9, 'C'),
(203, 'Szabolcs Ádám', 10, 'D'),
(204, 'Baka Zoltán', 11, 'E'),
(205, 'Tinódi Lili', 10, 'B'),
(206, 'Dere Domonkos Márk', 10, 'B'),
(207, 'Gara Kristóf Ágoston', 12, 'A'),
(208, 'Nóra Noémi', 11, 'A'),
(209, 'Magyar Máté', 9, 'F'),
(210, 'Vete Tünde Szamóca', 10, 'D'),
(211, 'Soltész Andrea', 10, 'F'),
(212, 'Szabó Zsófia', 10, 'D'),
(213, 'Nagy Borbála', 9, 'F'),
(214, 'Antal Benő', 7, 'A'),
(215, 'Hajbó Sára', 8, 'B'),
(216, 'Létay Jázmin', 7, 'A'),
(217, 'Dere Endre', 9, 'B'),
(218, 'Nagy Eszter Hajnalka', 10, 'D'),
(219, 'Zsády Veronika', 9, 'N'),
(220, 'Mala Dorottya', 9, 'N'),
(221, 'Gazsó Emma', 9, 'F'),
(222, 'Fehér Csenge', 8, 'A'),
(223, 'Tas Péter Marcell', 8, 'A'),
(224, 'Kis Máté Levente', 8, 'B'),
(225, 'Haba Klára Katalin', 8, 'A'),
(226, 'Balog Marcell', 8, 'B'),
(227, 'Érdi Gergely', 10, 'B'),
(228, 'Nagy Eszter', 10, 'D'),
(229, 'Szalai Liza', 12, 'A'),
(230, 'Sásdi Virág', 10, 'C'),
(231, 'Ózdi Hanna', 10, 'D'),
(232, 'Nagy Dorottya Sára', 10, 'C'),
(233, 'Lovász Laura', 10, 'C'),
(234, 'Raday Barnabás', 10, 'C'),
(235, 'Ferke Tamás Miklós', 10, 'A'),
(236, 'Mészáros Anna', 10, 'C'),
(237, 'Vete Máté', 7, 'B'),
(238, 'Horváth Milán Zoltán', 7, 'A'),
(239, 'Bazsa Eszter', 7, 'A'),
(240, 'Baráth Réka Barbara', 7, 'A'),
(241, 'Mónos Gergely', 7, 'A'),
(242, 'Mészáros Marcell', 7, 'A'),
(243, 'Égi Réka Luca', 7, 'A'),
(244, 'Balog Adél', 7, 'A'),
(245, 'Aradi Anna', 7, 'A'),
(246, 'Jenei Zita', 7, 'A'),
(247, 'Lovász Aliz', 7, 'B'),
(248, 'Vettel Naómi', 7, 'A'),
(249, 'Nagy Hanna', 7, 'A'),
(250, 'Mészáros Dorottya', 9, 'E'),
(251, 'Kende Réka', 9, 'E'),
(252, 'Debreceni Domonkos', 9, 'E'),
(253, 'Bárdy Márk Martin', 9, 'E'),
(254, 'Teréki Balázs Máté', 9, 'E'),
(255, 'Vince Zsigmond', 9, 'E'),
(256, 'Fóti Benő', 9, 'E'),
(257, 'Darabos Balázs', 9, 'E'),
(258, 'Sas Emma', 9, 'E'),
(259, 'Halász Martin Dávid', 9, 'E'),
(260, 'Nánay Boglárka', 9, 'C'),
(261, 'Nagy Péter', 9, 'C'),
(262, 'Bíró Andrea', 9, 'C'),
(263, 'Béri Lívia', 9, 'C'),
(264, 'Hegedűs Enikő', 9, 'C'),
(265, 'Roba Dóra', 9, 'C'),
(266, 'Daday Dániel', 9, 'C'),
(267, 'Halász Eszter', 9, 'C'),
(268, 'Rab Márton', 9, 'C'),
(269, 'Nánay Barnabás', 9, 'C'),
(270, 'Bán Sára', 11, 'B'),
(271, 'Gara Rozina', 7, 'B'),
(272, 'Kovács Petra', 7, 'B'),
(273, 'Kiss Lilla Flóra', 7, 'B'),
(274, 'Ballay Beáta', 10, 'B'),
(275, 'Ostor Janka', 9, 'A'),
(276, 'Fás Eszter', 9, 'E'),
(277, 'Vesze Lea', 7, 'B'),
(278, 'Gara Benő', 9, 'B'),
(279, 'Fekete Borbála', 9, 'B'),
(280, 'Márta Bálint', 10, 'C'),
(281, 'Csécsi Villő', 10, 'F'),
(282, 'Rátóti Vencel Rudolf', 10, 'B'),
(283, 'Perpi Hanna', 8, 'B'),
(284, 'Menyhért Flóra Lujza', 8, 'A'),
(285, 'Szegedi Eszter', 7, 'A'),
(286, 'Gáspár Lili', 9, 'B'),
(287, 'Hanna Flóra', 11, 'B'),
(288, 'Hegedűs Dóra', 7, 'B'),
(289, 'Győri Lia Miriam', 9, 'E'),
(290, 'Bécsi Andrea József', 11, 'C'),
(291, 'Banas Szonja', 7, 'B'),
(292, 'Kovács Lili', 11, 'B'),
(293, 'Kirschner Virág Lili', 9, 'D'),
(294, 'Kalocsai Judit Eszter', 11, 'C'),
(295, 'Tóth Zsófia', 11, 'C'),
(296, 'Csabai Nóra', 10, 'E'),
(297, 'Vete Laura Szófia', 9, 'N'),
(298, 'Biró Veronika', 9, 'F'),
(299, 'Mányai Izabella', 7, 'B'),
(300, 'Égi Hanna Imola', 8, 'A'),
(301, 'Koltai Dóra', 10, 'C'),
(302, 'Béres Kata', 7, 'A'),
(303, 'Léki Fruzsina', 12, 'A'),
(304, 'Merész Balázs Dániel', 12, 'A'),
(305, 'Halász Ákos Miklós', 8, 'B'),
(306, 'Mihályi Bence', 8, 'B'),
(307, 'Andocsi Brúnó', 9, 'A');


INSERT INTO `jelentkezes` (`azon`, `diakazon`, `szakazon`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 1),
(4, 4, 1),
(5, 5, 1),
(6, 6, 1),
(7, 7, 2),
(8, 8, 2),
(9, 9, 2),
(10, 10, 2),
(11, 11, 2),
(12, 12, 2),
(13, 13, 2),
(14, 14, 2),
(15, 15, 2),
(16, 16, 2),
(17, 4, 2),
(18, 17, 2),
(19, 18, 3),
(20, 19, 3),
(21, 20, 3),
(22, 21, 3),
(23, 22, 3),
(24, 23, 3),
(25, 24, 3),
(26, 25, 3),
(27, 26, 3),
(28, 7, 4),
(29, 27, 4),
(30, 28, 4),
(31, 29, 4),
(32, 30, 4),
(33, 31, 4),
(34, 32, 5),
(35, 33, 5),
(36, 34, 5),
(37, 35, 5),
(38, 36, 5),
(39, 37, 5),
(40, 38, 5),
(41, 39, 5),
(42, 40, 5),
(43, 41, 6),
(44, 42, 6),
(45, 43, 6),
(46, 44, 6),
(47, 45, 6),
(48, 46, 6),
(49, 47, 6),
(50, 48, 6),
(51, 49, 6),
(52, 50, 6),
(53, 51, 6),
(54, 52, 6),
(55, 53, 6),
(56, 54, 6),
(57, 55, 6),
(58, 56, 6),
(59, 57, 6),
(60, 26, 6),
(61, 58, 6),
(62, 59, 6),
(63, 41, 7),
(64, 43, 7),
(65, 44, 7),
(66, 45, 7),
(67, 46, 7),
(68, 47, 7),
(69, 48, 7),
(70, 49, 7),
(71, 50, 7),
(72, 51, 7),
(73, 52, 7),
(74, 53, 7),
(75, 54, 7),
(76, 55, 7),
(77, 56, 7),
(78, 57, 7),
(79, 26, 7),
(80, 58, 7),
(81, 59, 7),
(82, 60, 8),
(83, 8, 8),
(84, 61, 8),
(85, 62, 8),
(86, 63, 8),
(87, 64, 8),
(88, 65, 8),
(89, 66, 8),
(90, 67, 8),
(91, 68, 8),
(92, 69, 8),
(93, 70, 8),
(94, 71, 8),
(95, 72, 9),
(96, 73, 9),
(97, 74, 9),
(98, 75, 9),
(99, 76, 9),
(100, 77, 9),
(101, 78, 9),
(102, 79, 9),
(103, 80, 9),
(104, 81, 9),
(105, 36, 9),
(106, 82, 9),
(107, 83, 9),
(108, 38, 9),
(109, 84, 9),
(110, 85, 9),
(111, 86, 9),
(112, 87, 9),
(113, 88, 9),
(114, 89, 10),
(115, 90, 10),
(116, 1, 10),
(117, 91, 10),
(118, 92, 10),
(119, 93, 10),
(120, 94, 10),
(121, 95, 10),
(122, 96, 10),
(123, 97, 10),
(124, 98, 10),
(125, 99, 10),
(126, 9, 10),
(127, 100, 10),
(128, 101, 10),
(129, 102, 10),
(130, 103, 10),
(131, 104, 10),
(132, 105, 10),
(133, 106, 10),
(134, 107, 10),
(135, 108, 10),
(136, 16, 10),
(137, 109, 10),
(138, 110, 11),
(139, 111, 11),
(140, 112, 11),
(141, 76, 11),
(142, 113, 11),
(143, 114, 11),
(144, 115, 11),
(145, 116, 11),
(146, 117, 11),
(147, 118, 11),
(148, 119, 11),
(149, 120, 11),
(150, 121, 11),
(151, 122, 11),
(152, 123, 11),
(153, 124, 11),
(154, 125, 11),
(155, 126, 11),
(156, 17, 11),
(157, 127, 12),
(158, 128, 12),
(159, 129, 12),
(160, 130, 12),
(161, 131, 12),
(162, 132, 12),
(163, 133, 12),
(164, 66, 12),
(165, 134, 12),
(166, 135, 12),
(167, 136, 12),
(168, 137, 12),
(169, 138, 12),
(170, 139, 12),
(171, 140, 13),
(172, 141, 13),
(173, 76, 14),
(174, 142, 15),
(175, 143, 15),
(176, 144, 15),
(177, 145, 15),
(178, 146, 15),
(179, 147, 15),
(180, 148, 15),
(181, 149, 15),
(182, 80, 15),
(183, 150, 15),
(184, 151, 15),
(185, 152, 15),
(186, 153, 15),
(187, 154, 15),
(188, 155, 15),
(189, 156, 15),
(190, 157, 15),
(191, 158, 15),
(192, 159, 15),
(193, 160, 15),
(194, 65, 15),
(195, 161, 15),
(196, 162, 15),
(197, 163, 15),
(198, 14, 15),
(199, 164, 15),
(200, 150, 16),
(201, 61, 16),
(202, 165, 16),
(203, 166, 17),
(204, 167, 18),
(205, 168, 18),
(206, 142, 18),
(207, 169, 18),
(208, 170, 18),
(209, 171, 18),
(210, 143, 18),
(211, 172, 18),
(212, 173, 18),
(213, 174, 18),
(214, 175, 18),
(215, 148, 18),
(216, 176, 18),
(217, 76, 18),
(218, 177, 18),
(219, 128, 18),
(220, 178, 18),
(221, 129, 18),
(222, 179, 18),
(223, 34, 18),
(224, 180, 18),
(225, 81, 18),
(226, 150, 18),
(227, 181, 18),
(228, 182, 18),
(229, 35, 18),
(230, 183, 19),
(231, 170, 19),
(232, 173, 19),
(233, 184, 19),
(234, 60, 19),
(235, 185, 19),
(236, 186, 19),
(237, 187, 19),
(238, 181, 19),
(239, 182, 19),
(240, 188, 19),
(241, 189, 19),
(242, 190, 19),
(243, 191, 19),
(244, 192, 19),
(245, 193, 19),
(246, 194, 19),
(247, 69, 19),
(248, 137, 19),
(249, 195, 19),
(250, 196, 19),
(251, 197, 20),
(252, 184, 20),
(253, 185, 20),
(254, 198, 20),
(255, 127, 20),
(256, 187, 20),
(257, 130, 20),
(258, 199, 20),
(259, 193, 20),
(260, 200, 20),
(261, 201, 20),
(262, 202, 20),
(263, 203, 20),
(264, 204, 20),
(265, 1, 21),
(266, 146, 21),
(267, 93, 21),
(268, 27, 21),
(269, 205, 21),
(270, 206, 21),
(271, 55, 21),
(272, 28, 21),
(273, 24, 21),
(274, 207, 21),
(275, 208, 21),
(276, 209, 22),
(277, 114, 22),
(278, 127, 22),
(279, 210, 22),
(280, 211, 22),
(281, 212, 22),
(282, 213, 22),
(283, 214, 22),
(284, 35, 22),
(285, 215, 22),
(286, 216, 22),
(287, 217, 22),
(288, 218, 22),
(289, 159, 22),
(290, 163, 22),
(291, 219, 22),
(292, 220, 22),
(293, 221, 22),
(294, 4, 22),
(295, 88, 22),
(296, 6, 22),
(297, 73, 23),
(298, 75, 23),
(299, 76, 23),
(300, 77, 23),
(301, 33, 23),
(302, 79, 23),
(303, 80, 23),
(304, 36, 23),
(305, 37, 23),
(306, 83, 23),
(307, 38, 23),
(308, 39, 23),
(309, 222, 23),
(310, 223, 23),
(311, 224, 23),
(312, 85, 23),
(313, 225, 23),
(314, 226, 23),
(315, 130, 24),
(316, 227, 24),
(317, 228, 24),
(318, 125, 24),
(319, 110, 25),
(320, 229, 25),
(321, 113, 25),
(322, 114, 25),
(323, 115, 25),
(324, 52, 25),
(325, 120, 25),
(326, 24, 25),
(327, 207, 25),
(328, 183, 26),
(329, 230, 26),
(330, 210, 26),
(331, 231, 26),
(332, 232, 26),
(333, 67, 26),
(334, 233, 26),
(335, 234, 26),
(336, 235, 26),
(337, 236, 26),
(338, 237, 27),
(339, 167, 27),
(340, 168, 27),
(341, 142, 27),
(342, 169, 27),
(343, 238, 27),
(344, 173, 27),
(345, 174, 27),
(346, 148, 27),
(347, 176, 27),
(348, 239, 27),
(349, 240, 27),
(350, 180, 27),
(351, 214, 27),
(352, 188, 27),
(353, 241, 27),
(354, 242, 27),
(355, 243, 27),
(356, 244, 27),
(357, 192, 27),
(358, 245, 27),
(359, 246, 27),
(360, 247, 27),
(361, 160, 27),
(362, 248, 27),
(363, 249, 27),
(364, 250, 28),
(365, 251, 28),
(366, 252, 28),
(367, 253, 28),
(368, 254, 28),
(369, 255, 28),
(370, 256, 28),
(371, 257, 28),
(372, 182, 28),
(373, 161, 28),
(374, 258, 28),
(375, 259, 28),
(376, 60, 29),
(377, 179, 29),
(378, 130, 29),
(379, 182, 29),
(380, 143, 30),
(381, 144, 30),
(382, 260, 30),
(383, 186, 30),
(384, 261, 30),
(385, 130, 30),
(386, 150, 30),
(387, 262, 30),
(388, 263, 30),
(389, 190, 30),
(390, 153, 30),
(391, 264, 30),
(392, 193, 30),
(393, 265, 30),
(394, 266, 30),
(395, 134, 30),
(396, 202, 30),
(397, 267, 30),
(398, 268, 30),
(399, 269, 30),
(400, 139, 30),
(401, 111, 31),
(402, 112, 31),
(403, 116, 31),
(404, 118, 31),
(405, 199, 31),
(406, 22, 31),
(407, 122, 31),
(408, 124, 31),
(409, 270, 31),
(410, 271, 32),
(411, 142, 32),
(412, 251, 32),
(413, 230, 32),
(414, 272, 32),
(415, 147, 32),
(416, 114, 32),
(417, 273, 32),
(418, 216, 32),
(419, 217, 32),
(420, 264, 32),
(421, 218, 32),
(422, 274, 32),
(423, 13, 32),
(424, 275, 32),
(425, 276, 32),
(426, 277, 32),
(427, 58, 32),
(428, 278, 33),
(429, 279, 33),
(430, 167, 33),
(431, 280, 33),
(432, 271, 33),
(433, 168, 33),
(434, 251, 33),
(435, 281, 33),
(436, 282, 33),
(437, 283, 33),
(438, 230, 33),
(439, 284, 33),
(440, 239, 33),
(441, 76, 33),
(442, 285, 33),
(443, 127, 33),
(444, 33, 33),
(445, 286, 33),
(446, 287, 33),
(447, 288, 33),
(448, 289, 33),
(449, 290, 33),
(450, 243, 33),
(451, 82, 33),
(452, 291, 33),
(453, 21, 33),
(454, 292, 34),
(455, 130, 34),
(456, 289, 34),
(457, 150, 34),
(458, 9, 34),
(459, 293, 34),
(460, 115, 35),
(461, 294, 35),
(462, 44, 35),
(463, 260, 36),
(464, 296, 36),
(465, 297, 36),
(466, 167, 37),
(467, 298, 37),
(468, 260, 37),
(469, 33, 37),
(470, 299, 37),
(471, 300, 37),
(472, 132, 37),
(473, 247, 37),
(474, 248, 37),
(475, 161, 37),
(476, 40, 37),
(477, 233, 37),
(478, 301, 37),
(479, 136, 37),
(480, 24, 37),
(481, 302, 37),
(482, 28, 38),
(483, 303, 38),
(484, 25, 38),
(485, 304, 38),
(486, 145, 39),
(487, 74, 39),
(488, 305, 39),
(489, 81, 39),
(490, 306, 39),
(491, 89, 40),
(492, 307, 40);

INSERT INTO `szakkor` (`azon`, `mk`, `nev`, `tanar`) VALUES
(1, '2. idegen nyelv', 'Franciaszakkör', 'Marosi Norbert'),
(2, '2. idegen nyelv', 'Kezdő latin', 'Jeney Flóra'),
(3, '2. idegen nyelv', 'Latinérettségi-előkészítő', 'Jeney Flóra'),
(4, '2. idegen nyelv', 'Olasz beszédgyakorlat', 'Veleméri Melinda'),
(5, '2. idegen nyelv', 'Spanyol kultúrföldrajz', 'Bor Nóra'),
(6, 'Biológia - Kémia', 'Biológia 12. fakt kiegészítő', 'Simon Miklós'),
(7, 'Biológia - Kémia', 'Biológia OKTV-felkészítő', 'Simon Miklós'),
(8, 'Biológia - Kémia', 'Ötösöm lesz biokémiából', 'Keszei István'),
(9, 'Biológia - Kémia', 'Kémia kísérletezős, tehetséggondozó', 'Kovács Zita'),
(10, 'Biológia - Kémia', 'OKTV-re/emelt érettségire felkészítő', 'Hajdú Viktória'),
(11, 'Fizika', 'Fizikafeladat-megoldó', 'Bene Balázs'),
(12, 'Fizika', 'Kísérletezős, versenyfelkészítő szakkör', 'Juhász Erzsébet'),
(13, 'Földrajz - Társadalomismeret', 'Földrajzérettségi-előkészítő', 'Koma László'),
(14, 'Földrajz - Társadalomismeret', 'Földrajz OKTV-felkészítő', 'Szemesi József'),
(15, 'Földrajz - Társadalomismeret', 'Geopolitika', 'Pogács Balázs'),
(16, 'Földrajz - Társadalomismeret', 'Lóczy Lajos versenyre felkészítő szakkör', 'Rónai Csongor'),
(17, 'Informatika - Digitális kultúra', 'Érettségire készítő konzultáció - középszint', 'Nagy Ervin'),
(18, 'Informatika - Digitális kultúra', 'Kezdő programozás', 'Kovács Tamás'),
(19, 'Informatika - Digitális kultúra', 'Kreatív ROBOTIKA', 'Ménesi József'),
(20, 'Informatika - Digitális kultúra', 'Programozás - haladó', 'Kovács Tamás'),
(21, 'Magyar nyelv és irodalom', 'Filozófia', 'Lakatos Péter'),
(22, 'Magyar nyelv és irodalom', 'Színjátszó', 'Sásdi Antal'),
(23, 'Matematika', '8. osztályos érdeklődő szakkör', 'Bor Attila'),
(24, 'Matematika', 'Arany Dániel matematikaszakkör', 'Fekete Péter'),
(25, 'Matematika', 'Matematika a 12. évfolyamnak', 'Bor Attila'),
(26, 'Matematika', 'Matematikafeladat-megoldó szakkör', 'Deák Zsolt'),
(27, 'Matematika', 'Matematika szakkör', 'Székely Áron'),
(28, 'Matematika', 'Matematika szakkör 9.-eseknek', 'Bor Attila'),
(29, 'Matematika', 'Matematikaverseny-előkészítő', 'Balogh Bertalan'),
(30, 'Matematika', 'Matematikaversenyfeladat-megoldó szakkör', 'Zsurzs Veronika'),
(31, 'Matematika', 'Matematika VFő és TGó szakkör', 'Helyei Adrienn'),
(32, 'Művészetek', 'Énekkar', 'Dobos Antal'),
(33, 'Művészetek', 'Rajzszakkör', 'Keszi Péter'),
(34, 'Német nyelv', 'Felzárkóztató szakkör német nyelvből', 'Nagy Viktória'),
(35, 'Német nyelv', 'Német nyelv OKTV-felkészítő', 'Nagy Viktória'),
(36, 'Német nyelv', 'Német nyelvű iskolaújság szerkesztése', 'Téli Judit'),
(37, 'Testnevelés', 'Lány kosárlabda', 'Tóth Fülöp'),
(38, 'Történelem', 'Emelt szintű érettségire előkészítő szakkör', 'Hegedűs András'),
(39, 'Történelem', 'Kosáry történelemversenyre felkészítés', 'Vete Zoltán'),
(40, 'Történelem', 'Versenyfelkészítő szakkör', 'Kis Attila');

ALTER TABLE `diak`
  ADD PRIMARY KEY (`azon`);

ALTER TABLE `jelentkezes`
  ADD PRIMARY KEY (`azon`);

ALTER TABLE `szakkor`
  ADD PRIMARY KEY (`azon`);

COMMIT;
