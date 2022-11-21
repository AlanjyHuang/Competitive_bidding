-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2022 年 11 月 21 日 09:35
-- 伺服器版本： 10.4.24-MariaDB
-- PHP 版本： 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `competitive_bidding`
--

-- --------------------------------------------------------

--
-- 資料表結構 `上架`
--

CREATE TABLE `上架` (
  `id` int(11) NOT NULL,
  `name` text COLLATE utf8_unicode_ci NOT NULL,
  `firstPrice` int(11) NOT NULL,
  `deadline` timestamp NOT NULL DEFAULT current_timestamp(),
  `nowPrice` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 傾印資料表的資料 `上架`
--

INSERT INTO `上架` (`id`, `name`, `firstPrice`, `deadline`, `nowPrice`) VALUES
(1, 'asdasd', 100, '2022-11-20 16:00:00', 300),
(2, 'asdasd', 100, '2022-11-21 08:14:53', 100);

-- --------------------------------------------------------

--
-- 資料表結構 `下標`
--

CREATE TABLE `下標` (
  `id` int(11) NOT NULL,
  `UID` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `time` timestamp NOT NULL DEFAULT current_timestamp(),
  `成功` bit(1) NOT NULL DEFAULT b'0',
  `product_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 傾印資料表的資料 `下標`
--

INSERT INTO `下標` (`id`, `UID`, `price`, `time`, `成功`, `product_id`) VALUES
(1, 1, 10, '2022-11-20 17:39:00', b'0', 1),
(2, 1, 20, '2022-11-20 20:16:21', b'0', 2),
(3, 1, 20, '2022-11-21 08:03:40', b'0', 3),
(4, 2, 13, '2022-11-21 08:07:27', b'0', 1);

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `上架`
--
ALTER TABLE `上架`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `下標`
--
ALTER TABLE `下標`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `上架`
--
ALTER TABLE `上架`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `下標`
--
ALTER TABLE `下標`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
