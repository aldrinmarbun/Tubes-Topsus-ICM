-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 15, 2020 at 05:07 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_python`
--

-- --------------------------------------------------------

--
-- Table structure for table `blockchain`
--

CREATE TABLE `blockchain` (
  `id` varchar(100) NOT NULL,
  `data` varchar(100) NOT NULL,
  `timestamp` varchar(100) NOT NULL,
  `prevhash` varchar(100) NOT NULL,
  `hash` varchar(100) NOT NULL,
  `nonce` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `blockchain`
--

INSERT INTO `blockchain` (`id`, `data`, `timestamp`, `prevhash`, `hash`, `nonce`) VALUES
('1', 'budi', '2020-05-15 09:23:01.244626', '0', '5a1a978b0e0500357eed3e3fa0bdfd6bf6a3c6dda7505f3b879b1a24', '12156'),
('2', 'tono', '2020-05-15 09:23:01.247730', '5a1a978b0e0500357eed3e3fa0bdfd6bf6a3c6dda7505f3b879b1a24', '0dcdeb7426976eb125f967246ba5adcd761133b314c6bdaa0207ebf7', '2754072'),
('3', 'dwi', '2020-05-15 09:23:01.250614', '0dcdeb7426976eb125f967246ba5adcd761133b314c6bdaa0207ebf7', 'e4dfb7acedd9bd2768ec37e33863aeaf30ed9f491c711102295d98b4', '2483393'),
('4', 'dion', '2020-05-15 09:23:30.366034', 'e4dfb7acedd9bd2768ec37e33863aeaf30ed9f491c711102295d98b4', 'b66233e504ffdb63354425aab085d131eb249648d661d6f7bab84bd3', '256205'),
('5', 'febrianto', '2020-05-15 09:23:30.369142', 'b66233e504ffdb63354425aab085d131eb249648d661d6f7bab84bd3', 'e23307958c9be02b5781d2d8f4633839d8c33d7b63e91979287f09e3', '1644217'),
('6', 'jumi', '2020-05-15 09:23:30.371133', 'e23307958c9be02b5781d2d8f4633839d8c33d7b63e91979287f09e3', '6252917734fa5852412d1ced8981ad9b5f8837c8552578d55f0fe9d0', '1863083');

-- --------------------------------------------------------

--
-- Table structure for table `data_ins`
--

CREATE TABLE `data_ins` (
  `id` varchar(100) NOT NULL,
  `data` varchar(100) NOT NULL,
  `timestamp` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `data_pool`
--

CREATE TABLE `data_pool` (
  `id` varchar(100) NOT NULL,
  `data` varchar(100) NOT NULL,
  `timestamp` varchar(100) NOT NULL,
  `prevhash` varchar(100) NOT NULL,
  `hash` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blockchain`
--
ALTER TABLE `blockchain`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `data_ins`
--
ALTER TABLE `data_ins`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `data_pool`
--
ALTER TABLE `data_pool`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
