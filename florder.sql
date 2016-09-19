-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 2016-09-19 09:30:57
-- 服务器版本： 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `florder`
--

-- --------------------------------------------------------

--
-- 表的结构 `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=28 ;

--
-- 转存表中的数据 `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add seller', 7, 'add_seller'),
(20, 'Can change seller', 7, 'change_seller'),
(21, 'Can delete seller', 7, 'delete_seller'),
(22, 'Can add dish', 8, 'add_dish'),
(23, 'Can change dish', 8, 'change_dish'),
(24, 'Can delete dish', 8, 'delete_dish'),
(25, 'Can add table', 9, 'add_table'),
(26, 'Can change table', 9, 'change_table'),
(27, 'Can delete table', 9, 'delete_table');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- 转存表中的数据 `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$20000$qjEWbRduMN6B$tSKk0o52rVB3lD0zPRRgYK2HgN/HcJJlDL5TULErznk=', '2016-03-11 08:43:19', 1, 'root', '', '', '', 1, 1, '2016-03-05 01:29:18');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=10 ;

--
-- 转存表中的数据 `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(8, 'fl', 'dish'),
(7, 'fl', 'seller'),
(9, 'fl', 'table'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- 表的结构 `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=11 ;

--
-- 转存表中的数据 `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2016-03-05 01:29:08'),
(2, 'auth', '0001_initial', '2016-03-05 01:29:09'),
(3, 'admin', '0001_initial', '2016-03-05 01:29:09'),
(4, 'contenttypes', '0002_remove_content_type_name', '2016-03-05 01:29:09'),
(5, 'auth', '0002_alter_permission_name_max_length', '2016-03-05 01:29:09'),
(6, 'auth', '0003_alter_user_email_max_length', '2016-03-05 01:29:09'),
(7, 'auth', '0004_alter_user_username_opts', '2016-03-05 01:29:09'),
(8, 'auth', '0005_alter_user_last_login_null', '2016-03-05 01:29:09'),
(9, 'auth', '0006_require_contenttypes_0002', '2016-03-05 01:29:09'),
(10, 'sessions', '0001_initial', '2016-03-05 01:29:09');

-- --------------------------------------------------------

--
-- 表的结构 `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('7bynej161v4hhnjdkj5gj7ng0mnua0tb', 'YWViY2Q2MzQ3NzQ4OGI3ZjI4ZjViNzA0ODVjY2ViZDU2Y2Q4YmEzZjp7Il9hdXRoX3VzZXJfaGFzaCI6ImUxNWQ3MzU3OTFiOTM1YjQ1ZjgyNTZjMmU1ZjVjZjdjMjRkY2I5YTkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-03-25 08:43:19');

-- --------------------------------------------------------

--
-- 表的结构 `fl_customer`
--

CREATE TABLE IF NOT EXISTS `fl_customer` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `name` char(21) NOT NULL COMMENT '姓名',
  `mobile` char(11) NOT NULL COMMENT '手机号码',
  `avatar` varchar(255) NOT NULL COMMENT '头像地址',
  `wx` char(32) NOT NULL COMMENT '微信登录识别',
  `create_time` int(11) unsigned NOT NULL COMMENT '注册时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=9 ;

--
-- 转存表中的数据 `fl_customer`
--

INSERT INTO `fl_customer` (`id`, `name`, `mobile`, `avatar`, `wx`, `create_time`) VALUES
(6, '111', '11111', 'http://sfault-avatar.b0.upaiyun.com/927/036/92703636-5603f678d2c7c_huge256', '0', 1465817814),
(7, 'a1', '111', 'http://sfault-avatar.b0.upaiyun.com/927/036/92703636-5603f678d2c7c_huge256', '0', 1465822720),
(8, 'a2', '123', 'http://sfault-avatar.b0.upaiyun.com/927/036/92703636-5603f678d2c7c_huge256', '0', 1465822751);

-- --------------------------------------------------------

--
-- 表的结构 `fl_dish`
--

CREATE TABLE IF NOT EXISTS `fl_dish` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seller` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `dishname` varchar(50) NOT NULL,
  `dishphoto` varchar(100) NOT NULL,
  `dishprice` varchar(50) NOT NULL,
  `dishintroduce` longtext NOT NULL,
  `dishkind` varchar(50) NOT NULL,
  `add_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=16 ;

--
-- 转存表中的数据 `fl_dish`
--

INSERT INTO `fl_dish` (`id`, `seller`, `username`, `dishname`, `dishphoto`, `dishprice`, `dishintroduce`, `dishkind`, `add_time`) VALUES
(1, 10001, 'a1', '孜然炒肉', 'f65ad46095ba16ed28ced5040b5f39f6.jpg', '18', '44', 'cold', '2016-03-05 01:36:26'),
(2, 10001, 'a1', '红烧肉', 'f65ad46095ba16ed28ced5040b5f39f6.jpg', '237', '', 'hot', '2016-03-05 01:38:51'),
(3, 10001, 'a1', '奶昔', 'f65ad46095ba16ed28ced5040b5f39f6.jpg', '8', '', 'dessert', '2016-03-05 01:39:29'),
(4, 10002, 'b029', '土豆片', 'f65ad46095ba16ed28ced5040b5f39f6.jpg', '15', '香辣土豆片', 'hot', '2016-03-05 01:44:26'),
(5, 10002, 'b029', '兰州拉面', '899219351939813015.jpg', '10', '来自兰州的拉面', 'main', '2016-03-05 01:45:07');

-- --------------------------------------------------------

--
-- 表的结构 `fl_order`
--

CREATE TABLE IF NOT EXISTS `fl_order` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `seller` int(10) unsigned NOT NULL,
  `table_id` smallint(5) unsigned NOT NULL,
  `dish` varchar(255) NOT NULL COMMENT '1,2,3\ndish_id1, dish_id2',
  `customer` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '0 表示未登陆使用',
  `subscribe` tinyint(2) NOT NULL DEFAULT '0' COMMENT '0 非预约\n1 预约',
  `sub_time` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '预约时间',
  `create_time` int(10) unsigned NOT NULL COMMENT '下订单的时间',
  `status` tinyint(2) unsigned NOT NULL DEFAULT '0' COMMENT '0 无效/取消\n1 待制作\n2 待配送\n3 已配送',
  `finish_time` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '订单完成时间（取消/已配送）',
  `total_price` mediumint(8) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`,`seller`,`customer`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=51 ;

--
-- 转存表中的数据 `fl_order`
--

INSERT INTO `fl_order` (`id`, `seller`, `table_id`, `dish`, `customer`, `subscribe`, `sub_time`, `create_time`, `status`, `finish_time`, `total_price`) VALUES
(1, 10002, 20, '1,2,3', 0, 0, 0, 0, 0, 0, 0),
(2, 10002, 20, '1,2,3', 0, 0, 1456083898, 1456064048, 0, 0, 0),
(3, 10002, 20, '1,2,3', 0, 1, 1456083898, 1456064097, 0, 0, 0),
(4, 10002, 20, '1,12,23', 0, 1, 1456083898, 1456115505, 0, 0, 0),
(5, 10002, 20, '1,12,23', 0, 1, 1456083898, 1456115550, 0, 0, 0),
(6, 10002, 20, '1,12,23', 0, 1, 1456083898, 1456115570, 0, 0, 0),
(7, 10002, 20, '1,12,23', 0, 1, 1456083898, 1456115585, 0, 0, 772),
(12, 111, 112, '3-1', 0, 0, 0, 1456840841, 1, 1457339739, 601),
(13, 111, 111, '3-2,4-2,5-2', 0, 0, 0, 1456841182, 1, 1457339740, 600),
(14, 111, 90, '1-1,2-2,3-3,4-4,5-5', 0, 0, 0, 1456841393, 1, 1457339742, 599),
(15, 111, 1, '3-3,4-1,5-1', 0, 1, 1456840000, 1456841506, 1, 1457145507, 601),
(16, 111, 2, '1-3,2-3,3-3,4-3,5-3', 1, 1, 1456840000, 1456926244, 1, 1457852662, 400),
(17, 111, 111, '3-3,4-1,5-1', 1, 1, 1456840000, 1456841506, 1, 1457152835, 600),
(18, 111, 111, '3-3,4-1,5-1', 0, 0, 0, 1456841506, 1, 1457328914, 599),
(19, 111, 111, '3-3,4-1,5-1', 0, 1, 1456840000, 1456841506, 1, 1457145507, 598),
(20, 111, 111, '3-3,4-1,5-1', 0, 1, 1456840000, 1456841506, 1, 1457145507, 597),
(21, 111, 111, '3-3,4-1,5-1', 0, 1, 1456840000, 1456841506, 1, 1457145507, 596),
(22, 111, 111, '3-3,4-1,5-1', 0, 1, 1456840000, 1456841506, 1, 1457145507, 595),
(23, 111, 111, '3-3,4-1,5-1', 0, 1, 1456840000, 1456841506, 1, 1457145507, 594),
(24, 111, 111, '3-3,4-1,5-1', 0, 1, 1456840000, 1456841506, 1, 1457145507, 593),
(25, 111, 111, '3-3,4-1,5-1', 0, 1, 1456840000, 1456841506, 1, 1457145507, 601),
(26, 111, 111, '3-3,4-1,5-1', 0, 1, 1456840000, 1456841506, 1, 1457145507, 601),
(27, 111, 111, '3-3,4-1,5-1', 0, 1, 1456840000, 1456841506, 1, 1457145507, 601),
(28, 111, 111, '3-3,4-1,5-1', 0, 1, 1456840000, 1456841506, 1, 1457145507, 601),
(29, 111, 111, '3-3,4-1,5-1', 0, 1, 1456840000, 1456841506, 1, 1457145507, 601),
(32, 111, 111, '3-3,4-1,5-1', 0, 0, 0, 1456841506, 1, 1457328914, 599),
(35, 111, 2, '1-3,2-3,3-3,4-3,5-3', 1, 1, 1456840000, 1456926244, 1, 1457852663, 400),
(36, 111, 2, '1-3,2-3,3-3,4-3,5-3', 1, 1, 1456840000, 1456926244, 0, 0, 400),
(37, 111, 2, '1-3,2-3,3-3,4-3,5-3', 1, 1, 1456840000, 1456926244, 0, 0, 400),
(38, 111, 2, '1-3,2-3,3-3,4-3,5-3', 1, 1, 1456840000, 1456926244, 0, 0, 400),
(39, 111, 2, '1-3,2-3,3-3,4-3,5-3', 1, 1, 1456840000, 1456926244, 0, 0, 400),
(40, 111, 2, '1-3,2-3,3-3,4-3,5-3', 1, 1, 1456840000, 1456926244, 0, 0, 400),
(41, 111, 2, '1-3,2-3,3-3,4-3,5-3', 1, 1, 1456840000, 1456926244, 1, 1457330725, 400),
(44, 111, 112, '3-1', 0, 0, 0, 1456840841, 1, 1457339742, 601),
(45, 111, 111, '3-2,4-2,5-2', 0, 0, 0, 1456841182, 1, 1457339743, 600),
(46, 111, 90, '1-1,2-2,3-3,4-4,5-5', 0, 0, 0, 1456841393, 1, 1465654572, 599),
(47, 10001, 112, '3-1', 0, 0, 0, 1456840841, 1, 1465818795, 601),
(48, 111, 111, '3-2,4-2,5-2', 0, 0, 0, 1456841182, 1, 1457852667, 600),
(49, 111, 90, '1-3,2-3,3-3,4-3,5-3', 0, 0, 0, 1456841393, 1, 1457330893, 599),
(50, 10001, 1, '2-5', 0, 0, 0, 1465821974, 0, 0, 111);

-- --------------------------------------------------------

--
-- 表的结构 `fl_seller`
--

CREATE TABLE IF NOT EXISTS `fl_seller` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seller` int(11) DEFAULT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `isfgpwd` tinyint(1) NOT NULL,
  `resname` longtext NOT NULL,
  `resaddress` longtext NOT NULL,
  `resphone` longtext NOT NULL,
  `resphoto` varchar(100) NOT NULL,
  `resintroduce` longtext NOT NULL,
  `resopentime` longtext NOT NULL,
  `resnotice` longtext NOT NULL,
  `resother` longtext NOT NULL,
  `add_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=19 ;

--
-- 转存表中的数据 `fl_seller`
--

INSERT INTO `fl_seller` (`id`, `seller`, `username`, `password`, `email`, `isfgpwd`, `resname`, `resaddress`, `resphone`, `resphoto`, `resintroduce`, `resopentime`, `resnotice`, `resother`, `add_time`) VALUES
(1, 10001, 'a1', '111', '1@1.com', 0, '11', '11', '11', 'touxiang.jpg', '', '11', '', '', '2016-03-05 01:31:13'),
(2, 10002, 'b029', '123', '2@2.com', 0, '123', '123', '123', '899219351939813015.jpg', '', '10:00-20:00', '', '', '2016-03-05 01:39:47');

-- --------------------------------------------------------

--
-- 表的结构 `fl_table`
--

CREATE TABLE IF NOT EXISTS `fl_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seller` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `tablenum` varchar(50) NOT NULL,
  `tableperson` varchar(50) NOT NULL,
  `add_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- 限制导出的表
--

--
-- 限制表 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- 限制表 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- 限制表 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- 限制表 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
