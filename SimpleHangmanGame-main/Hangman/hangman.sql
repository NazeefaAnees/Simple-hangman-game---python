-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 15, 2021 at 04:59 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hangman`
--

-- --------------------------------------------------------

--
-- Table structure for table `playerinfo`
--

CREATE TABLE `playerinfo` (
  `gameID` int(4) UNSIGNED ZEROFILL NOT NULL,
  `date` varchar(20) NOT NULL,
  `time` varchar(10) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `mode` varchar(10) NOT NULL,
  `word` varchar(30) DEFAULT NULL,
  `turns` int(5) DEFAULT NULL,
  `turnsUsed` int(3) DEFAULT NULL,
  `hintGiven` varchar(4) DEFAULT NULL,
  `winORloss` varchar(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `playerinfo`
--

INSERT INTO `playerinfo` (`gameID`, `date`, `time`, `name`, `mode`, `word`, `turns`, `turnsUsed`, `hintGiven`, `winORloss`) VALUES
(0001, '15 Dec 2021', '18:50', 'NAZEEFA', 'EASY', 'DOCTOR', 6, 3, 'YES', 'WIN'),
(0002, '15 Dec 2021', '19:16', 'NAZEEFA', 'MEDIUM', 'ELEVEN', 6, 1, 'YES', 'WIN'),
(0003, '15 Dec 2021', '19:28', 'NAZEEFA', 'HARD', 'MASSEUSE', 8, 8, 'NO', 'LOSS'),
(0004, '15 Dec 2021', '20:04', 'JAKE', 'EASY', 'NAIL', 4, 4, 'YES', 'LOSS'),
(0005, '15 Dec 2021', '20:04', 'BELLA', 'HARD', 'ABSURD', 6, 6, 'NO', 'LOSS'),
(0006, '15 Dec 2021', '20:11', 'AMY', 'EASY', 'GOAT', 4, 2, 'YES', 'WIN'),
(0007, '15 Dec 2021', '20:12', 'AMY', 'HARD', 'JOGGING', 7, 4, 'YES', 'WIN'),
(0008, '15 Dec 2021', '20:12', 'AMY', 'EASY', 'PARK', 4, 4, 'NO', 'LOSS');

-- --------------------------------------------------------

--
-- Table structure for table `playerinfo_persession`
--

CREATE TABLE `playerinfo_persession` (
  `gameID` int(4) UNSIGNED ZEROFILL NOT NULL,
  `date` varchar(20) NOT NULL,
  `time` varchar(10) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `mode` varchar(10) DEFAULT NULL,
  `word` varchar(30) DEFAULT NULL,
  `turns` int(5) DEFAULT NULL,
  `turnsUsed` int(3) DEFAULT NULL,
  `hintGiven` varchar(4) DEFAULT NULL,
  `winORloss` varchar(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `playerinfo`
--
ALTER TABLE `playerinfo`
  ADD PRIMARY KEY (`gameID`);

--
-- Indexes for table `playerinfo_persession`
--
ALTER TABLE `playerinfo_persession`
  ADD PRIMARY KEY (`gameID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `playerinfo`
--
ALTER TABLE `playerinfo`
  MODIFY `gameID` int(4) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `playerinfo_persession`
--
ALTER TABLE `playerinfo_persession`
  MODIFY `gameID` int(4) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
