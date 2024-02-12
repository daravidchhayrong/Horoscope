-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 18, 2022 at 08:32 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `final_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `kh`
--

CREATE TABLE `kh` (
  `id` int(45) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `DOB` varchar(255) DEFAULT NULL,
  `sign` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kh`
--

INSERT INTO `kh` (`id`, `name`, `DOB`, `sign`) VALUES
(1, 'Daravid', '11/30/03', 'Goat'),
(2, 'Test', '4/17/02', 'Horse');

-- --------------------------------------------------------

--
-- Table structure for table `zodiac`
--

CREATE TABLE `zodiac` (
  `id` int(45) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `DOB` varchar(255) DEFAULT NULL,
  `sign` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `zodiac`
--

INSERT INTO `zodiac` (`id`, `name`, `DOB`, `sign`) VALUES
(1, 'Daravid', '11/30/03', 'Sagittarius'),
(2, 'Test', '4/17/02', 'Aries');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `kh`
--
ALTER TABLE `kh`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `zodiac`
--
ALTER TABLE `zodiac`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `kh`
--
ALTER TABLE `kh`
  MODIFY `id` int(45) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `zodiac`
--
ALTER TABLE `zodiac`
  MODIFY `id` int(45) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
