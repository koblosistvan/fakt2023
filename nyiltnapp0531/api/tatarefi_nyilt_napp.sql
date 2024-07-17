-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Gép: localhost:3306
-- Létrehozás ideje: 2024. Júl 17. 14:53
-- Kiszolgáló verziója: 10.6.18-MariaDB
-- PHP verzió: 8.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `tatarefi_nyilt_napp`
--

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `lessons`
--

CREATE TABLE `lessons` (
  `id` int(11) NOT NULL,
  `room` varchar(255) NOT NULL,
  `period` tinyint(4) NOT NULL,
  `start_time` varchar(255) NOT NULL,
  `end_time` varchar(255) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `teacher` varchar(255) NOT NULL,
  `day` varchar(255) NOT NULL,
  `class` varchar(255) NOT NULL,
  `grade` int(11) NOT NULL,
  `student_group` varchar(255) NOT NULL,
  `level` varchar(255) NOT NULL,
  `language` varchar(255) DEFAULT NULL,
  `valid` bit(1) NOT NULL DEFAULT b'1',
  `last_upd` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- A tábla adatainak kiíratása `lessons`
--

INSERT INTO `lessons` (`id`, `room`, `period`, `start_time`, `end_time`, `subject`, `teacher`, `day`, `class`, `grade`, `student_group`, `level`, `language`, `valid`, `last_upd`) VALUES
(5, 'Z3', 6, '12:50', '13:35', 'Ének', 'Györkéné Gulyás Orsolya', 'Csütörtök', '12.B', 12, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:36:18'),
(6, 'Z1', 6, '12:50', '13:35', 'Vizuális kultúra', 'Aladzsits Szilvia', 'Csütörtök', '11.A', 11, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:36:18'),
(10, 'Z3', 4, '11:00', '11:45', 'Ének', 'Györkéné Gulyás Orsolya', 'Csütörtök', '10.C', 10, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:36:18'),
(12, 'Z4', 3, '10:05', '10:50', 'Orosz nyelv', 'Kerényi Gabriella', 'Csütörtök', '[List]', 9, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:36:18'),
(19, 'Z4', 5, '11:55', '12:40', 'Orosz nyelv', 'Kerényi Gabriella', 'Csütörtök', '[List]', 11, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:36:18'),
(25, '27', 4, '11:00', '11:45', 'Francia nyelv', 'Temesi Tímea', 'Csütörtök', '[List]', 12, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(27, '17', 2, '9:05', '9:50', 'Katolikus hittan', 'Havassy Bálint', 'Csütörtök', '10.C', 10, 'Kat', 'alap', '', b'1', '2024-07-16 09:33:18'),
(30, 'Z4', 4, '11:00', '11:45', 'Orosz nyelv', 'Kerényi Gabriella', 'Csütörtök', '[List]', 12, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(34, '14', 7, '14:00', '14:45', 'Francia nyelv', 'Temesi Tímea', 'Csütörtök', '[List]', 10, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(40, '5', 4, '11:00', '11:45', 'Digitális Kultúra', 'Kiss István', 'Csütörtök', '9.B', 9, '1. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(42, '5', 6, '12:50', '13:35', 'Digitális Kultúra', 'Kiss István', 'Csütörtök', '9.B', 9, '2. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(58, 'T2', 4, '11:00', '11:45', 'Technika', 'Szurcsik Gyöngyvér', 'Csütörtök', '10.A', 10, 'Lány', 'alap', '', b'1', '2024-07-16 09:33:18'),
(61, 'T1', 4, '11:00', '11:45', 'Technika', 'Gál Zoltán', 'Csütörtök', '10.A', 10, 'Fiú', 'alap', '', b'1', '2024-07-16 09:33:18'),
(63, 'T2', 8, '14:50', '15:35', 'Technika', 'Basky Péter', 'Csütörtök', '12.B', 12, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(67, '1', 3, '10:05', '10:50', 'Francia nyelv', 'Temesi Tímea', 'Csütörtök', '[List]', 9, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(70, 'Z1', 5, '11:55', '12:40', 'Francia nyelv', 'Temesi Tímea', 'Csütörtök', '[List]', 11, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(74, '1', 5, '11:55', '12:40', 'Református hittan', 'Nagy Péterné', 'Csütörtök', '8.A', 8, 'Ref', 'alap', '', b'1', '2024-07-16 09:33:18'),
(79, 'K2', 5, '11:55', '12:40', 'Irodalom', 'Györkéné Gulyás Orsolya', 'Csütörtök', '9.C', 9, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(90, '21', 4, '11:00', '11:45', 'Irodalom', 'Zahoránné Pavelka Ildikó', 'Csütörtök', '11.B', 11, 'Magyar alap', 'alap', '', b'1', '2024-07-16 09:33:18'),
(95, 'T3', 4, '11:00', '11:45', 'Irodalom', 'Maller Márta', 'Csütörtök', '11.C', 11, 'Magyar alap', 'alap', '', b'1', '2024-07-16 09:33:18'),
(97, '17', 3, '10:05', '10:50', 'Irodalom', 'Gálné Bagdán Eszter', 'Csütörtök', '[List]', 11, '[List]', 'emelt', '', b'1', '2024-07-16 09:33:18'),
(103, '7', 4, '11:00', '11:45', 'Irodalom', 'Geiszelhardt Zsófia', 'Csütörtök', '11.A', 11, 'Magyar alap', 'alap', '', b'1', '2024-07-16 09:33:18'),
(104, 'Z2', 1, '8:10', '8:55', 'Irodalom', 'Pirik Martina', 'Csütörtök', '12.A', 12, 'Magyar alap', 'alap', '', b'1', '2024-07-16 09:33:18'),
(107, '8', 2, '9:05', '9:50', 'Irodalom', 'Zahoránné Pavelka Ildikó', 'Csütörtök', '12.B', 12, 'Magyar alap', 'alap', '', b'1', '2024-07-16 09:33:18'),
(110, 'T3', 1, '8:10', '8:55', 'Irodalom', 'Gálné Bagdán Eszter', 'Csütörtök', '12.C', 12, 'Magyar alap', 'alap', '', b'1', '2024-07-16 09:33:18'),
(113, 'Z3', 2, '9:05', '9:50', 'Irodalom', 'Maller Márta', 'Csütörtök', '[List]', 12, '[List]', 'emelt', '', b'1', '2024-07-16 09:33:18'),
(126, '1', 4, '11:00', '11:45', 'Magyar nyelv', 'Pirik Martina', 'Csütörtök', '8.A', 8, '1. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(138, '7', 3, '10:05', '10:50', 'Magyar nyelv', 'Geiszelhardt Zsófia', 'Csütörtök', '11.A', 11, 'Magyar alap', 'alap', '', b'1', '2024-07-16 09:33:18'),
(139, 'T3', 3, '10:05', '10:50', 'Magyar nyelv', 'Maller Márta', 'Csütörtök', '11.C', 11, 'Magyar alap', 'alap', '', b'1', '2024-07-16 09:33:18'),
(140, '21', 3, '10:05', '10:50', 'Magyar nyelv', 'Zahoránné Pavelka Ildikó', 'Csütörtök', '11.B', 11, 'Magyar alap', 'alap', '', b'1', '2024-07-16 09:33:18'),
(142, '17', 4, '11:00', '11:45', 'Magyar nyelv', 'Gálné Bagdán Eszter', 'Csütörtök', '[List]', 11, '[List]', 'emelt', '', b'1', '2024-07-16 09:33:18'),
(143, 'Z2', 2, '9:05', '9:50', 'Magyar nyelv', 'Pirik Martina', 'Csütörtök', '12.A', 12, 'Magyar alap', 'alap', '', b'1', '2024-07-16 09:33:18'),
(144, '8', 1, '8:10', '8:55', 'Magyar nyelv', 'Zahoránné Pavelka Ildikó', 'Csütörtök', '12.B', 12, 'Magyar alap', 'alap', '', b'1', '2024-07-16 09:33:18'),
(145, 'T3', 2, '9:05', '9:50', 'Magyar nyelv', 'Gálné Bagdán Eszter', 'Csütörtök', '12.C', 12, 'Magyar alap', 'alap', '', b'1', '2024-07-16 09:33:18'),
(147, 'Z3', 1, '8:10', '8:55', 'Magyar nyelv', 'Maller Márta', 'Csütörtök', '[List]', 12, '[List]', 'emelt', '', b'1', '2024-07-16 09:33:18'),
(150, 'Z2', 3, '10:05', '10:50', 'Dráma és tánc', 'Pirik Martina', 'Csütörtök', '12.A', 12, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(152, 'T3', 5, '11:55', '12:40', 'Dráma és tánc', 'Gálné Bagdán Eszter', 'Csütörtök', '12.C', 12, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(154, '14', 2, '9:05', '9:50', 'Történelem', 'Farkas Diána', 'Csütörtök', '7.A', 7, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(162, 'K2', 6, '12:50', '13:35', 'Történelem', 'Nagy Dániel', 'Csütörtök', '9.C', 9, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(164, '16', 3, '10:05', '10:50', 'Történelem', 'Szakál Ferenc Csaba', 'Csütörtök', '10.B', 10, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(174, '6', 5, '11:55', '12:40', 'Történelem, társadalmi és állampolgári ismeretek ', 'Nagy Dániel', 'Csütörtök', '10.A', 10, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(194, 'Eml', 4, '11:00', '11:45', 'Baptista hittan', 'Szimon Gergő', 'Csütörtök', '7.A', 7, 'Bapt.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(196, 'Eml', 5, '11:55', '12:40', 'Baptista hittan', 'Szimon Gergő', 'Csütörtök', '8.A', 8, 'Bapt', 'alap', '', b'1', '2024-07-16 09:33:18'),
(198, '22', 6, '12:50', '13:35', 'Evangélikus hittan', 'Franko Mátyás', 'Csütörtök', '11.B', 11, 'Ev.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(199, '6', 4, '11:00', '11:45', 'Katolikus hittan', 'Juhász Csilla', 'Csütörtök', '7.A', 7, 'Kat.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(201, '14', 5, '11:55', '12:40', 'Katolikus hittan', 'Juhász Csilla', 'Csütörtök', '8.A', 8, 'Kat', 'alap', '', b'1', '2024-07-16 09:33:18'),
(203, '7', 6, '12:50', '13:35', 'Katolikus hittan', 'Juhász Csilla', 'Csütörtök', '9.A', 9, 'Kat.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(206, '7', 2, '9:05', '9:50', 'Katolikus hittan', 'Juhász Csilla', 'Csütörtök', '9.B', 9, 'Kat.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(208, '25', 1, '8:10', '8:55', 'Katolikus hittan', 'Juhász Csilla', 'Csütörtök', '9.C', 9, 'Kat.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(210, '16', 1, '8:10', '8:55', 'Katolikus hittan', 'Havassy Bálint', 'Csütörtök', '[List]', 10, '[List]', 'alap', '', b'1', '2024-07-16 09:33:18'),
(211, '8', 8, '14:50', '15:35', 'Katolikus hittan', 'Havassy Bálint', 'Csütörtök', '11.A', 11, 'Kat.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(213, '7', 5, '11:55', '12:40', 'Katolikus hittan', 'Havassy Bálint', 'Csütörtök', '[List]', 12, '[List]', 'alap', '', b'1', '2024-07-16 09:33:18'),
(218, '14', 4, '11:00', '11:45', 'Református hittan', 'Farkas Balázs', 'Csütörtök', '7.A', 7, 'Ref.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(220, '17', 6, '12:50', '13:35', 'Református hittan', 'Nagy Péterné', 'Csütörtök', '9.A', 9, 'Ref.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(221, 'K1', 2, '9:05', '9:50', 'Református hittan', 'Szabó Elődné', 'Csütörtök', '9.B', 9, 'Ref.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(224, 'K2', 1, '8:10', '8:55', 'Református hittan', 'Szabó Elődné', 'Csütörtök', '9.C', 9, 'Ref.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(226, '21', 1, '8:10', '8:55', 'Református hittan', 'Farkas Balázs', 'Csütörtök', '10.A', 10, 'Ref.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(227, '15', 2, '9:05', '9:50', 'Református hittan', 'Nagy Péterné', 'Csütörtök', '10.C', 10, 'Ref', 'alap', '', b'1', '2024-07-16 09:33:18'),
(229, 'K1', 1, '8:10', '8:55', 'Református hittan', 'Nagy Péterné', 'Csütörtök', '10.B', 10, 'Ref.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(232, '7', 8, '14:50', '15:35', 'Református hittan', 'Szabó Elődné', 'Csütörtök', '11.A', 11, 'Ref.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(233, 'Z2', 5, '11:55', '12:40', 'Református hittan', 'Farkas Balázs', 'Csütörtök', '12.A', 12, 'Ref.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(235, '8', 5, '11:55', '12:40', 'Református hittan', 'Szabó Elődné', 'Csütörtök', '12.B', 12, 'Ref.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(253, 'Z5', 6, '12:50', '13:35', 'Biológia', 'Hüvös-Récsi Annamária', 'Csütörtök', '10.A', 10, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(256, 'Z5', 4, '11:00', '11:45', 'Biológia', 'Hüvös-Récsi Annamária', 'Csütörtök', '10.B', 10, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(261, 'Z5', 3, '10:05', '10:50', 'Biológia', 'Hüvös-Récsi Annamária', 'Csütörtök', '10.C', 10, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(264, '1', 1, '8:10', '8:55', 'Biológia', 'Hüvös-Récsi Annamária', 'Csütörtök', '8.A', 8, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(266, 'Eml', 1, '8:10', '8:55', 'Baptista hittan', 'Szimon Gergő', 'Csütörtök', '[List]', 10, '[List]', 'alap', '', b'1', '2024-07-16 09:33:18'),
(267, 'Eml', 6, '12:50', '13:35', 'Baptista hittan', 'Szimon Gergő', 'Csütörtök', '11.B', 11, 'Bapt.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(269, '6', 6, '12:50', '13:35', 'Református hittan', 'Szabó Elődné', 'Csütörtök', '11.B', 11, 'Ref.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(272, '8', 6, '12:50', '13:35', 'Katolikus hittan', 'Havassy Bálint', 'Csütörtök', '11.B', 11, 'Kat.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(273, '22', 8, '14:50', '15:35', 'Evangélikus hittan', 'Franko Mátyás', 'Csütörtök', '11.A', 11, 'Ev.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(276, '22', 1, '8:10', '8:55', 'Evangélikus hittan', 'Franko Mátyás', 'Csütörtök', '10.A', 10, 'Ev.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(278, '22', 4, '11:00', '11:45', 'Evangélikus hittan', 'Franko Mátyás', 'Csütörtök', '7.A', 7, 'Ev.', 'alap', '', b'1', '2024-07-16 09:33:18'),
(282, 'Z5', 2, '9:05', '9:50', 'Kémia', 'Németh Krisztina Júlia', 'Csütörtök', '9.A', 9, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(291, '15', 1, '8:10', '8:55', 'Kémia', 'Pozsgayné Tóth Ildikó', 'Csütörtök', '10.C', 10, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(303, 'Z5', 1, '8:10', '8:55', 'Fizika', 'Vihartné Balogh Éva', 'Csütörtök', '9.B', 9, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(309, '16', 2, '9:05', '9:50', 'Fizika', 'Vihartné Balogh Éva', 'Csütörtök', '10.B', 10, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(320, '14', 6, '12:50', '13:35', 'Földrajz', 'Fodor Tibor', 'Csütörtök', '7.A', 7, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(322, '1', 2, '9:05', '9:50', 'Földrajz', 'Aladzsits Szilvia', 'Csütörtök', '8.A', 8, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(326, 'K1', 5, '11:55', '12:40', 'Földrajz', 'Fodor Tibor', 'Csütörtök', '9.B', 9, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(345, '5', 1, '8:10', '8:55', 'Digitális Kultúra', 'Kiss István', 'Csütörtök', '9.A', 9, '1. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(347, '5', 5, '11:55', '12:40', 'Digitális Kultúra', 'Kiss István', 'Csütörtök', '9.A', 9, '2. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(358, '24', 7, '14:00', '14:45', 'Digitális Kultúra', 'Kiss István', 'Csütörtök', '11.C', 11, '2. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(360, '5', 7, '14:00', '14:45', 'Digitális Kultúra', 'Köblös István', 'Csütörtök', '11.C', 11, '1. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(361, '24', 3, '10:05', '10:50', 'Digitális Kultúra', 'Kiss István', 'Csütörtök', '8.A', 8, '1. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(380, '8', 3, '10:05', '10:50', 'Osztályfőnöki', 'Essősyné Vízkeleti Gyöngyi', 'Csütörtök', '12.B', 12, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(381, 'T3', 6, '12:50', '13:35', 'Osztályfőnöki', 'Koros Gábor Kálmán', 'Csütörtök', '12.C', 12, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(383, 'K1', 6, '12:50', '13:35', 'Matematika', 'Szerticsné Pinczés Mária', 'Csütörtök', '9.B', 9, '1. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(387, 'Z2', 4, '11:00', '11:45', 'Matematika', 'Vihartné Balogh Éva', 'Csütörtök', '9.B', 9, '2. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(391, 'Z1', 1, '8:10', '8:55', 'Matematika', 'Köblös István', 'Csütörtök', '[List]', 11, '[List]', 'alap', '', b'1', '2024-07-16 09:33:18'),
(393, '17', 1, '8:10', '8:55', 'Matematika', 'Illés Marianna', 'Csütörtök', '[List]', 11, '[List]', 'alap', '', b'1', '2024-07-16 09:33:18'),
(396, '14', 1, '8:10', '8:55', 'Matematika', 'Illés Dániel János', 'Csütörtök', '[List]', 11, '[List]', 'alap', '', b'1', '2024-07-16 09:33:18'),
(402, '7', 1, '8:10', '8:55', 'Matematika', 'Németh Krisztina Júlia', 'Csütörtök', '[List]', 11, '[List]', 'emelt', '', b'1', '2024-07-16 09:33:18'),
(404, '6', 1, '8:10', '8:55', 'Matematika', 'Szerticsné Pinczés Mária', 'Csütörtök', '[List]', 11, '[List]', 'emelt', '', b'1', '2024-07-16 09:33:18'),
(416, '8', 7, '14:00', '14:45', 'Technika, életvitel és gyakorlat', 'Szabó Edit', 'Csütörtök', '[List]', 12, '[List]', 'alap', '', b'1', '2024-07-16 09:33:18'),
(417, 'T3', 7, '14:00', '14:45', 'Technika, életvitel és gyakorlat', 'Koros Gábor Kálmán', 'Csütörtök', '[List]', 12, '[List]', 'alap', '', b'1', '2024-07-16 09:33:18'),
(418, 'Z2', 7, '14:00', '14:45', 'Technika, életvitel és gyakorlat', 'Illés Marianna', 'Csütörtök', '[List]', 12, '[List]', 'emelt', '', b'1', '2024-07-16 09:33:18'),
(419, '16', 7, '14:00', '14:45', 'Technika, életvitel és gyakorlat', 'Szabóné Salgó Mária', 'Csütörtök', '[List]', 12, '[List]', 'emelt', '', b'1', '2024-07-16 09:33:18'),
(422, 'T2', 5, '11:55', '12:40', 'Testnevelés', 'Szurcsik Gyöngyvér', 'Csütörtök', '7.A', 7, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(427, 'T1', 2, '9:05', '9:50', 'Testnevelés', 'Basky Péter', 'Csütörtök', '9.C', 9, 'Lány', 'alap', '', b'1', '2024-07-16 09:33:18'),
(430, 'T2', 2, '9:05', '9:50', 'Testnevelés', 'Palásti Bence', 'Csütörtök', '9.C', 9, 'Fiú', 'alap', '', b'1', '2024-07-16 09:33:18'),
(434, 'T1', 5, '11:55', '12:40', 'Testnevelés', 'Basky Péter', 'Csütörtök', '9.A', 9, '1. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(437, 'T1', 1, '8:10', '8:55', 'Testnevelés', 'Gál Zoltán', 'Csütörtök', '9.A', 9, '2. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(450, 'T2', 7, '14:00', '14:45', 'Technika', 'Szurcsik Gyöngyvér', 'Csütörtök', '11.A', 11, 'Lány', 'alap', '', b'1', '2024-07-16 09:33:18'),
(455, 'T1', 7, '14:00', '14:45', 'Technika', 'Gál Zoltán', 'Csütörtök', '11.A', 11, 'Fiú', 'alap', '', b'1', '2024-07-16 09:33:18'),
(457, 'T1', 6, '12:50', '13:35', 'Technika', 'Szurcsik Gyöngyvér', 'Csütörtök', '12.A', 12, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(460, 'T2', 3, '10:05', '10:50', 'Technika', 'Gál Zoltán', 'Csütörtök', '12.C', 12, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(469, 'T2', 6, '12:50', '13:35', 'Testnevelés', 'Basky Péter', 'Csütörtök', '11.C', 11, 'Egész osztály', 'alap', '', b'1', '2024-07-16 09:33:18'),
(473, '26', 1, '8:10', '8:55', 'Angol nyelv', 'Hartmann Erika Andrea', 'Csütörtök', '7.A', 7, 'Angol 1.', 'alap', 'elso', b'1', '2024-07-16 09:33:18'),
(476, '1', 6, '12:50', '13:35', 'Angol nyelv', 'Pirik Martina', 'Csütörtök', '8.A', 8, 'Angol 1.', 'alap', 'elso', b'1', '2024-07-16 09:33:18'),
(477, '27', 1, '8:10', '8:55', 'Angol nyelv', 'Almerné Benedek Judit', 'Csütörtök', '7.A', 7, 'Angol 2.', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(481, '25', 6, '12:50', '13:35', 'Angol nyelv', 'Bierbauer-Kovács Emőke', 'Csütörtök', '8.A', 8, 'Angol 2.', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(487, '7', 7, '14:00', '14:45', 'Angol nyelv', 'Hartmann Erika Andrea', 'Csütörtök', '[List]', 9, '[List]', 'alap', 'elso', b'1', '2024-07-16 09:33:18'),
(493, '27', 7, '14:00', '14:45', 'Angol nyelv', 'Roszman Gergő Ferenc', 'Csütörtök', '[List]', 9, '[List]', 'alap', 'elso', b'1', '2024-07-16 09:33:18'),
(497, '6', 7, '14:00', '14:45', 'Angol nyelv', 'Katona Gabriella Mária', 'Csütörtök', '[List]', 9, '[List]', 'alap', 'elso', b'1', '2024-07-16 09:33:18'),
(498, '26', 3, '10:05', '10:50', 'Angol nyelv', 'Katona Gabriella Mária', 'Csütörtök', '[List]', 9, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(503, 'K1', 3, '10:05', '10:50', 'Angol nyelv', 'Roszman Gergő Ferenc', 'Csütörtök', '[List]', 9, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(505, '27', 3, '10:05', '10:50', 'Angol nyelv', 'Hartmann Erika Andrea', 'Csütörtök', '[List]', 9, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(517, '24', 2, '9:05', '9:50', 'Angol nyelv', 'Hartmann Erika Andrea', 'Csütörtök', '11.A', 11, 'Angol A 1/1', 'alap', 'elso', b'1', '2024-07-16 09:33:18'),
(521, '27', 2, '9:05', '9:50', 'Angol nyelv', 'Roszman Gergő Ferenc', 'Csütörtök', '11.A', 11, 'Angol A 1/2', 'alap', 'elso', b'1', '2024-07-16 09:33:18'),
(522, '25', 2, '9:05', '9:50', 'Angol nyelv', 'Almerné Benedek Judit', 'Csütörtök', '[List]', 11, '[List]', 'alap', 'elso', b'1', '2024-07-16 09:33:18'),
(526, '26', 2, '9:05', '9:50', 'Angol nyelv', 'Kerényi Gabriella', 'Csütörtök', '[List]', 11, '[List]', 'alap', 'elso', b'1', '2024-07-16 09:33:18'),
(531, '6', 2, '9:05', '9:50', 'Angol nyelv', 'Bierbauer-Kovács Emőke', 'Csütörtök', '[List]', 11, '[List]', 'alap', 'elso', b'1', '2024-07-16 09:33:18'),
(535, '26', 5, '11:55', '12:40', 'Angol nyelv', 'Roszman Gergő Ferenc', 'Csütörtök', '[List]', 11, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(539, '27', 5, '11:55', '12:40', 'Angol nyelv', 'Almerné Benedek Judit', 'Csütörtök', '[List]', 11, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(554, '26', 4, '11:00', '11:45', 'Angol nyelv', 'Katona Gabriella Mária', 'Csütörtök', '[List]', 12, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(558, '8', 4, '11:00', '11:45', 'Angol nyelv', 'Roszman Gergő Ferenc', 'Csütörtök', '[List]', 12, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(568, 'Z2', 6, '12:50', '13:35', 'Német nyelv', 'Essősyné Vízkeleti Gyöngyi', 'Csütörtök', '8.A', 8, 'Német', 'alap', 'elso', b'1', '2024-07-16 09:33:18'),
(571, '24', 1, '8:10', '8:55', 'Német nyelv', 'Essősyné Vízkeleti Gyöngyi', 'Csütörtök', '7.A', 7, 'Német', 'alap', 'elso', b'1', '2024-07-16 09:33:18'),
(574, '25', 7, '14:00', '14:45', 'Német nyelv', 'Gálné Bagdán Eszter', 'Csütörtök', '[List]', 9, '[List]', 'alap', 'elso', b'1', '2024-07-16 09:33:18'),
(580, 'K1', 7, '14:00', '14:45', 'Német nyelv', 'Fohner Éva Veronika', 'Csütörtök', '[List]', 9, '[List]', 'alap', 'elso', b'1', '2024-07-16 09:33:18'),
(584, 'K2', 3, '10:05', '10:50', 'Német nyelv', 'Tóth-Horváth Beáta', 'Csütörtök', '[List]', 9, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(588, 'Z3', 3, '10:05', '10:50', 'Német nyelv', 'Liebe Gabriella', 'Csütörtök', '[List]', 9, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(591, '25', 3, '10:05', '10:50', 'Német nyelv', 'Fohner Éva Veronika', 'Csütörtök', '[List]', 9, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(596, '15', 7, '14:00', '14:45', 'Német nyelv', 'Essősyné Vízkeleti Gyöngyi', 'Csütörtök', '[List]', 10, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(600, 'K2', 7, '14:00', '14:45', 'Német nyelv', 'Tóth-Horváth Beáta', 'Csütörtök', '[List]', 10, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(602, '21', 2, '9:05', '9:50', 'Német nyelv', 'Fohner Éva Veronika', 'Csütörtök', '11.A', 11, 'Német A', 'alap', 'elso', b'1', '2024-07-16 09:33:18'),
(605, '24', 5, '11:55', '12:40', 'Német nyelv', 'Geiszelhardt Zsófia', 'Csütörtök', '[List]', 11, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(609, '17', 5, '11:55', '12:40', 'Német nyelv', 'Tóth-Horváth Beáta', 'Csütörtök', '[List]', 11, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(612, '25', 5, '11:55', '12:40', 'Német nyelv', 'Liebe Gabriella', 'Csütörtök', '[List]', 11, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(623, '24', 4, '11:00', '11:45', 'Német nyelv', 'Fohner Éva Veronika', 'Csütörtök', '[List]', 12, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(625, '25', 4, '11:00', '11:45', 'Német nyelv', 'Liebe Gabriella', 'Csütörtök', '[List]', 12, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(629, '15', 4, '11:00', '11:45', 'Német nyelv', 'Essősyné Vízkeleti Gyöngyi', 'Csütörtök', '[List]', 12, '[List]', 'alap', 'masodik', b'1', '2024-07-16 09:33:18'),
(640, '22', 5, '11:55', '12:40', 'Evangélikus hittan', 'Franko Mátyás', 'Csütörtök', '8.A', 8, 'Ev', 'alap', '', b'1', '2024-07-16 09:33:18'),
(695, '15', 5, '11:55', '12:40', 'Matematika', 'Köblös István', 'Csütörtök', '[List]', 10, '[List]', 'alap', '', b'1', '2024-07-16 09:33:18'),
(696, '15', 6, '12:50', '13:35', 'Matematika', 'Köblös István', 'Csütörtök', '[List]', 10, '[List]', 'alap', '', b'1', '2024-07-16 09:33:18'),
(699, '21', 5, '11:55', '12:40', 'Matematika', 'Szabó Edit', 'Csütörtök', '[List]', 10, '[List]', 'alap', '', b'1', '2024-07-16 09:33:18'),
(700, '21', 6, '12:50', '13:35', 'Matematika', 'Szabó Edit', 'Csütörtök', '[List]', 10, '[List]', 'alap', '', b'1', '2024-07-16 09:33:18'),
(703, '16', 5, '11:55', '12:40', 'Matematika', 'Vihartné Balogh Éva', 'Csütörtök', '[List]', 10, '[List]', 'alap', '', b'1', '2024-07-16 09:33:18'),
(704, '16', 6, '12:50', '13:35', 'Matematika', 'Vihartné Balogh Éva', 'Csütörtök', '[List]', 10, '[List]', 'alap', '', b'1', '2024-07-16 09:33:18'),
(729, '5', 2, '9:05', '9:50', 'Matematika', 'Koros Gábor Kálmán', 'Csütörtök', '10.A', 10, '1. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(731, '5', 3, '10:05', '10:50', 'Matematika', 'Koros Gábor Kálmán', 'Csütörtök', '10.A', 10, '1. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(733, 'Z1', 2, '9:05', '9:50', 'Matematika', 'Illés Marianna', 'Csütörtök', '10.A', 10, '2. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(735, 'Z1', 3, '10:05', '10:50', 'Matematika', 'Illés Marianna', 'Csütörtök', '10.A', 10, '2. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(738, '14', 3, '10:05', '10:50', 'Matematika', 'Szerticsné Pinczés Mária', 'Csütörtök', '7.A', 7, '1. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(741, '15', 3, '10:05', '10:50', 'Matematika', 'Németh Krisztina Júlia', 'Csütörtök', '7.A', 7, '2. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(749, 'Z1', 4, '11:00', '11:45', 'Matematika', 'Köblös István', 'Csütörtök', '8.A', 8, '2. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(751, '6', 3, '10:05', '10:50', 'Matematika', 'Köblös István', 'Csütörtök', '8.A', 8, '2. csoport', 'alap', '', b'1', '2024-07-16 09:33:18'),
(753, '16', 4, '11:00', '11:45', 'Matematika', 'Szerticsné Pinczés Mária', 'Csütörtök', '[List]', 9, '[List]', 'alap', '', b'1', '2024-07-16 09:33:18'),
(757, 'K2', 4, '11:00', '11:45', 'Matematika', 'Németh Krisztina Júlia', 'Csütörtök', '[List]', 9, '[List]', 'alap', '', b'1', '2024-07-16 09:33:18'),
(761, 'K1', 4, '11:00', '11:45', 'Matematika', 'Illés Marianna', 'Csütörtök', '[List]', 9, '[List]', 'alap', '', b'1', '2024-07-16 09:33:18'),
(773, 'Z5', 8, '14:50', '15:35', 'Biológia', 'Hüvös-Récsi Annamária', 'Csütörtök', '[List]', 11, '[List]', 'emelt', '', b'1', '2024-07-16 09:33:18'),
(779, 'K2', 2, '9:05', '9:50', 'Német nyelv', 'Tóth-Horváth Beáta', 'Csütörtök', '[List]', 11, '[List]', 'alap', 'elso', b'1', '2024-07-16 09:33:18');

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `lessons`
--
ALTER TABLE `lessons`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
