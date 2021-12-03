-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 03, 2021 at 12:26 PM
-- Server version: 10.3.31-MariaDB-0ubuntu0.20.04.1
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `university`
--

-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

CREATE TABLE `faculty` (
  `faculty_ID` int(11) NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  `admin` varchar(20) DEFAULT NULL,
  `fundation_year` char(4) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `faculty`
--

INSERT INTO `faculty` (`faculty_ID`, `name`, `admin`, `fundation_year`, `address`) VALUES
(1, 'computer', 'Dr Dori', '1390', 'Tehran'),
(2, 'electronic', 'Dr Mohammadi', '1390', 'Isfahan'),
(3, 'mathematics', 'Dr Karimi', '1380', 'Shiraz'),
(4, 'architecture', 'Mr Akbari', '1399', 'Tehran'),
(5, 'data science', 'Mr Shahmoradi', '1400', 'Mashhad'),
(6, 'chemistry', 'Dr Sharifi', '1395', 'Tehran');

-- --------------------------------------------------------

--
-- Table structure for table `field`
--

CREATE TABLE `field` (
  `field_ID` int(11) NOT NULL,
  `field_name` varchar(30) DEFAULT NULL,
  `orientation` varchar(50) DEFAULT NULL,
  `grade` varchar(30) DEFAULT NULL,
  `faculty_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `field`
--

INSERT INTO `field` (`field_ID`, `field_name`, `orientation`, `grade`, `faculty_ID`) VALUES
(1, 'computer', 'software', 'bachelor', 1),
(2, 'computer', 'hardware', 'bachelor', 1),
(3, 'computer', 'maching learning', 'master', 5),
(4, 'mathematics', 'pure mathematics', 'bachelor', 3),
(5, 'art', '3D', 'master', 4),
(6, 'electronic', 'robotic', 'master', 2),
(7, 'data science', 'image processing', 'bachelor', 5),
(8, 'computer', 'parallel processing', 'master', 1),
(9, 'chemistry', 'pure chemistry', 'bachelor', 6);

-- --------------------------------------------------------

--
-- Table structure for table `professors`
--

CREATE TABLE `professors` (
  `professor_ID` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `family` varchar(20) DEFAULT NULL,
  `degree` varchar(30) DEFAULT NULL,
  `faculty_member` bit(1) DEFAULT NULL,
  `faculty_ID` int(11) DEFAULT NULL,
  `phone` char(20) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `professors`
--

INSERT INTO `professors` (`professor_ID`, `name`, `family`, `degree`, `faculty_member`, `faculty_ID`, `phone`, `address`) VALUES
(1, 'Mohammad', 'Dori', 'dr', b'1', 1, '09013128010', 'Tehran'),
(2, 'Salar', 'Sharifi', 'dr', b'1', 5, '09920615020', 'Tehran'),
(3, 'Hamed', 'Azizi', 'master', b'0', 6, '09112223333', 'Isfahan'),
(4, 'Amir', 'Adibi', 'master', b'1', 4, '09123456789', 'Shiraz'),
(5, 'Reza', 'Mohammadi', 'dr', b'0', 3, '09111111111', 'Mashhad'),
(6, 'Farshid', 'Sameri', 'master', b'0', 4, '09987654321', 'Tehran'),
(7, 'Ehsan', 'Naseri', 'dr', b'1', 2, '09222222222', 'Isfahan');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `student_ID` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `family` varchar(20) DEFAULT NULL,
  `field_ID` int(11) NOT NULL,
  `entering_year` char(4) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `average` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`student_ID`, `name`, `family`, `field_ID`, `entering_year`, `address`, `average`) VALUES
(1, 'Mohammad', 'Dori', 1, '1400', 'Tehran', 20),
(2, 'Ali', 'Mohammad', 1, '1390', 'Tehran', 19),
(3, 'Ali', 'Adibi', 4, '1395', 'Isfahan', 10),
(4, 'Salar', 'Sharifi', 5, '1401', 'Isfahan', 5),
(5, 'Mohammad', 'Azizi', 2, '1399', 'Shiraz', 18.75),
(6, 'Sara', 'Nasiri', 3, '1398', 'Tabriz', 13),
(7, 'Nazanin', 'Dori', 3, '1400', 'Mashhad', 12.88),
(8, 'Amir', 'Amiri', 6, '1395', 'Guilan', 19.93),
(9, 'Reza', 'Talebi', 6, '1395', 'Yazd', 11),
(10, 'Reza', 'Dori', 6, '1389', 'Qum', 10.5),
(11, 'Mohammad', 'Dori', 5, '1397', 'Isfahan', 14.2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `faculty`
--
ALTER TABLE `faculty`
  ADD PRIMARY KEY (`faculty_ID`);

--
-- Indexes for table `field`
--
ALTER TABLE `field`
  ADD PRIMARY KEY (`field_ID`),
  ADD KEY `faculty_ID` (`faculty_ID`);

--
-- Indexes for table `professors`
--
ALTER TABLE `professors`
  ADD PRIMARY KEY (`professor_ID`),
  ADD KEY `faculty_ID` (`faculty_ID`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`student_ID`),
  ADD KEY `field_ID` (`field_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `professors`
--
ALTER TABLE `professors`
  MODIFY `professor_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `student_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `field`
--
ALTER TABLE `field`
  ADD CONSTRAINT `field_ibfk_1` FOREIGN KEY (`faculty_ID`) REFERENCES `faculty` (`faculty_ID`);

--
-- Constraints for table `professors`
--
ALTER TABLE `professors`
  ADD CONSTRAINT `professors_ibfk_1` FOREIGN KEY (`faculty_ID`) REFERENCES `faculty` (`faculty_ID`);

--
-- Constraints for table `students`
--
ALTER TABLE `students`
  ADD CONSTRAINT `students_ibfk_1` FOREIGN KEY (`field_ID`) REFERENCES `field` (`field_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
