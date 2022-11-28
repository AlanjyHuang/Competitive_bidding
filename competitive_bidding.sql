-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2022 年 11 月 28 日 09:31
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
-- 資料庫： `1211`
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
  `nowPrice` int(11) NOT NULL,
  `getMan` varchar(10) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 傾印資料表的資料 `上架`
--

INSERT INTO `上架` (`id`, `name`, `firstPrice`, `deadline`, `nowPrice`, `getMan`) VALUES
(1, 'chair', 50, '2022-11-28 06:39:39', 700, ''),
(2, 'happy nut', 0, '2022-11-28 06:50:19', 700, ''),
(3, 'coco', 100, '2022-11-28 06:54:44', 250, ''),
(4, 'coco', 100, '2022-11-28 07:25:19', 1239, ''),
(5, 'bin', 200, '2022-11-28 07:00:25', 2501, ''),
(6, 'binhappy', 200, '2022-11-28 07:25:59', 1239, ''),
(7, 'binhappy', 200, '2022-11-28 07:27:03', 1239, ''),
(8, 'binhappy1', 200, '2022-11-30 06:39:39', 44444, 'egg'),
(9, 'egg', 200, '2022-11-30 06:39:39', 44444, 'egg'),
(10, 'egg', 200, '2022-11-28 06:21:39', 200, ''),
(11, 'egg2', 200, '2022-11-28 06:30:39', 200, ''),
(12, 'egg2', 200, '2022-11-28 08:24:39', 44444, 'egg222'),
(13, 'binhappy2', 200, '2022-11-28 08:27:39', 400, '1211');

-- --------------------------------------------------------

--
-- 資料表結構 `下標`
--

CREATE TABLE `下標` (
  `id` int(11) NOT NULL,
  `UID` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `time` timestamp NOT NULL DEFAULT current_timestamp(),
  `成功` tinyint(1) NOT NULL,
  `product_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 傾印資料表的資料 `下標`
--

INSERT INTO `下標` (`id`, `UID`, `price`, `time`, `成功`, `product_id`) VALUES
(1, 108321007, 100, '2022-11-26 16:00:00', 0, 1),
(2, 108321007, 150, '2022-11-26 16:00:00', 0, 1),
(3, 108321007, 200, '2022-11-26 16:00:00', 0, 1),
(4, 108321007, 250, '2022-11-26 16:00:00', 0, 1),
(5, 108321007, 300, '2022-11-26 16:00:00', 0, 1),
(6, 108321008, 300, '2022-11-26 16:00:00', 0, 1),
(7, 1, 500, '2022-11-28 06:31:50', 0, 1),
(8, 108321007, 500, '2022-11-28 06:35:51', 0, 1),
(9, 108321007, 700, '2022-11-28 06:39:39', 0, 1),
(10, 108321007, 700, '2022-11-28 06:50:19', 0, 2),
(11, 108321007, 250, '2022-11-28 06:54:44', 0, 3),
(12, 22233, 2500, '2022-11-28 07:00:22', 0, 5),
(13, 22233, 2501, '2022-11-28 07:00:25', 0, 5),
(14, 111122220, 1239, '2022-11-28 07:25:19', 0, 4),
(15, 111122220, 1239, '2022-11-28 07:25:59', 0, 6),
(16, 111122220, 1239, '2022-11-28 07:27:03', 0, 7),
(17, 111122220, 1239, '2022-11-28 07:27:56', 0, 8),
(18, 111122220, 1239, '2022-11-28 07:34:44', 0, 8),
(19, 111122220, 1240, '2022-11-28 07:34:51', 0, 8),
(20, 111122220, 1240, '2022-11-28 07:35:35', 0, 8),
(21, 0, 1245, '2022-11-28 07:37:07', 0, 8),
(22, 0, 44444, '2022-11-28 07:39:15', 0, 8),
(23, 0, 44444, '2022-11-28 08:04:03', 0, 9),
(24, 0, 44444, '2022-11-28 08:23:16', 0, 9),
(25, 0, 44444, '2022-11-28 08:23:47', 0, 12),
(26, 0, 44444, '2022-11-28 08:24:01', 0, 12),
(27, 1211, 400, '2022-11-28 08:27:22', 0, 13);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `下標`
--
ALTER TABLE `下標`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
