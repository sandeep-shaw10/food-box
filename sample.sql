-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 16, 2020 at 04:01 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sample`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_table`
--

CREATE TABLE `admin_table` (
  `id` int(11) NOT NULL,
  `name` varchar(64) NOT NULL,
  `password` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin_table`
--

INSERT INTO `admin_table` (`id`, `name`, `password`) VALUES
(1, 'Aniruddha Sarkar', 'admin'),
(3, 'Ayush Jha', 'admin'),
(4, 'Sandeep Shaw', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `billing`
--

CREATE TABLE `billing` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `day` date NOT NULL,
  `money` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `billing`
--

INSERT INTO `billing` (`id`, `user_id`, `day`, `money`) VALUES
(1, 3, '0000-00-00', 360);

-- --------------------------------------------------------

--
-- Table structure for table `daily_sales`
--

CREATE TABLE `daily_sales` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `sold` int(11) NOT NULL,
  `income` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `sales_table`
--

CREATE TABLE `sales_table` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `orderby` varchar(64) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `number` varchar(32) NOT NULL,
  `name` varchar(64) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sales_table`
--

INSERT INTO `sales_table` (`id`, `user_id`, `orderby`, `date`, `number`, `name`, `quantity`, `price`, `amount`) VALUES
(4, 1, 'Sandeep', '2020-08-07 18:03:40', 'A001', 'Chicken Biryani', 1, 120, 120),
(5, 1, 'Sandeep', '2020-08-07 18:03:41', 'A001', 'Chicken Biryani', 1, 120, 120),
(6, 1, 'Sandeep', '2020-08-07 18:03:41', 'A001', 'Chicken Biryani', 2, 120, 240),
(7, 1, 'Sandeep', '2020-08-07 18:19:52', 'A002', 'Mutton Biryani', 2, 180, 360),
(8, 1, 'Sandeep', '2020-08-07 18:19:52', 'A003', 'Palak Paneer', 5, 60, 300),
(9, 19, 'Pal', '2020-08-07 18:35:12', 'A001', 'Chicken Biryani', 2, 120, 240),
(10, 19, 'Pal', '2020-08-07 18:35:12', 'A002', 'Mutton Biryani', 2, 180, 360),
(11, 19, 'Pal', '2020-08-07 18:35:12', 'A003', 'Palak Paneer', 5, 60, 300),
(12, 1, 'Sandeep', '2020-08-07 19:06:39', 'A003', 'Palak Paneer', 5, 60, 300),
(13, 1, 'Sandeep', '2020-08-07 19:08:00', 'A003', 'Palak Paneer', 5, 60, 300),
(14, 1, 'Sandeep', '2020-08-07 19:24:31', 'A003', 'Palak Paneer', 5, 60, 300),
(15, 1, 'Sandeep', '2020-08-16 11:53:27', 'A004', 'Indian Momo', 4, 60, 240),
(16, 1, 'Sandeep', '2020-08-16 12:11:31', 'A004', 'Indian Momo', 2, 60, 120),
(17, 1, 'Sandeep', '2020-08-16 12:24:52', 'A004', 'Indian Momo', 2, 60, 120),
(18, 1, 'Sandeep', '2020-08-16 12:24:52', 'A001', 'Chicken Biryani', 1, 120, 120),
(19, 1, 'Sandeep', '2020-08-16 12:37:39', 'A004', 'Indian Momo', 4, 60, 240),
(20, 1, 'Sandeep', '2020-08-16 12:37:39', 'A003', 'Palak Paneer', 5, 60, 300),
(21, 3, 'Ayush', '2020-08-16 19:23:19', 'A001', 'Chicken Biryani', 3, 120, 360),
(22, 3, 'Ayush', '2020-08-16 19:30:11', 'A001', 'Chicken Biryani', 3, 120, 360);

-- --------------------------------------------------------

--
-- Table structure for table `stock_table`
--

CREATE TABLE `stock_table` (
  `id` int(11) NOT NULL,
  `num` varchar(64) NOT NULL,
  `name` varchar(64) NOT NULL,
  `type` varchar(32) NOT NULL,
  `price` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stock_table`
--

INSERT INTO `stock_table` (`id`, `num`, `name`, `type`, `price`, `quantity`) VALUES
(2, 'A002', 'Mutton Biryani', 'South Indian', 180, 6),
(4, 'A004', 'Indian Momo', 'North Indian', 60, 18);

-- --------------------------------------------------------

--
-- Table structure for table `user_cart`
--

CREATE TABLE `user_cart` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `item_num` varchar(64) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user_table`
--

CREATE TABLE `user_table` (
  `user_id` int(11) NOT NULL,
  `username` varchar(64) NOT NULL,
  `user_password` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_table`
--

INSERT INTO `user_table` (`user_id`, `username`, `user_password`) VALUES
(1, 'Sandeep Shaw', 'shaw'),
(2, 'Anirudhha Sarkar', 'sarkar'),
(3, 'Ayush jha', 'jha'),
(4, 'Ram Das', 'qwerty'),
(9, 'Mohan nath', 'nath'),
(14, 'Mohan Nath', 'mohan'),
(15, 'Deepak thakey', 'deepak'),
(17, 'Vinayak Pal', 'vinayak'),
(18, 'Pankaj Tripathi', 'pankaj'),
(19, 'Pal Arun', 'arun');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_table`
--
ALTER TABLE `admin_table`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `billing`
--
ALTER TABLE `billing`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `daily_sales`
--
ALTER TABLE `daily_sales`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sales_table`
--
ALTER TABLE `sales_table`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stock_table`
--
ALTER TABLE `stock_table`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_cart`
--
ALTER TABLE `user_cart`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_table`
--
ALTER TABLE `user_table`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_table`
--
ALTER TABLE `admin_table`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `billing`
--
ALTER TABLE `billing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `daily_sales`
--
ALTER TABLE `daily_sales`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sales_table`
--
ALTER TABLE `sales_table`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `stock_table`
--
ALTER TABLE `stock_table`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `user_cart`
--
ALTER TABLE `user_cart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `user_table`
--
ALTER TABLE `user_table`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
