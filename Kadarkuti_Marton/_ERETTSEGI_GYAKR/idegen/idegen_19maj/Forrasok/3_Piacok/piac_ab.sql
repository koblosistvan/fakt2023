-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2025. Már 06. 23:03
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
-- Adatbázis: `piac_ab`
--

DROP DATABASE IF EXISTS `piac_ab`;
CREATE DATABASE `piac_ab`;
USE `piac_ab`;

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `arusitohely`
--

CREATE TABLE `arusitohely` (
  `id` int(2) NOT NULL,
  `nev` varchar(33) DEFAULT NULL,
  `tipus` varchar(20) DEFAULT NULL,
  `megye` varchar(7) DEFAULT NULL,
  `telepules` varchar(17) DEFAULT NULL,
  `irszam` int(4) DEFAULT NULL,
  `cim` varchar(57) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- A tábla adatainak kiíratása `arusitohely`
--

INSERT INTO `arusitohely` (`id`, `nev`, `tipus`, `megye`, `telepules`, `irszam`, `cim`) VALUES
(1, 'Napi élelmiszerpiac', 'piac', 'Somogy', 'Balatonboglár', 8630, 'Dózsa utca'),
(2, 'Állat- és kirakodóvásár', 'vásár', 'Somogy', 'Balatonboglár', 8630, 'Zrínyi utca, Major'),
(3, 'Élelmiszerpiac', 'piac', 'Somogy', 'Balatonlelle', 8638, 'Rákóczi utca'),
(4, 'Őstermelői piac', 'termelői piac', 'Somogy', 'Balatonmáriafürdő', 8647, 'Fizető strand'),
(5, 'Vásárcsarnok, Helyi kirakodóvásár', 'piac és vásárcsarnok', 'Somogy', 'Barcs', 7570, '1819/53 hrsz.'),
(6, 'Petörke Portéka', 'termelői piac', 'Somogy', 'Bárdudvarnok', 7478, 'Petörke-tó partja'),
(7, 'Községi piac ', 'piac', 'Tolna', 'Báta', 7149, 'Fő utca 159.'),
(8, 'Piac', 'piac', 'Tolna', 'Bátaszék', 7140, 'Kossuth utca'),
(9, 'Rákóczi utcai piac', 'piac', 'Tolna', 'Bonyhád', 7150, 'Rákóczi utca'),
(10, 'Országos állat- és kirakodóvásár', 'vásár', 'Tolna', 'Bonyhád', 7150, '1029 hrsz.'),
(11, 'Piac', 'piac', 'Tolna', 'Dombóvár', 7200, 'Petőfi utca 11.'),
(12, 'Állatvásár', 'vásár', 'Tolna', 'Dombóvár', 7200, 'Teleki utca'),
(13, 'Kirakodó vásár', 'vásár', 'Tolna', 'Dombóvár', 7200, 'Dózsa György utca 1.'),
(14, 'Vegyes termékek árusítása', 'piac', 'Tolna', 'Fadd', 7133, 'Mátyás király utca 32.'),
(15, 'Országos állat- és kirakodóvásár', 'vásár', 'Tolna', 'Fadd', 7133, 'Mátyás király utca nyugati végén lévő közterület'),
(16, 'Piaccsarnok, vásár', 'piac és vásárcsarnok', 'Somogy', 'Fonyód', 8640, '8053 hrsz, 8044/10-13, 10235, 10236, 10242 hrsz.'),
(17, 'Piac', 'piac', 'Baranya', 'Harkány', 7815, 'Ady Endre utca'),
(18, 'Heti piac', 'piac', 'Tolna', 'Hőgyész', 2053, ''),
(19, 'Országos állat- és kirakodóvásár', 'vásár', 'Tolna', 'Hőgyész', 2053, ''),
(20, 'Őstermelői piac', 'termelői piac', 'Somogy', 'Kaposmérő', 7521, 'Rákóczi utca 41/a. Faluház előtti terület'),
(21, 'Élelmiszerpiac és vásárcsarnok', 'piac', 'Somogy', 'Kaposvár', 7400, 'Laktanya utca 5.'),
(22, 'Élelmiszerpiac', 'piac', 'Somogy', 'Kaposvár', 7400, 'Arany tér 7.'),
(23, 'Állandó heti vásár', 'vásár', 'Somogy', 'Kaposvár', 7400, 'Vásártéri utca 2.'),
(24, 'Kaposvári Nagypiac', 'piac és vásárcsarnok', 'Somogy', 'Kaposvár', 7400, 'Baross Gábor utca 5-13. '),
(25, 'Piac', 'piac', 'Somogy', 'Karád', 8676, 'Semmelweis téri közterület '),
(26, 'Országos kirakódóvásár', 'vásár', 'Somogy', 'Karád', 8676, 'Somogymeggyes útszakasz és a Vásártér utcaközötti terület'),
(27, 'Vásárcsarnok', 'piac és vásárcsarnok', 'Baranya', 'Komló', 7300, 'Berek utca 14.'),
(28, 'Piac', 'piac', 'Baranya', 'Magyarszék', 7396, 'Sporttelep önkormányzati tulajdonú területen (185 hrsz.)'),
(29, 'Élelmiszerpiac, vásár', 'piac', 'Somogy', 'Marcali', 8700, '1638/130 hrsz.'),
(30, 'Piaccsarnok', 'piac és vásárcsarnok', 'Somogy', 'Marcali', 8700, '1638/31 hrsz.'),
(31, 'Városi piac', 'piac', 'Baranya', 'Mohács', 7700, 'Városi piac kerítésen belüli része'),
(32, 'Országos állat- és kirakodóvásár', 'vásár', 'Baranya', 'Mohács', 7700, 'budapesti országút 3683/4, 16/1 és 3678. hrsz. '),
(33, 'Mozsgói piac', 'termelői piac', 'Baranya', 'Mozsgó', 7932, 'Batthyány utca, Sportpálya'),
(34, 'Élelmiszerpiac és kirakodóvásár', 'piac', 'Somogy', 'Nagyatád', 7500, 'Piac tér'),
(35, 'Piactér, vásárcsarnok', 'piac és vásárcsarnok', 'Somogy', 'Nagyatád', 7500, 'Kolozsvári utca'),
(36, 'Heti kirakodó és élelmiszerpiac', 'piac', 'Tolna', 'Ozora', 7086, 'Szabadság tér'),
(37, 'Országos kirakodóvásár', 'vásár', 'Tolna', 'Ozora', 7086, 'a benzinkút mögött'),
(38, 'Állat- és kirakodóvásár', 'vásár', 'Somogy', 'Ötvöskónyi', 7511, '0129/15 hrsz'),
(39, 'Hetipiac', 'piac', 'Tolna', 'Paks', 7030, 'Villany utca 2.'),
(40, 'Biópiac', 'biopiac', 'Baranya', 'Pécs', 7622, 'Bajcsy-Zsilinszky utca 25.'),
(41, 'Vásárcsarnok', 'vásárcsarnok', 'Baranya', 'Pécs', 7622, 'Bajcsy-Zsilinszky utca 25.'),
(42, 'Diana téri piac', 'piac', 'Baranya', 'Pécs', 7632, 'Diana tér'),
(43, 'Uránvárosi piac', 'piac', 'Baranya', 'Pécs', 7632, 'Hajnóczy utca 1.'),
(44, 'Vásártér  ', 'piac', 'Baranya', 'Pécs', 7632, 'Móra Ferenc utca '),
(45, 'Élelmiszerpiac és kirakodóvásár', 'piac', 'Somogy', 'Ságvár', 8654, 'Hrsz. 157, 158'),
(46, 'Kirakodóvásár', 'vásár', 'Somogy', 'Ságvár', 8654, 'Hrsz. 157, 158'),
(47, 'Piac', 'piac', 'Baranya', 'Sellye', 7960, 'Bodonyi Nándor utca'),
(48, 'Vásár', 'vásár', 'Baranya', 'Sellye', 7960, 'Sport utca déli részén lévő terület'),
(49, 'Piac, vásárcsarnok', 'piac és vásárcsarnok', 'Baranya', 'Siklós', 7800, 'Mária utca, Dózsa György utca és a Táncsics Mihály utcák'),
(50, 'Heti piac', 'piac', 'Tolna', 'Simontornya', 7081, 'Hunyadi utca'),
(51, 'Országos állat- és kirakodóvásár', 'vásár', 'Tolna', 'Simontornya', 7081, 'Arany János utca'),
(52, 'Siófoki Vásárcsarnok', 'vásárcsarnok', 'Somogy', 'Siófok', 8600, 'Vámház utca 2.'),
(53, 'Siófoki Bioudvar', 'biopiac', 'Somogy', 'Siófok', 8601, 'Széchenyi utca 6/a.'),
(54, 'Termelői piac és kézműves vásár', 'termelői piac', 'Somogy', 'Szántódpuszta', 8622, '70-es út mellett'),
(55, 'Helyi piac ', 'piac', 'Baranya', 'Szászvár', 7349, 'Faluház udvara'),
(56, 'Országos  kirakodó- és  autóvásár', 'vásár', 'Baranya', 'Szászvár', 7349, ''),
(57, 'Déli piac', 'piac', 'Tolna', 'Szekszárd', 7100, 'Béri Balogh Ádám utca'),
(58, 'Központi piac', 'piac', 'Tolna', 'Szekszárd', 7100, 'Várköz utca'),
(59, 'Szekszárdi Vásár', 'vásár', 'Tolna', 'Szekszárd', 7100, 'Aranytó utcai Vásártér (3785-3787 hrsz.)'),
(60, 'Piac, heti kirakodóvásár', 'piac', 'Baranya', 'Szigetvár', 7900, 'Istvánffy utca'),
(61, 'Országos állat- és kirakodóvásár', 'vásár', 'Baranya', 'Szigetvár', 7900, '960 hrsz. alatt nyilvántartott földterület'),
(62, 'Piac', 'piac', 'Somogy', 'Tab', 8660, 'Vörösmarty utca'),
(63, 'Állat- és kirakodóvásár', 'vásár', 'Somogy', 'Tab', 8660, 'Kossuth Lajos utca'),
(64, 'Városi piac', 'piac', 'Tolna', 'Tolna', 7130, 'Hősök tere 1.'),
(65, 'Hétközi piac', 'piac', 'Tolna', 'Tolna', 7130, 'Piactér'),
(66, 'Piac', 'piac', 'Somogy', 'Zamárdi', 8621, 'Siófoki út');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `nap`
--

CREATE TABLE `nap` (
  `id` int(3) NOT NULL,
  `nev` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- A tábla adatainak kiíratása `nap`
--

INSERT INTO `nap` (`id`, `nev`) VALUES
(1, 'hétfő'),
(2, 'kedd'),
(3, 'szerda'),
(4, 'csütörtök'),
(5, 'péntek'),
(6, 'szombat'),
(7, 'vasárnap');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `nyitvatartas`
--

CREATE TABLE `nyitvatartas` (
  `helyid` int(2) DEFAULT NULL,
  `napid` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- A tábla adatainak kiíratása `nyitvatartas`
--

INSERT INTO `nyitvatartas` (`helyid`, `napid`) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(1, 7),
(1, 6),
(5, 4),
(5, 3),
(5, 5),
(5, 1),
(5, 2),
(6, 6),
(7, 1),
(7, 2),
(7, 4),
(7, 3),
(7, 6),
(7, 5),
(8, 3),
(8, 6),
(9, 2),
(9, 5),
(10, 4),
(10, 2),
(10, 3),
(10, 6),
(10, 7),
(10, 5),
(11, 1),
(11, 2),
(11, 5),
(11, 3),
(11, 4),
(11, 6),
(12, 7),
(13, 7),
(14, 6),
(14, 3),
(14, 1),
(14, 2),
(14, 5),
(14, 4),
(15, 6),
(16, 6),
(16, 3),
(18, 5),
(18, 2),
(20, 6),
(21, 7),
(21, 3),
(21, 5),
(21, 6),
(21, 2),
(21, 4),
(24, 5),
(24, 2),
(24, 6),
(24, 7),
(24, 4),
(24, 3),
(25, 5),
(25, 3),
(25, 1),
(28, 3),
(28, 6),
(31, 5),
(31, 2),
(31, 6),
(31, 3),
(31, 4),
(31, 1),
(32, 6),
(35, 4),
(35, 2),
(35, 6),
(36, 5),
(36, 3),
(39, 2),
(39, 5),
(40, 4),
(40, 5),
(40, 6),
(41, 4),
(41, 5),
(41, 2),
(41, 1),
(41, 6),
(41, 3),
(42, 1),
(42, 2),
(42, 3),
(42, 4),
(42, 6),
(42, 7),
(42, 5),
(43, 3),
(43, 2),
(43, 1),
(43, 5),
(43, 4),
(43, 6),
(44, 5),
(44, 7),
(44, 3),
(44, 4),
(44, 2),
(44, 6),
(44, 1),
(46, 6),
(47, 3),
(47, 1),
(47, 5),
(47, 6),
(47, 7),
(47, 4),
(47, 2),
(48, 2),
(49, 3),
(49, 6),
(49, 5),
(49, 1),
(49, 2),
(49, 4),
(50, 4),
(50, 6),
(52, 6),
(52, 5),
(52, 2),
(52, 4),
(52, 3),
(52, 1),
(53, 3),
(54, 2),
(54, 3),
(55, 5),
(55, 6),
(55, 4),
(55, 3),
(56, 7),
(58, 1),
(58, 2),
(58, 4),
(58, 3),
(58, 6),
(58, 5),
(59, 7),
(60, 2),
(60, 3),
(60, 1),
(60, 6),
(60, 7),
(60, 4),
(60, 5),
(62, 3),
(62, 6),
(63, 3),
(64, 7),
(64, 5),
(64, 2),
(65, 5),
(65, 7),
(65, 2);

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `arusitohely`
--
ALTER TABLE `arusitohely`
  ADD PRIMARY KEY (`id`);

--
-- A tábla indexei `nap`
--
ALTER TABLE `nap`
  ADD PRIMARY KEY (`id`);

--
-- A tábla indexei `nyitvatartas`
--
ALTER TABLE `nyitvatartas`
  ADD KEY `fk_nyitvatartas_helyid` (`helyid`),
  ADD KEY `fk_nyitvatartas_napid` (`napid`);

--
-- A kiírt táblák AUTO_INCREMENT értéke
--

--
-- AUTO_INCREMENT a táblához `nap`
--
ALTER TABLE `nap`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Megkötések a kiírt táblákhoz
--

--
-- Megkötések a táblához `nyitvatartas`
--
ALTER TABLE `nyitvatartas`
  ADD CONSTRAINT `fk_nyitvatartas_helyid` FOREIGN KEY (`helyid`) REFERENCES `arusitohely` (`id`),
  ADD CONSTRAINT `fk_nyitvatartas_napid` FOREIGN KEY (`napid`) REFERENCES `nap` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
