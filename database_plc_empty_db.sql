-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 19, 2022 at 04:57 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `database_plc`
--

-- --------------------------------------------------------

--
-- Table structure for table `input_table`
--

CREATE TABLE `input_table` (
  `ID_Input` int(11) NOT NULL,
  `Data_Input` binary(255) NOT NULL,
  `Time_Input` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `plc_controller`
--

CREATE TABLE `plc_controller` (
  `ID_PLC` int(11) NOT NULL,
  `IP_Address` varchar(50) NOT NULL,
  `RACK` int(11) NOT NULL,
  `SLOT` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tag`
--

CREATE TABLE `tag` (
  `ID_Tag` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Data_Type` varchar(50) NOT NULL,
  `Address_start_byte` int(11) NOT NULL,
  `Address_start_bit` int(11) NOT NULL,
  `ID_PLC` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tag_input`
--

CREATE TABLE `tag_input` (
  `ID_Tag` int(11) NOT NULL,
  `ID_Input` int(11) NOT NULL,
  `Value_Tag` binary(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `input_table`
--
ALTER TABLE `input_table`
  ADD PRIMARY KEY (`ID_Input`);

--
-- Indexes for table `plc_controller`
--
ALTER TABLE `plc_controller`
  ADD PRIMARY KEY (`ID_PLC`);

--
-- Indexes for table `tag`
--
ALTER TABLE `tag`
  ADD PRIMARY KEY (`ID_Tag`),
  ADD KEY `ID_PLC` (`ID_PLC`);

--
-- Indexes for table `tag_input`
--
ALTER TABLE `tag_input`
  ADD KEY `ID_Tag` (`ID_Tag`),
  ADD KEY `ID_Input` (`ID_Input`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `input_table`
--
ALTER TABLE `input_table`
  MODIFY `ID_Input` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `plc_controller`
--
ALTER TABLE `plc_controller`
  MODIFY `ID_PLC` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tag`
--
ALTER TABLE `tag`
  MODIFY `ID_Tag` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tag`
--
ALTER TABLE `tag`
  ADD CONSTRAINT `tag_ibfk_1` FOREIGN KEY (`ID_PLC`) REFERENCES `plc_controller` (`ID_PLC`) ON UPDATE CASCADE;

--
-- Constraints for table `tag_input`
--
ALTER TABLE `tag_input`
  ADD CONSTRAINT `tag_input_ibfk_1` FOREIGN KEY (`ID_Tag`) REFERENCES `tag` (`ID_Tag`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tag_input_ibfk_2` FOREIGN KEY (`ID_Input`) REFERENCES `input_table` (`ID_Input`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
