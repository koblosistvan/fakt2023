-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2025. Már 06. 22:46
-- Kiszolgáló verziója: 10.4.32-MariaDB
-- PHP verzió: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `iroda`
--

DROP DATABASE IF EXISTS `iroda`;
CREATE DATABASE `iroda`;
USE `iroda`;

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `doku`
--

CREATE TABLE `doku` (
  `id` int(3) NOT NULL,
  `terjedelem` int(6) DEFAULT NULL,
  `szakterulet` varchar(19) DEFAULT NULL,
  `nyelvid` int(3) DEFAULT NULL,
  `munkaido` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- A tábla adatainak kiíratása `doku`
--

INSERT INTO `doku` (`id`, `terjedelem`, `szakterulet`, `nyelvid`, `munkaido`) VALUES
(1, 111932, 'jog', 3, 8),
(2, 90630, 'hivatalos okmány', 1, 8),
(3, 128217, 'informatika', 5, 4),
(4, 81699, 'pszichológia', 91, 13),
(5, 135694, 'jog', 65, 5),
(6, 140936, 'hivatalos okmány', 5, 10),
(7, 60677, 'informatika', 46, 8),
(8, 75321, 'pszichológia', 23, 13),
(9, 145299, 'jog', 1, 13),
(10, 61808, 'hivatalos okmány', 2, 6),
(11, 45416, 'informatika', 93, 8),
(12, 25600, 'pszichológia', 56, 7),
(13, 103703, 'kereskedelem', 96, 10),
(14, 10017, 'marketing', 3, 7),
(15, 104520, 'marketing', 88, 10),
(16, 88806, 'idegenforgalom', 46, 9),
(17, 25685, 'építőipar', 97, 9),
(18, 103737, 'irodalom', 5, 14),
(19, 43435, 'vegyipar', 1, 1),
(20, 18902, 'pénzügy', 23, 11),
(21, 87064, 'hivatalos levelezés', 52, 8),
(22, 65690, 'gépészet', 7, 12),
(23, 134454, 'elektronika', 35, 5),
(24, 102427, 'életmód', 50, 11),
(25, 134769, 'sport', 4, 10),
(26, 83203, 'környzetvédelem', 54, 3),
(27, 131487, 'marketing', 1, 15),
(28, 130810, 'ingatlan', 2, 12),
(29, 36753, 'logisztika', 51, 9),
(30, 33051, 'marketing', 10, 7),
(31, 126741, 'ingatlan', 52, 15),
(32, 134898, 'logisztika', 50, 12),
(33, 131665, 'pszichológia', 50, 11),
(34, 33128, 'kereskedelem', 50, 5),
(35, 13191, 'idegenforgalom', 51, 9),
(36, 16977, 'marketing', 61, 10),
(37, 100467, 'ingatlan', 50, 5),
(38, 100532, 'marketing', 104, 13),
(39, 13628, 'ingatlan', 49, 3),
(40, 99985, 'logisztika', 23, 13),
(41, 17736, 'hivatalos levelezés', 87, 6),
(42, 96820, 'gépészet', 102, 14),
(43, 82163, 'elektronika', 41, 13),
(44, 82834, 'életmód', 32, 7),
(45, 28346, 'sport', 40, 9),
(46, 75106, 'életmód', 6, 5),
(47, 31780, 'sport', 78, 2),
(48, 134765, 'életmód', 23, 10),
(49, 111867, 'sport', 92, 7),
(50, 71202, 'életmód', 64, 3),
(51, 60960, 'sport', 18, 12),
(52, 124477, 'pszichológia', 50, 9),
(53, 47953, 'kereskedelem', 9, 4),
(54, 47275, 'idegenforgalom', 50, 7),
(55, 48762, 'pszichológia', 68, 5),
(56, 116143, 'pszichológia', 9, 2),
(57, 147329, 'kereskedelem', 58, 15),
(58, 92090, 'idegenforgalom', 50, 9),
(59, 109009, 'irodalom', 89, 9),
(60, 93969, 'irodalom', 34, 6),
(61, 115456, 'irodalom', 50, 7),
(62, 2911, 'sport', 20, 3),
(63, 106903, 'irodalom', 59, 11),
(64, 87564, 'irodalom', 50, 3),
(65, 77039, 'irodalom', 50, 14),
(66, 79114, 'pénzügy', 94, 6),
(67, 137429, 'hivatalos levelezés', 87, 8),
(68, 148592, 'gépészet', 50, 10),
(69, 18006, 'elektronika', 93, 11),
(70, 103342, 'pénzügy', 50, 13),
(71, 124148, 'hivatalos levelezés', 29, 5),
(72, 120648, 'gépészet', 14, 4),
(73, 96161, 'elektronika', 77, 10),
(74, 3139, 'életmód', 86, 8),
(75, 114171, 'hivatalos levelezés', 89, 13),
(76, 4823, 'hivatalos levelezés', 51, 1),
(77, 84995, 'hivatalos levelezés', 10, 3),
(78, 115263, 'hivatalos levelezés', 91, 14),
(79, 55404, 'hivatalos levelezés', 50, 6),
(80, 50803, 'hivatalos levelezés', 52, 11),
(81, 137144, 'hivatalos levelezés', 12, 13),
(82, 59669, 'pénzügy', 51, 10),
(83, 24137, 'pénzügy', 3, 1),
(84, 69478, 'irodalom', 3, 8),
(85, 48414, 'irodalom', 50, 12),
(86, 138129, 'irodalom', 39, 8),
(87, 10767, 'irodalom', 50, 11),
(88, 6045, 'irodalom', 50, 3),
(89, 102679, 'irodalom', 58, 13),
(90, 142379, 'pénzügy', 58, 14),
(91, 141032, 'környzetvédelem', 51, 13),
(92, 143820, 'környzetvédelem', 19, 15),
(93, 123483, 'környzetvédelem', 50, 8),
(94, 119705, 'környzetvédelem', 2, 3),
(95, 121680, 'környzetvédelem', 129, 12),
(96, 27461, 'vegyipar', 44, 10),
(97, 142464, 'elektronika', 47, 2),
(98, 54162, 'elektronika', 2, 7),
(99, 91945, 'elektronika', 37, 8),
(100, 74921, 'elektronika', 50, 2),
(101, 88852, 'elektronika', 51, 13),
(102, 119913, 'irodalom', 51, 5),
(103, 127807, 'irodalom', 50, 5),
(104, 42868, 'elektronika', 124, 4),
(105, 142781, 'vegyipar', 2, 12),
(106, 28415, 'elektronika', 60, 4),
(107, 11871, 'elektronika', 91, 5),
(108, 94497, 'elektronika', 23, 7),
(109, 65428, 'irodalom', 120, 12),
(110, 67236, 'irodalom', 10, 8),
(111, 90071, 'irodalom', 6, 2),
(112, 23792, 'irodalom', 1, 7),
(113, 23435, 'vegyipar', 1, 11),
(114, 96804, 'vegyipar', 1, 3);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `fordito`
--

CREATE TABLE `fordito` (
  `nyelvid` int(3) DEFAULT NULL,
  `szemelyid` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- A tábla adatainak kiíratása `fordito`
--

INSERT INTO `fordito` (`nyelvid`, `szemelyid`) VALUES
(1, 1),
(18, 1),
(50, 1),
(67, 1),
(4, 2),
(53, 2),
(99, 2),
(111, 2),
(2, 3),
(19, 3),
(51, 3),
(68, 3),
(1, 4),
(31, 4),
(49, 4),
(50, 4),
(80, 4),
(98, 4),
(1, 5),
(17, 5),
(30, 5),
(50, 5),
(66, 5),
(79, 5),
(3, 6),
(24, 6),
(52, 6),
(73, 6),
(4, 7),
(53, 7),
(3, 8),
(29, 8),
(52, 8),
(78, 8),
(100, 8),
(112, 8),
(5, 9),
(54, 9),
(11, 10),
(60, 10),
(6, 11),
(21, 11),
(23, 33),
(55, 11),
(70, 11),
(72, 11),
(5, 12),
(22, 12),
(54, 12),
(71, 12),
(7, 13),
(56, 13),
(2, 14),
(51, 14),
(1, 15),
(50, 15),
(12, 16),
(61, 16),
(1, 17),
(50, 17),
(13, 18),
(62, 18),
(1, 19),
(50, 19),
(2, 20),
(51, 20),
(14, 21),
(63, 21),
(4, 22),
(53, 22),
(4, 23),
(20, 23),
(53, 23),
(69, 23),
(14, 24),
(63, 24),
(8, 25),
(57, 25),
(4, 26),
(53, 26),
(2, 27),
(16, 27),
(51, 27),
(65, 27),
(15, 28),
(64, 28),
(2, 29),
(51, 29),
(8, 30),
(25, 30),
(57, 30),
(74, 30),
(2, 31),
(51, 31),
(9, 32),
(58, 32),
(1, 33),
(50, 33),
(10, 34),
(59, 34),
(1, 35),
(50, 35),
(26, 36),
(75, 36),
(27, 37),
(76, 37),
(28, 38),
(77, 38),
(32, 39),
(81, 39),
(33, 40),
(82, 40),
(34, 41),
(83, 41),
(35, 42),
(84, 42),
(36, 43),
(85, 43),
(37, 44),
(86, 44),
(38, 45),
(87, 45),
(39, 46),
(88, 46),
(40, 47),
(89, 47),
(41, 48),
(90, 48),
(42, 49),
(91, 49),
(43, 50),
(92, 50),
(44, 51),
(93, 51),
(45, 52),
(94, 52),
(46, 53),
(95, 53),
(47, 54),
(96, 54),
(48, 55),
(97, 55),
(101, 56),
(113, 56),
(102, 57),
(114, 57),
(103, 58),
(115, 58),
(104, 59),
(116, 59),
(105, 60),
(117, 60),
(106, 61),
(118, 61),
(107, 62),
(119, 62),
(108, 63),
(120, 63),
(109, 64),
(121, 64),
(110, 65),
(122, 65),
(123, 66),
(134, 66),
(124, 67),
(135, 67),
(125, 68),
(136, 68),
(126, 69),
(137, 69),
(127, 70),
(138, 70),
(128, 71),
(139, 71),
(129, 72),
(140, 72),
(130, 73),
(141, 73),
(131, 74),
(142, 74),
(132, 75),
(143, 75),
(133, 76),
(144, 76);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `nyelv`
--

CREATE TABLE `nyelv` (
  `id` int(3) NOT NULL,
  `fnyelv` varchar(10) DEFAULT NULL,
  `cnyelv` varchar(10) DEFAULT NULL,
  `egysegar` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- A tábla adatainak kiíratása `nyelv`
--

INSERT INTO `nyelv` (`id`, `fnyelv`, `cnyelv`, `egysegar`) VALUES
(1, 'magyar', 'angol', 4000),
(2, 'magyar', 'német', 4000),
(3, 'magyar', 'spanyol', 4000),
(4, 'magyar', 'olasz', 4000),
(5, 'magyar', 'francia', 4000),
(6, 'magyar', 'albán', 8000),
(7, 'magyar', 'arab', 8000),
(8, 'magyar', 'bolgár', 8000),
(9, 'magyar', 'cseh', 8000),
(10, 'magyar', 'dán', 8000),
(11, 'magyar', 'észt', 8000),
(12, 'magyar', 'finn', 8000),
(13, 'magyar', 'héber', 10000),
(14, 'magyar', 'holland', 10000),
(15, 'magyar', 'horváth', 4000),
(16, 'magyar', 'japán', 10000),
(17, 'magyar', 'kínai', 10000),
(18, 'magyar', 'latin', 10000),
(19, 'magyar', 'lengyel', 4000),
(20, 'magyar', 'lett', 4000),
(21, 'magyar', 'litván', 4000),
(22, 'magyar', 'norvég', 4000),
(23, 'magyar', 'orosz', 4000),
(24, 'magyar', 'portugál', 7000),
(25, 'magyar', 'román', 4000),
(26, 'magyar', 'svéd', 7000),
(27, 'magyar', 'szerb', 4000),
(28, 'magyar', 'szlovák', 4000),
(29, 'magyar', 'szlovén', 4000),
(30, 'magyar', 'török', 9000),
(31, 'magyar', 'ukrán', 4000),
(32, 'magyar', 'azeri', 10000),
(33, 'magyar', 'belorusz', 4000),
(34, 'magyar', 'bengáli', 14000),
(35, 'magyar', 'dari', 12000),
(36, 'magyar', 'eszperantó', 8000),
(37, 'magyar', 'flamand', 10000),
(38, 'magyar', 'hindi', 10000),
(39, 'magyar', 'indonéz', 10000),
(40, 'magyar', 'kazah', 10000),
(41, 'magyar', 'koreai', 10000),
(42, 'magyar', 'kurd', 10000),
(43, 'magyar', 'macedon', 4000),
(44, 'magyar', 'mongol', 10000),
(45, 'magyar', 'örmény', 10000),
(46, 'magyar', 'perzsa', 10000),
(47, 'magyar', 'tibeti', 10000),
(48, 'magyar', 'vietnámi', 10000),
(49, 'magyar', 'katalán', 10000),
(50, 'angol', 'magyar', 4000),
(51, 'német', 'magyar', 4000),
(52, 'spanyol', 'magyar', 4000),
(53, 'olasz', 'magyar', 4000),
(54, 'francia', 'magyar', 4000),
(55, 'albán', 'magyar', 8000),
(56, 'arab', 'magyar', 8000),
(57, 'bolgár', 'magyar', 8000),
(58, 'cseh', 'magyar', 8000),
(59, 'dán', 'magyar', 8000),
(60, 'észt', 'magyar', 8000),
(61, 'finn', 'magyar', 8000),
(62, 'héber', 'magyar', 10000),
(63, 'holland', 'magyar', 10000),
(64, 'horváth', 'magyar', 4000),
(65, 'japán', 'magyar', 10000),
(66, 'kínai', 'magyar', 10000),
(67, 'latin', 'magyar', 10000),
(68, 'lengyel', 'magyar', 4000),
(69, 'lett', 'magyar', 4000),
(70, 'litván', 'magyar', 4000),
(71, 'norvég', 'magyar', 4000),
(72, 'orosz', 'magyar', 4000),
(73, 'portugál', 'magyar', 7000),
(74, 'román', 'magyar', 4000),
(75, 'svéd', 'magyar', 7000),
(76, 'szerb', 'magyar', 4000),
(77, 'szlovák', 'magyar', 4000),
(78, 'szlovén', 'magyar', 4000),
(79, 'török', 'magyar', 9000),
(80, 'ukrán', 'magyar', 4000),
(81, 'azeri', 'magyar', 10000),
(82, 'belorusz', 'magyar', 4000),
(83, 'bengáli', 'magyar', 14000),
(84, 'dari', 'magyar', 12000),
(85, 'eszperantó', 'magyar', 8000),
(86, 'flamand', 'magyar', 10000),
(87, 'hindi', 'magyar', 10000),
(88, 'indonéz', 'magyar', 10000),
(89, 'kazah', 'magyar', 10000),
(90, 'koreai', 'magyar', 10000),
(91, 'kurd', 'magyar', 10000),
(92, 'macedon', 'magyar', 4000),
(93, 'mongol', 'magyar', 10000),
(94, 'örmény', 'magyar', 10000),
(95, 'perzsa', 'magyar', 10000),
(96, 'tibeti', 'magyar', 10000),
(97, 'vietnámi', 'magyar', 10000),
(98, 'katalán', 'magyar', 10000),
(99, 'angol', 'német', 5000),
(100, 'angol', 'spanyol', 7500),
(101, 'angol', 'olasz', 7500),
(102, 'angol', 'francia', 6000),
(103, 'angol', 'lengyel', 7500),
(104, 'angol', 'lengyel', 7500),
(105, 'angol', 'orosz', 6000),
(106, 'angol', 'portugál', 7500),
(107, 'angol', 'román', 7500),
(108, 'angol', 'szlovák', 7500),
(109, 'angol', 'szlovén', 7500),
(110, 'angol', 'török', 8000),
(111, 'német', 'angol', 5000),
(112, 'spanyol', 'angol', 7500),
(113, 'olasz', 'angol', 7500),
(114, 'francia', 'angol', 6000),
(115, 'lengyel', 'angol', 7500),
(116, 'lengyel', 'angol', 7500),
(117, 'orosz', 'angol', 6000),
(118, 'portugál', 'angol', 7500),
(119, 'román', 'angol', 7500),
(120, 'szlovák', 'angol', 7500),
(121, 'szlovén', 'angol', 7500),
(122, 'török', 'angol', 8000),
(123, 'német', 'spanyol', 7500),
(124, 'német', 'olasz', 7500),
(125, 'német', 'francia', 7500),
(126, 'német', 'lengyel', 7500),
(127, 'német', 'lengyel', 7500),
(128, 'német', 'orosz', 6000),
(129, 'német', 'portugál', 8000),
(130, 'német', 'román', 6000),
(131, 'német', 'szlovák', 7500),
(132, 'német', 'szlovén', 7500),
(133, 'német', 'török', 7500),
(134, 'spanyol', 'német', 7500),
(135, 'olasz', 'német', 7500),
(136, 'francia', 'német', 7500),
(137, 'lengyel', 'német', 7500),
(138, 'cseh', 'német', 7500),
(139, 'orosz', 'német', 6000),
(140, 'portugál', 'német', 8000),
(141, 'román', 'német', 6000),
(142, 'szlovák', 'német', 7500),
(143, 'szlovén', 'német', 7500),
(144, 'török', 'német', 7500);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `szemely`
--

CREATE TABLE `szemely` (
  `id` int(2) NOT NULL,
  `nev` varchar(23) DEFAULT NULL,
  `elerheto` tinyint(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- A tábla adatainak kiíratása `szemely`
--

INSERT INTO `szemely` (`id`, `nev`, `elerheto`) VALUES
(1, 'Skvar Tamás', -1),
(2, 'Tatár István', -1),
(3, 'Siket Karen', 0),
(4, 'Horváth Mercédesz', -1),
(5, 'Dombovári Petra', -1),
(6, 'Rém Elek', -1),
(7, 'Kamarás Zsófia Viktória', -1),
(8, 'Sebő Tas', -1),
(9, 'Szendrődi Csaba', -1),
(10, 'Berger Péter', -1),
(11, 'Csonka Anna', -1),
(12, 'Szelei Anikó Dorina', -1),
(13, 'Kovács Ágnes', -1),
(14, 'Szőke Mátyás', -1),
(15, 'Kiss Zsófia', -1),
(16, 'Bakos Kata Judit', -1),
(17, 'Bodnár Anna Katalin', -1),
(18, 'Keszthelyi Zsolt', -1),
(19, 'Kiss Lajos', 0),
(20, 'Szabó Orsolya Virág', 0),
(21, 'Vég Kálmán', -1),
(22, 'Hirzer Zsolt', -1),
(23, 'Kincses Zoltán', -1),
(24, 'Zentay Réka', -1),
(25, 'Kovai Róbert', -1),
(26, 'Koch Róbert', -1),
(27, 'Szilágyi István', 0),
(28, 'Horváth Pál', -1),
(29, 'Duma Árpád', -1),
(30, 'Nemes Gerda', -1),
(31, 'Zsolnai Péter', 0),
(32, 'Illés Nóra', -1),
(33, 'Fődi Anna', -1),
(34, 'Szűcs Lóránt', -1),
(35, 'Borsos Anett', -1),
(36, 'Sarlós Róbert', -1),
(37, 'Hoffmann Bettina', -1),
(38, 'Farkas Ildikó', -1),
(39, 'Gál Brigitta', 0),
(40, 'Szabó Izabella Diána', -1),
(41, 'Rácz Lili', 0),
(42, 'Botos Noémi', -1),
(43, 'Kasznár Judit', -1),
(44, 'Lengyel Zsófia', -1),
(45, 'Kerekes Lili', -1),
(46, 'Kis Barbara Emma', -1),
(47, 'Vida Csongor', -1),
(48, 'Nagy Eszter', -1),
(49, 'Benkő Kata Enikő', -1),
(50, 'Urbán Roland', -1),
(51, 'Samu Blanka', 0),
(52, 'Pálinkás Anna', -1),
(53, 'Falch Emil', 0),
(54, 'Teleki Kálmán', -1),
(55, 'Sima Dezső', -1),
(56, 'Rudas Ádám', -1),
(57, 'Forrai Laura', 0),
(58, 'Irinyi Katalin Ida', -1),
(59, 'Hódi Vivien', -1),
(60, 'Máté Oszkár', -1),
(61, 'Püski Kata', -1),
(62, 'Mészáros Anita Réka', -1),
(63, 'Kis Nóra Judit', -1),
(64, 'Nyári Judit', -1),
(65, 'Balog Orsolya', -1),
(66, 'Zombori Adrienn', -1),
(67, 'Tóti Albert', -1),
(68, 'Szabó Lilla', -1),
(69, 'Petres Zoltán', -1),
(70, 'Barta Petra', -1),
(71, 'Rovó Petra', -1),
(72, 'Bor János', -1),
(73, 'Fogó Róbert', -1),
(74, 'Juhász Imre', -1),
(75, 'Nagy Tímea', 0),
(76, 'Tanács Lilla', -1);

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `doku`
--
ALTER TABLE `doku`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_doku_nyelvid` (`nyelvid`);

--
-- A tábla indexei `fordito`
--
ALTER TABLE `fordito`
  ADD KEY `fk_fordito_nyelvid` (`nyelvid`),
  ADD KEY `fk_fordito_szemelyid` (`szemelyid`);

--
-- A tábla indexei `nyelv`
--
ALTER TABLE `nyelv`
  ADD PRIMARY KEY (`id`);

--
-- A tábla indexei `szemely`
--
ALTER TABLE `szemely`
  ADD PRIMARY KEY (`id`);

--
-- Megkötések a kiírt táblákhoz
--

--
-- Megkötések a táblához `doku`
--
ALTER TABLE `doku`
  ADD CONSTRAINT `fk_doku_nyelvid` FOREIGN KEY (`nyelvid`) REFERENCES `nyelv` (`id`);

--
-- Megkötések a táblához `fordito`
--
ALTER TABLE `fordito`
  ADD CONSTRAINT `fk_fordito_nyelvid` FOREIGN KEY (`nyelvid`) REFERENCES `nyelv` (`id`),
  ADD CONSTRAINT `fk_fordito_szemelyid` FOREIGN KEY (`szemelyid`) REFERENCES `szemely` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
