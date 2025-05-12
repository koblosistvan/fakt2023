-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2025. Ápr 14. 11:37
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
-- Adatbázis: `tresz`
--

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `vizsga`
--

CREATE TABLE `vizsga` (
  `id` int(11) NOT NULL,
  `vizsgazoid` int(11) NOT NULL,
  `pontszam` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `vizsgazo`
--

CREATE TABLE `vizsgazo` (
  `id` int(11) NOT NULL,
  `nev` varchar(255) DEFAULT NULL,
  `osztaly` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- A tábla adatainak kiíratása `vizsgazo`
--

INSERT INTO `vizsgazo` (`id`, `nev`, `osztaly`) VALUES
(1, 'Bogdán Samu Milán', '12A'),
(2, 'Csesznegi Andor', '12A'),
(3, 'Soós Márton', '12A'),
(4, 'Treszl Marcell', '12A'),
(5, 'Németh Kristóf Soma', '12A'),
(6, 'Bodor Zoltán Áron', '12A'),
(7, 'Erős Dominik', '12A'),
(8, 'Gubody Ádám Balázs', '12A'),
(9, 'Hegedűs Zoltán', '12A'),
(10, 'Nagy Balázs', '12A'),
(17, 'Griffin Péter', '71A'),
(18, 'Hornyák Kevin', '12C'),
(19, 'Hormyák Kevi', '12C'),
(20, 'Stein Bünde', '12C'),
(21, 'Petrekin Bence', '12D'),
(22, 'Gelbmann Bence', '12E'),
(23, 'Hermann Máté', '12E'),
(24, 'Miski Ferenc', '12E');

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `vizsga`
--
ALTER TABLE `vizsga`
  ADD PRIMARY KEY (`id`);

--
-- A tábla indexei `vizsgazo`
--
ALTER TABLE `vizsgazo`
  ADD PRIMARY KEY (`id`);

--
-- A kiírt táblák AUTO_INCREMENT értéke
--

--
-- AUTO_INCREMENT a táblához `vizsga`
--
ALTER TABLE `vizsga`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT a táblához `vizsgazo`
--
ALTER TABLE `vizsgazo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
