
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;


CREATE TABLE IF NOT EXISTS `bank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `bank` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `country` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `country` (`country`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;




CREATE TABLE IF NOT EXISTS `bill` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `document_id` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `document_date` date DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `document_status` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `document_origin_id` int(11) DEFAULT NULL,
  `document_origin` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `memo` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `total_gross` float DEFAULT NULL,
  `total_discount` float DEFAULT NULL,
  `total_tax` float DEFAULT NULL,
  `total_net` float DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `currency_id` int(11) DEFAULT NULL,
  `entity_id` int(11) DEFAULT NULL,
  `period_id` int(11) DEFAULT NULL,
  `business_partner_id` int(11) DEFAULT NULL,
  `document_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `currency_id` (`currency_id`),
  KEY `entity_id` (`entity_id`),
  KEY `period_id` (`period_id`),
  KEY `business_partner_id` (`business_partner_id`),
  KEY `document_type_id` (`document_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `bill_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` float DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `total_gross` float DEFAULT NULL,
  `total_discount` float DEFAULT NULL,
  `total_tax` float DEFAULT NULL,
  `total_net` float DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `bill_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `tax_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `bill_id` (`bill_id`),
  KEY `item_id` (`item_id`),
  KEY `tax_id` (`tax_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `budget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `budget` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `status` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `calendar_id` int(11) DEFAULT NULL,
  `entity_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `calendar_id` (`calendar_id`),
  KEY `entity_id` (`entity_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `budget_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` int(11) NOT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `budget_id` int(11) DEFAULT NULL,
  `account_id` int(11) DEFAULT NULL,
  `period_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `budget_id` (`budget_id`),
  KEY `account_id` (`account_id`),
  KEY `period_id` (`period_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `business_partner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `business_partner` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `type` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `status` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `entity_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `entity_id` (`entity_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `calendar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `calendar` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `status` tinyint(1) NOT NULL,
  `year` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;




CREATE TABLE IF NOT EXISTS `calendar_period` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `period` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `period_start` date NOT NULL,
  `period_end` date NOT NULL,
  `status` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `calendar_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `calendar_id` (`calendar_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `chart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `chart` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `language` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `description` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;




CREATE TABLE IF NOT EXISTS `chart_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `account` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `type` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `posting` tinyint(1) NOT NULL,
  `budgeting` tinyint(1) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `level` int(11) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `parent_id` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `chart_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `chart_id` (`chart_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `currency` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `currency` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `status` tinyint(1) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `territory_id` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=246 ;



INSERT INTO `currency` (`id`, `code`, `currency`, `status`, `start_date`, `end_date`, `created_by`, `updated_by`, `created_on`, `updated_on`, `territory_id`) VALUES
(1, 'ADP', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'AD'),
(2, 'AED', 'United Arab Emirates Dirham', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'AE'),
(3, 'ALL', 'Albania Lek', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'AL'),
(4, 'AMD', 'Armenia Dram', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'AM'),
(5, 'ANG', 'Netherlands Antilles Guilder', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'AN'),
(6, 'AOK', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'AO'),
(7, 'AON', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'AO'),
(8, 'ARA', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'AR'),
(9, 'ARS', 'Argentina Peso', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'AR'),
(10, 'ATS', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'AT'),
(11, 'AUD', 'Australia Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'AU'),
(12, 'AWG', 'Aruba Guilder', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'AW'),
(13, 'AZM', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'AZ'),
(14, 'BBD', 'Barbados Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BB'),
(15, 'BDT', 'Bangladesh Taka', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BD'),
(16, 'BEF', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BE'),
(17, 'BGL', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BG'),
(18, 'BHD', 'Bahrain Dinar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BH'),
(19, 'BIF', 'Burundi Franc', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BI'),
(20, 'BMD', 'Bermuda Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BM'),
(21, 'BND', 'Brunei Darussalam Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BN'),
(22, 'BOB', 'Bolivia Boliviano', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BO'),
(23, 'BOV', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BO'),
(24, 'BRC', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BR'),
(25, 'BRL', 'Brazil Real', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BR'),
(26, 'BSD', 'Bahamas Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BS'),
(27, 'BTN', 'Bhutan Ngultrum', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BT'),
(28, 'BUK', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MM'),
(29, 'BWP', 'Botswana Pula', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BW'),
(30, 'BYB', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BY'),
(31, 'BZD', 'Belize Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BZ'),
(32, 'CAD', 'Canada Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'CA'),
(33, 'CHF', 'Switzerland Franc', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'CH'),
(34, 'CLF', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'CL'),
(35, 'CLP', 'Chile Peso', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'CL'),
(36, 'CNY', 'China Yuan Renminbi', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'CN'),
(37, 'COP', 'Colombia Peso', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'CO'),
(38, 'CRC', 'Costa Rica Colon', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'CR'),
(39, 'CSK', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(40, 'CUP', 'Cuba Peso', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'CU'),
(41, 'CVE', 'Cape Verde Escudo', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'CV'),
(42, 'CYP', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'CY'),
(43, 'CZK', 'Czech Republic Koruna', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'CZ'),
(44, 'DEM', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'DE'),
(45, 'DJF', 'Djibouti Franc', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'DJ'),
(46, 'DKK', 'Denmark Krone', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'DK'),
(47, 'DOP', 'Dominican Republic Peso', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'DO'),
(48, 'DZD', 'Algeria Dinar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'DZ'),
(49, 'ECS', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'EC'),
(50, 'ECV', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(51, 'EEK', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'EE'),
(52, 'EGP', 'Egypt Pound', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'EG'),
(53, 'ESB', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'ES'),
(54, 'ESP', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'ES'),
(55, 'ETB', 'Ethiopia Birr', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'ET'),
(56, 'EUR', 'Euro Member Countries', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(57, 'FIM', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'FI'),
(58, 'FJD', 'Fiji Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'FJ'),
(59, 'FKP', 'Falkland Islands (Malvinas) Pound', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'FK'),
(60, 'FRF', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'FR'),
(61, 'GBP', 'United Kingdom Pound', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'GB'),
(62, 'GEK', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'GE'),
(63, 'GHC', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'GH'),
(64, 'GIP', 'Gibraltar Pound', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'GI'),
(65, 'GMD', 'Gambia Dalasi', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'GM'),
(66, 'GNF', 'Guinea Franc', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'GN'),
(67, 'GRD', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'GR'),
(68, 'GTQ', 'Guatemala Quetzal', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'GT'),
(69, 'GWP', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'GW'),
(70, 'GYD', 'Guyana Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'GY'),
(71, 'HKD', 'Hong Kong Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'HK'),
(72, 'HNL', 'Honduras Lempira', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'HN'),
(73, 'HRD', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'HR'),
(74, 'HRK', 'Croatia Kuna', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'HR'),
(75, 'HTG', 'Haiti Gourde', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'HT'),
(76, 'HUF', 'Hungary Forint', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'HU'),
(77, 'IDR', 'Indonesia Rupiah', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'ID'),
(78, 'IEP', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'IE'),
(79, 'ILS', 'Israel Shekel', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'IL'),
(80, 'INR', 'India Rupee', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'IN'),
(81, 'IQD', 'Iraq Dinar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'IQ'),
(82, 'IRR', 'Iran Rial', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'IR'),
(83, 'ISK', 'Iceland Krona', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'IS'),
(84, 'ITL', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'IT'),
(85, 'JMD', 'Jamaica Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'JM'),
(86, 'JOD', 'Jordan Dinar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'JO'),
(87, 'JPY', 'Japan Yen', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'JP'),
(88, 'KES', 'Kenya Shilling', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'KE'),
(89, 'KGS', 'Kyrgyzstan Som', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'KG'),
(90, 'KHR', 'Cambodia Riel', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'KH'),
(91, 'KMF', 'Comoros Franc', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'KM'),
(92, 'KPW', 'Korea (North) Won', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'KP'),
(93, 'KRW', 'Korea (South) Won', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'KR'),
(94, 'KWD', 'Kuwait Dinar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'KW'),
(95, 'KYD', 'Cayman Islands Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'KY'),
(96, 'KZT', 'Kazakhstan Tenge', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'KZ'),
(97, 'LAK', 'Laos Kip', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'LA'),
(98, 'LBP', 'Lebanon Pound', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'LB'),
(99, 'LKR', 'Sri Lanka Rupee', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'LK'),
(100, 'LRD', 'Liberia Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'LR'),
(101, 'LSL', 'Lesotho Loti', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'LS'),
(102, 'LTL', 'Lithuania Litas', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'LT'),
(103, 'LUC', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'LU'),
(104, 'LUF', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'LU'),
(105, 'LUL', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'LU'),
(106, 'LVL', 'Latvia Lat', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'LV'),
(107, 'LVR', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'LV'),
(108, 'LYD', 'Libya Dinar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'LY'),
(109, 'MAD', 'Morocco Dirham', 1, '2016-08-22', '2017-08-22', '', 'test', NULL, '2017-10-01', 'MA'),
(110, 'MDL', 'Moldova Leu', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MD'),
(111, 'MGF', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MG'),
(112, 'MKD', 'Macedonia Denar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MK'),
(113, 'MMK', 'Myanmar (Burma) Kyat', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MM'),
(114, 'MNT', 'Mongolia Tughrik', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MN'),
(115, 'MOP', 'Macau Pataca', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MO'),
(116, 'MRO', 'Mauritania Ouguiya', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MR'),
(117, 'MTL', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MT'),
(118, 'MUR', 'Mauritius Rupee', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MU'),
(119, 'MVR', 'Maldives (Maldive Islands) Rufiyaa', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MV'),
(120, 'MWK', 'Malawi Kwacha', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MW'),
(121, 'MXN', 'Mexico Peso', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MX'),
(122, 'MXP', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MX'),
(123, 'MYR', 'Malaysia Ringgit', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MY'),
(124, 'MZM', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MZ'),
(125, 'NAD', 'Namibia Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'NA'),
(126, 'NGN', 'Nigeria Naira', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'NG'),
(127, 'NIC', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'NI'),
(128, 'NIO', 'Nicaragua Cordoba', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'NI'),
(129, 'NLG', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'NL'),
(130, 'NOK', 'Norway Krone', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'NO'),
(131, 'NPR', 'Nepal Rupee', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'NP'),
(132, 'NZD', 'New Zealand Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'NZ'),
(133, 'OMR', 'Oman Rial', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'OM'),
(134, 'PAB', 'Panama Balboa', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'PA'),
(135, 'PEI', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'PE'),
(136, 'PEN', 'Peru Nuevo Sol', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'PE'),
(137, 'PGK', 'Papua New Guinea Kina', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'PG'),
(138, 'PHP', 'Philippines Peso', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'PH'),
(139, 'PKR', 'Pakistan Rupee', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'PK'),
(140, 'PLN', 'Poland Zloty', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'PL'),
(141, 'PLZ', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'PL'),
(142, 'PTE', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'PT'),
(143, 'PYG', 'Paraguay Guarani', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'PY'),
(144, 'QAR', 'Qatar Riyal', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'QA'),
(145, 'ROL', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'RO'),
(146, 'RUR', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'RU'),
(147, 'RWF', 'Rwanda Franc', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'RW'),
(148, 'SAR', 'Saudi Arabia Riyal', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SA'),
(149, 'SBD', 'Solomon Islands Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SB'),
(150, 'SCR', 'Seychelles Rupee', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SC'),
(151, 'SDD', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SD'),
(152, 'SDP', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SD'),
(153, 'SEK', 'Sweden Krona', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SE'),
(154, 'SGD', 'Singapore Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SG'),
(155, 'SHP', 'Saint Helena Pound', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SH'),
(156, 'SIT', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SI'),
(157, 'SKK', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SK'),
(158, 'SLL', 'Sierra Leone Leone', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SL'),
(159, 'SOS', 'Somalia Shilling', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SO'),
(160, 'SRG', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SR'),
(161, 'STAT', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(162, 'STD', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'ST'),
(163, 'SUR', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'RU'),
(164, 'SVC', 'El Salvador Colon', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SV'),
(165, 'SYP', 'Syria Pound', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SY'),
(166, 'SZL', 'Swaziland Lilangeni', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SZ'),
(167, 'THB', 'Thailand Baht', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'TH'),
(168, 'TJR', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'TJ'),
(169, 'TMM', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'TM'),
(170, 'TND', 'Tunisia Dinar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'TN'),
(171, 'TOP', 'Tonga Pa''anga', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'TO'),
(172, 'TPE', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(173, 'TRL', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'TR'),
(174, 'TTD', 'Trinidad and Tobago Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'TT'),
(175, 'TWD', 'Taiwan New Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'TW'),
(176, 'TZS', 'Tanzania Shilling', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'TZ'),
(177, 'UAK', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'UA'),
(178, 'UGS', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'UG'),
(179, 'UGX', 'Uganda Shilling', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'UG'),
(180, 'USD', 'United States Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'US'),
(181, 'USN', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'US'),
(182, 'USS', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'US'),
(183, 'UYP', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'UY'),
(184, 'UYU', 'Uruguay Peso', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'UY'),
(185, 'UZS', 'Uzbekistan Som', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'UZ'),
(186, 'VEB', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'VE'),
(187, 'VND', 'Viet Nam Dong', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'VN'),
(188, 'VUV', 'Vanuatu Vatu', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'VU'),
(189, 'WST', 'Samoa Tala', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'WS'),
(190, 'XAF', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(191, 'XAG', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(192, 'XAU', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(193, 'XB5', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(194, 'XBA', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(195, 'XBB', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(196, 'XBC', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(197, 'XBD', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(198, 'XCD', 'East Caribbean Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(199, 'XDR', 'International Monetary Fund (IMF) Special Drawing Rights', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(200, 'XEU', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(201, 'XFO', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(202, 'XFU', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(203, 'XOF', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(204, 'XPD', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(205, 'XPF', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(206, 'XPT', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(207, 'XTS', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(208, 'XXX', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(209, 'YDD', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'YE'),
(210, 'YER', 'Yemen Rial', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'YE'),
(211, 'YUD', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(212, 'YUN', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(213, 'ZAL', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'ZA'),
(214, 'ZAR', 'South Africa Rand', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'ZA'),
(215, 'ZMK', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'ZM'),
(216, 'ZRN', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'CD'),
(217, 'ZRZ', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'CD'),
(218, 'ZWD', 'Zimbabwe Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'ZW'),
(219, 'RON', 'Romania New Leu', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'RO'),
(220, 'TRY', 'Turkey Lira', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'TR'),
(221, 'RSD', 'Serbia Dinar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'RS'),
(222, 'AZN', 'Azerbaijan New Manat', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'AZ'),
(223, 'VEF', 'Venezuela Bolivar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'VE'),
(224, 'SRD', 'Suriname Dollar', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SR'),
(225, 'MZN', 'Mozambique Metical', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MZ'),
(226, 'MGA', 'Madagascar Ariary', 1, '2016-08-22', '2017-08-22', '', 'test', NULL, '2016-08-22', 'MG'),
(227, 'GHS', 'Ghana Cedi', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'GH'),
(228, 'CHE', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'CH'),
(229, 'CHW', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'CH'),
(230, 'COU', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'CO'),
(231, 'AFN', 'Afghanistan Afghani', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(232, 'SDG', 'Sudan Pound', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'SD'),
(233, 'UYI', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'UY'),
(234, 'BYR', 'Belarus Ruble', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BY'),
(235, 'MXV', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'MX'),
(236, 'GEL', 'Georgia Lari', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'GE'),
(237, 'CDF', 'Congo/Kinshasa Franc', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'CD'),
(238, 'ERN', 'Eritrea Nakfa', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'ER'),
(239, 'AOA', 'Angola Kwanza', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'AO'),
(240, 'BAM', 'Bosnia and Herzegovina Convertible Marka', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BA'),
(241, 'BGN', 'Bulgaria Lev', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'BG'),
(242, 'RUB', 'Russia Ruble', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'RU'),
(243, 'UAH', 'Ukraine Hryvna', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'UA'),
(244, 'YUM', '', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, NULL),
(245, 'TJS', 'Tajikistan Somoni', 0, '2016-08-22', '2017-08-22', '', NULL, NULL, NULL, 'TJ');



CREATE TABLE IF NOT EXISTS `currency_rate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rate` float NOT NULL,
  `currency_from` int(11) DEFAULT NULL,
  `currency_to` int(11) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `currency_from` (`currency_from`),
  KEY `currency_to` (`currency_to`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `document` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `description` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `goods_receipt` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `document_id` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `document_date` date DEFAULT NULL,
  `document_status` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `document_origin_id` int(11) DEFAULT NULL,
  `document_origin` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `memo` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `total_gross` float DEFAULT NULL,
  `total_discount` float DEFAULT NULL,
  `total_tax` float DEFAULT NULL,
  `total_net` float DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `currency_id` int(11) DEFAULT NULL,
  `entity_id` int(11) DEFAULT NULL,
  `period_id` int(11) DEFAULT NULL,
  `business_partner_id` int(11) DEFAULT NULL,
  `document_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `currency_id` (`currency_id`),
  KEY `entity_id` (`entity_id`),
  KEY `period_id` (`period_id`),
  KEY `business_partner_id` (`business_partner_id`),
  KEY `document_type_id` (`document_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS `goods_receipt_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` float DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `total_gross` float DEFAULT NULL,
  `total_discount` float DEFAULT NULL,
  `total_tax` float DEFAULT NULL,
  `total_net` float DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `warehouse_id` int(11) DEFAULT NULL,
  `goods_receipt_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `tax_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `warehouse_id` (`warehouse_id`),
  KEY `goods_receipt_id` (`goods_receipt_id`),
  KEY `item_id` (`item_id`),
  KEY `tax_id` (`tax_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `invoice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `document_id` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `document_date` date DEFAULT NULL,
  `document_status` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `document_origin_id` int(11) DEFAULT NULL,
  `document_origin` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `memo` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `total_gross` float DEFAULT NULL,
  `total_discount` float DEFAULT NULL,
  `total_tax` float DEFAULT NULL,
  `total_net` float DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `currency_id` int(11) DEFAULT NULL,
  `entity_id` int(11) DEFAULT NULL,
  `period_id` int(11) DEFAULT NULL,
  `business_partner_id` int(11) DEFAULT NULL,
  `document_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `currency_id` (`currency_id`),
  KEY `entity_id` (`entity_id`),
  KEY `period_id` (`period_id`),
  KEY `business_partner_id` (`business_partner_id`),
  KEY `document_type_id` (`document_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `invoice_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` float DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `total_gross` float DEFAULT NULL,
  `total_discount` float DEFAULT NULL,
  `total_tax` float DEFAULT NULL,
  `total_net` float DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `invoice_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `tax_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `invoice_id` (`invoice_id`),
  KEY `item_id` (`item_id`),
  KEY `tax_id` (`tax_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `item` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `description` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `list_price` float DEFAULT NULL,
  `size` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `size_measure` varchar(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `weight` varchar(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `item_class` varchar(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `discontinued_date` date DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `item_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `status` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `entity_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `entity_id` (`entity_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `journal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `memo` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `source` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `status` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `actual` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `balanced` tinyint(1) DEFAULT NULL,
  `total_debit` float DEFAULT NULL,
  `total_credit` float DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `currency_id` int(11) DEFAULT NULL,
  `entity_id` int(11) DEFAULT NULL,
  `period_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `currency_id` (`currency_id`),
  KEY `entity_id` (`entity_id`),
  KEY `period_id` (`period_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `journal_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` int(11) NOT NULL,
  `debit_credit` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `journal_id` int(11) DEFAULT NULL,
  `account_id` int(11) DEFAULT NULL,
  `tax_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `journal_id` (`journal_id`),
  KEY `account_id` (`account_id`),
  KEY `tax_id` (`tax_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `legal_entity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `entity` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `national_id` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `fiscal_id` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `entity_status` tinyint(1) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `chart_id` int(11) DEFAULT NULL,
  `headquarter` int(11) DEFAULT NULL,
  `currency_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `chart_id` (`chart_id`),
  KEY `headquarter` (`headquarter`),
  KEY `currency_id` (`currency_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `street` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `zip_code` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `state_province` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `country` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `country` (`country`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `purchase_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `document_id` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `document_date` date DEFAULT NULL,
  `document_status` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `document_origin_id` int(11) DEFAULT NULL,
  `document_origin` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `memo` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `total_gross` float DEFAULT NULL,
  `total_discount` float DEFAULT NULL,
  `total_tax` float DEFAULT NULL,
  `total_net` float DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `currency_id` int(11) DEFAULT NULL,
  `entity_id` int(11) DEFAULT NULL,
  `period_id` int(11) DEFAULT NULL,
  `business_partner_id` int(11) DEFAULT NULL,
  `document_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `currency_id` (`currency_id`),
  KEY `entity_id` (`entity_id`),
  KEY `period_id` (`period_id`),
  KEY `business_partner_id` (`business_partner_id`),
  KEY `document_type_id` (`document_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `purchase_order_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` float DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `total_gross` float DEFAULT NULL,
  `total_discount` float DEFAULT NULL,
  `total_tax` float DEFAULT NULL,
  `total_net` float DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `purchase_order_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `tax_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `purchase_order_id` (`purchase_order_id`),
  KEY `item_id` (`item_id`),
  KEY `tax_id` (`tax_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `quote` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `document_id` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `document_date` date DEFAULT NULL,
  `document_status` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `memo` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `total_gross` float DEFAULT NULL,
  `total_discount` float DEFAULT NULL,
  `total_tax` float DEFAULT NULL,
  `total_net` float DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `currency_id` int(11) DEFAULT NULL,
  `entity_id` int(11) DEFAULT NULL,
  `period_id` int(11) DEFAULT NULL,
  `business_partner_id` int(11) DEFAULT NULL,
  `document_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `currency_id` (`currency_id`),
  KEY `entity_id` (`entity_id`),
  KEY `period_id` (`period_id`),
  KEY `business_partner_id` (`business_partner_id`),
  KEY `document_type_id` (`document_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `quote_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` float DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `total_gross` float DEFAULT NULL,
  `total_discount` float DEFAULT NULL,
  `total_tax` float DEFAULT NULL,
  `total_net` float DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `quote_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `tax_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `quote_id` (`quote_id`),
  KEY `item_id` (`item_id`),
  KEY `tax_id` (`tax_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `rfq` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `document_id` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `document_date` date DEFAULT NULL,
  `status` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `memo` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `total_gross` float DEFAULT NULL,
  `total_discount` float DEFAULT NULL,
  `total_tax` float DEFAULT NULL,
  `total_net` float DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `currency_id` int(11) DEFAULT NULL,
  `entity_id` int(11) DEFAULT NULL,
  `period_id` int(11) DEFAULT NULL,
  `business_partner_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `currency_id` (`currency_id`),
  KEY `entity_id` (`entity_id`),
  KEY `period_id` (`period_id`),
  KEY `business_partner_id` (`business_partner_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `rfq_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` float DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `total_gross` float DEFAULT NULL,
  `total_discount` float DEFAULT NULL,
  `total_tax` float DEFAULT NULL,
  `total_net` float DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `rfq_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `tax_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rfq_id` (`rfq_id`),
  KEY `item_id` (`item_id`),
  KEY `tax_id` (`tax_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `sale_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `document_id` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `document_date` date DEFAULT NULL,
  `document_status` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `document_origin_id` int(11) DEFAULT NULL,
  `document_origin` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `memo` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `total_gross` float DEFAULT NULL,
  `total_discount` float DEFAULT NULL,
  `total_tax` float DEFAULT NULL,
  `total_net` float DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `currency_id` int(11) DEFAULT NULL,
  `entity_id` int(11) DEFAULT NULL,
  `period_id` int(11) DEFAULT NULL,
  `business_partner_id` int(11) DEFAULT NULL,
  `document_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `currency_id` (`currency_id`),
  KEY `entity_id` (`entity_id`),
  KEY `period_id` (`period_id`),
  KEY `business_partner_id` (`business_partner_id`),
  KEY `document_type_id` (`document_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `sale_order_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` float DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `total_gross` float DEFAULT NULL,
  `total_discount` float DEFAULT NULL,
  `total_tax` float DEFAULT NULL,
  `total_net` float DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `sale_order_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `tax_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sale_order_id` (`sale_order_id`),
  KEY `item_id` (`item_id`),
  KEY `tax_id` (`tax_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `shipping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `document_id` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `document_date` date DEFAULT NULL,
  `document_status` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `document_origin_id` int(11) DEFAULT NULL,
  `document_origin` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `memo` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `total_gross` float DEFAULT NULL,
  `total_discount` float DEFAULT NULL,
  `total_tax` float DEFAULT NULL,
  `total_net` float DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `currency_id` int(11) DEFAULT NULL,
  `entity_id` int(11) DEFAULT NULL,
  `period_id` int(11) DEFAULT NULL,
  `business_partner_id` int(11) DEFAULT NULL,
  `document_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `currency_id` (`currency_id`),
  KEY `entity_id` (`entity_id`),
  KEY `period_id` (`period_id`),
  KEY `business_partner_id` (`business_partner_id`),
  KEY `document_type_id` (`document_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `shipping_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` float DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `total_gross` float DEFAULT NULL,
  `total_discount` float DEFAULT NULL,
  `total_tax` float DEFAULT NULL,
  `total_net` float DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `shipping_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `tax_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `shipping_id` (`shipping_id`),
  KEY `item_id` (`item_id`),
  KEY `tax_id` (`tax_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `tax` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `tax` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `status` tinyint(1) NOT NULL,
  `rate` float NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `created_by` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `updated_by` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_on` date DEFAULT NULL,
  `updated_on` date DEFAULT NULL,
  `territory_id` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `territory` (
  `code` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `language` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `source_language` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;



INSERT INTO `territory` (`code`, `name`, `language`, `source_language`) VALUES
('AD', 'ANDORRA', 'EN', 'EN'),
('AE', 'UNITED ARAB EMIRATES', 'EN', 'EN'),
('AG', 'ANTIGUA AND BARBUDA', 'EN', 'EN'),
('AI', 'ANGUILLA', 'EN', 'EN'),
('AL', 'ALBANIA', 'EN', 'EN'),
('AM', 'ARMENIA', 'EN', 'EN'),
('AN', 'NETHERLANDS ANTILLES', 'EN', 'EN'),
('AO', 'ANGOLA', 'EN', 'EN'),
('AQ', 'ANTARCTICA', 'EN', 'EN'),
('AR', 'ARGENTINA', 'EN', 'EN'),
('AS', 'AMERICAN SAMOA', 'EN', 'EN'),
('AT', 'AUSTRIA', 'EN', 'EN'),
('AU', 'AUSTRALIA', 'EN', 'EN'),
('AW', 'ARUBA', 'EN', 'EN'),
('AZ', 'AZERBAIJAN', 'EN', 'EN'),
('BA', 'BOSNIA AND HERZEGOVINA', 'EN', 'EN'),
('BB', 'BARBADOS', 'EN', 'EN'),
('BD', 'BANGLADESH', 'EN', 'EN'),
('BE', 'BELGIUM', 'EN', 'EN'),
('BF', 'BURKINA FASO', 'EN', 'EN'),
('BG', 'BULGARIA', 'EN', 'EN'),
('BH', 'BAHRAIN', 'EN', 'EN'),
('BI', 'BURUNDI', 'EN', 'EN'),
('BJ', 'BENIN', 'EN', 'EN'),
('BM', 'BERMUDA', 'EN', 'EN'),
('BN', 'BRUNEI DARUSSALAM', 'EN', 'EN'),
('BO', 'BOLIVIA', 'EN', 'EN'),
('BR', 'BRAZIL', 'EN', 'EN'),
('BS', 'BAHAMAS', 'EN', 'EN'),
('BT', 'BHUTAN', 'EN', 'EN'),
('BV', 'BOUVET ISLAND', 'EN', 'EN'),
('BW', 'BOTSWANA', 'EN', 'EN'),
('BY', 'BELARUS', 'EN', 'EN'),
('BZ', 'BELIZE', 'EN', 'EN'),
('CA', 'CANADA', 'EN', 'EN'),
('CC', 'COCOS (KEELING) ISLANDS', 'EN', 'EN'),
('CD', 'CONGO, THE DEMOCRATIC REPUBLIC OF THE', 'EN', 'EN'),
('CF', 'CENTRAL AFRICAN REPUBLIC', 'EN', 'EN'),
('CG', 'CONGO', 'EN', 'EN'),
('CH', 'SWITZERLAND', 'EN', 'EN'),
('CI', 'COTE D''IVOIRE', 'EN', 'EN'),
('CK', 'COOK ISLANDS', 'EN', 'EN'),
('CL', 'CHILE', 'EN', 'EN'),
('CM', 'CAMEROON', 'EN', 'EN'),
('CN', 'CHINA', 'EN', 'EN'),
('CO', 'COLOMBIA', 'EN', 'EN'),
('CR', 'COSTA RICA', 'EN', 'EN'),
('CU', 'CUBA', 'EN', 'EN'),
('CV', 'CAPE VERDE', 'EN', 'EN'),
('CX', 'CHRISTMAS ISLAND', 'EN', 'EN'),
('CY', 'CYPRUS', 'EN', 'EN'),
('CZ', 'CZECH REPUBLIC', 'EN', 'EN'),
('DE', 'GERMANY', 'EN', 'EN'),
('DJ', 'DJIBOUTI', 'EN', 'EN'),
('DK', 'DENMARK', 'EN', 'EN'),
('DM', 'DOMINICA', 'EN', 'EN'),
('DO', 'DOMINICAN REPUBLIC', 'EN', 'EN'),
('DZ', 'ALGERIA', 'EN', 'EN'),
('EC', 'ECUADOR', 'EN', 'EN'),
('EE', 'ESTONIA', 'EN', 'EN'),
('EG', 'EGYPT', 'EN', 'EN'),
('EH', 'WESTERN SAHARA', 'EN', 'EN'),
('ER', 'ERITREA', 'EN', 'EN'),
('ES', 'SPAIN', 'EN', 'EN'),
('ET', 'ETHIOPIA', 'EN', 'EN'),
('FI', 'FINLAND', 'EN', 'EN'),
('FJ', 'FIJI', 'EN', 'EN'),
('FK', 'FALKLAND ISLANDS (MALVINAS)', 'EN', 'EN'),
('FM', 'MICRONESIA, FEDERATED STATES OF', 'EN', 'EN'),
('FO', 'FAROE ISLANDS', 'EN', 'EN'),
('FR', 'FRANCE', 'EN', 'EN'),
('GA', 'GABON', 'EN', 'EN'),
('GB', 'UNITED KINGDOM', 'EN', 'EN'),
('GD', 'GRENADA', 'EN', 'EN'),
('GE', 'GEORGIA', 'EN', 'EN'),
('GF', 'FRENCH GUIANA', 'EN', 'EN'),
('GG', 'GUERNSEY', 'EN', 'EN'),
('GH', 'GHANA', 'EN', 'EN'),
('GI', 'GIBRALTAR', 'EN', 'EN'),
('GL', 'GREENLAND', 'EN', 'EN'),
('GM', 'GAMBIA', 'EN', 'EN'),
('GN', 'GUINEA', 'EN', 'EN'),
('GP', 'GUADELOUPE', 'EN', 'EN'),
('GQ', 'EQUATORIAL GUINEA', 'EN', 'EN'),
('GR', 'GREECE', 'EN', 'EN'),
('GS', 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS', 'EN', 'EN'),
('GT', 'GUATEMALA', 'EN', 'EN'),
('GU', 'GUAM', 'EN', 'EN'),
('GW', 'GUINEA-BISSAU', 'EN', 'EN'),
('GY', 'GUYANA', 'EN', 'EN'),
('HK', 'HONG KONG', 'EN', 'EN'),
('HM', 'HEARD ISLAND AND MCDONALD ISLANDS', 'EN', 'EN'),
('HN', 'HONDURAS', 'EN', 'EN'),
('HR', 'CROATIA', 'EN', 'EN'),
('HT', 'HAITI', 'EN', 'EN'),
('HU', 'HUNGARY', 'EN', 'EN'),
('ID', 'INDONESIA', 'EN', 'EN'),
('IE', 'IRELAND', 'EN', 'EN'),
('IL', 'ISRAEL', 'EN', 'EN'),
('IM', 'ISLE OF MAN', 'EN', 'EN'),
('IN', 'INDIA', 'EN', 'EN'),
('IO', 'BRITISH INDIAN OCEAN TERRITORY', 'EN', 'EN'),
('IQ', 'IRAQ', 'EN', 'EN'),
('IR', 'IRAN, ISLAMIC REPUBLIC OF', 'EN', 'EN'),
('IS', 'ICELAND', 'EN', 'EN'),
('IT', 'ITALY', 'EN', 'EN'),
('JE', 'JERSEY', 'EN', 'EN'),
('JM', 'JAMAICA', 'EN', 'EN'),
('JO', 'JORDAN', 'EN', 'EN'),
('JP', 'JAPAN', 'EN', 'EN'),
('KE', 'KENYA', 'EN', 'EN'),
('KG', 'KYRGYZSTAN', 'EN', 'EN'),
('KH', 'CAMBODIA', 'EN', 'EN'),
('KI', 'KIRIBATI', 'EN', 'EN'),
('KM', 'COMOROS', 'EN', 'EN'),
('KN', 'SAINT KITTS AND NEVIS', 'EN', 'EN'),
('KP', 'KOREA, DEMOCRATIC PEOPLE''S REPUBLIC OF', 'EN', 'EN'),
('KR', 'KOREA, REPUBLIC OF', 'EN', 'EN'),
('KW', 'KUWAIT', 'EN', 'EN'),
('KY', 'CAYMAN ISLANDS', 'EN', 'EN'),
('KZ', 'KAZAKHSTAN', 'EN', 'EN'),
('LA', 'LAO PEOPLE''S DEMOCRATIC REPUBLIC', 'EN', 'EN'),
('LB', 'LEBANON', 'EN', 'EN'),
('LC', 'SAINT LUCIA', 'EN', 'EN'),
('LI', 'LIECHTENSTEIN', 'EN', 'EN'),
('LK', 'SRI LANKA', 'EN', 'EN'),
('LR', 'LIBERIA', 'EN', 'EN'),
('LS', 'LESOTHO', 'EN', 'EN'),
('LT', 'LITHUANIA', 'EN', 'EN'),
('LU', 'LUXEMBOURG', 'EN', 'EN'),
('LV', 'LATVIA', 'EN', 'EN'),
('LY', 'LIBYAN ARAB JAMAHIRIYA', 'EN', 'EN'),
('MA', 'MOROCCO', 'EN', 'EN'),
('MC', 'MONACO', 'EN', 'EN'),
('MD', 'MOLDOVA, REPUBLIC OF', 'EN', 'EN'),
('ME', 'MONTENEGRO', 'EN', 'EN'),
('MG', 'MADAGASCAR', 'EN', 'EN'),
('MH', 'MARSHALL ISLANDS', 'EN', 'EN'),
('MK', 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF', 'EN', 'EN'),
('ML', 'MALI', 'EN', 'EN'),
('MM', 'MYANMAR', 'EN', 'EN'),
('MN', 'MONGOLIA', 'EN', 'EN'),
('MO', 'MACAO', 'EN', 'EN'),
('MP', 'NORTHERN MARIANA ISLANDS', 'EN', 'EN'),
('MQ', 'MARTINIQUE', 'EN', 'EN'),
('MR', 'MAURITANIA', 'EN', 'EN'),
('MS', 'MONTSERRAT', 'EN', 'EN'),
('MT', 'MALTA', 'EN', 'EN'),
('MU', 'MAURITIUS', 'EN', 'EN'),
('MV', 'MALDIVES', 'EN', 'EN'),
('MW', 'MALAWI', 'EN', 'EN'),
('MX', 'MEXICO', 'EN', 'EN'),
('MY', 'MALAYSIA', 'EN', 'EN'),
('MZ', 'MOZAMBIQUE', 'EN', 'EN'),
('NA', 'NAMIBIA', 'EN', 'EN'),
('NC', 'NEW CALEDONIA', 'EN', 'EN'),
('NE', 'NIGER', 'EN', 'EN'),
('NF', 'NORFOLK ISLAND', 'EN', 'EN'),
('NG', 'NIGERIA', 'EN', 'EN'),
('NI', 'NICARAGUA', 'EN', 'EN'),
('NL', 'NETHERLANDS', 'EN', 'EN'),
('NO', 'NORWAY', 'EN', 'EN'),
('NP', 'NEPAL', 'EN', 'EN'),
('NR', 'NAURU', 'EN', 'EN'),
('NU', 'NIUE', 'EN', 'EN'),
('NZ', 'NEW ZEALAND', 'EN', 'EN'),
('OM', 'OMAN', 'EN', 'EN'),
('PA', 'PANAMA', 'EN', 'EN'),
('PE', 'PERU', 'EN', 'EN'),
('PF', 'FRENCH POLYNESIA', 'EN', 'EN'),
('PG', 'PAPUA NEW GUINEA', 'EN', 'EN'),
('PH', 'PHILIPPINES', 'EN', 'EN'),
('PK', 'PAKISTAN', 'EN', 'EN'),
('PL', 'POLAND', 'EN', 'EN'),
('PM', 'SAINT PIERRE AND MIQUELON', 'EN', 'EN'),
('PN', 'PITCAIRN', 'EN', 'EN'),
('PR', 'PUERTO RICO', 'EN', 'EN'),
('PS', 'PALESTINIAN TERRITORY, OCCUPIED', 'EN', 'EN'),
('PT', 'PORTUGAL', 'EN', 'EN'),
('PW', 'PALAU', 'EN', 'EN'),
('PY', 'PARAGUAY', 'EN', 'EN'),
('QA', 'QATAR', 'EN', 'EN'),
('RE', 'RÉUNION', 'EN', 'EN'),
('RO', 'ROMANIA', 'EN', 'EN'),
('RS', 'SERBIA', 'EN', 'EN'),
('RU', 'RUSSIAN FEDERATION', 'EN', 'EN'),
('RW', 'RWANDA', 'EN', 'EN'),
('SA', 'SAUDI ARABIA', 'EN', 'EN'),
('SB', 'SOLOMON ISLANDS', 'EN', 'EN'),
('SC', 'SEYCHELLES', 'EN', 'EN'),
('SD', 'SUDAN', 'EN', 'EN'),
('SE', 'SWEDEN', 'EN', 'EN'),
('SG', 'SINGAPORE', 'EN', 'EN'),
('SH', 'SAINT HELENA', 'EN', 'EN'),
('SI', 'SLOVENIA', 'EN', 'EN'),
('SJ', 'SVALBARD AND JAN MAYEN', 'EN', 'EN'),
('SK', 'SLOVAKIA', 'EN', 'EN'),
('SL', 'SIERRA LEONE', 'EN', 'EN'),
('SM', 'SAN MARINO', 'EN', 'EN'),
('SN', 'SENEGAL', 'EN', 'EN'),
('SO', 'SOMALIA', 'EN', 'EN'),
('SR', 'SURINAME', 'EN', 'EN'),
('ST', 'SAO TOME AND PRINCIPE', 'EN', 'EN'),
('SV', 'EL SALVADOR', 'EN', 'EN'),
('SY', 'SYRIAN ARAB REPUBLIC', 'EN', 'EN'),
('SZ', 'SWAZILAND', 'EN', 'EN'),
('TC', 'TURKS AND CAICOS ISLANDS', 'EN', 'EN'),
('TD', 'CHAD', 'EN', 'EN'),
('TF', 'FRENCH SOUTHERN TERRITORIES', 'EN', 'EN'),
('TG', 'TOGO', 'EN', 'EN'),
('TH', 'THAILAND', 'EN', 'EN'),
('TJ', 'TAJIKISTAN', 'EN', 'EN'),
('TK', 'TOKELAU', 'EN', 'EN'),
('TL', 'TIMOR-LESTE', 'EN', 'EN'),
('TM', 'TURKMENISTAN', 'EN', 'EN'),
('TN', 'TUNISIA', 'EN', 'EN'),
('TO', 'TONGA', 'EN', 'EN'),
('TR', 'TURKEY', 'EN', 'EN'),
('TT', 'TRINIDAD AND TOBAGO', 'EN', 'EN'),
('TV', 'TUVALU', 'EN', 'EN'),
('TW', 'TAIWAN, PROVINCE OF CHINA', 'EN', 'EN'),
('TZ', 'TANZANIA, UNITED REPUBLIC OF', 'EN', 'EN'),
('UA', 'UKRAINE', 'EN', 'EN'),
('UG', 'UGANDA', 'EN', 'EN'),
('UM', 'UNITED STATES MINOR OUTLYING ISLANDS', 'EN', 'EN'),
('US', 'UNITED STATES', 'EN', 'EN'),
('UY', 'URUGUAY', 'EN', 'EN'),
('UZ', 'UZBEKISTAN', 'EN', 'EN'),
('VA', 'HOLY SEE (VATICAN CITY STATE)', 'EN', 'EN'),
('VC', 'SAINT VINCENT AND THE GRENADINES', 'EN', 'EN'),
('VE', 'VENEZUELA', 'EN', 'EN'),
('VG', 'VIRGIN ISLANDS, BRITISH', 'EN', 'EN'),
('VI', 'VIRGIN ISLANDS, U.S.', 'EN', 'EN'),
('VN', 'VIET NAM', 'EN', 'EN'),
('VU', 'VANUATU', 'EN', 'EN'),
('WF', 'WALLIS AND FUTUNA', 'EN', 'EN'),
('WS', 'SAMOA', 'EN', 'EN'),
('YE', 'YEMEN', 'EN', 'EN'),
('YT', 'MAYOTTE', 'EN', 'EN'),
('ZA', 'SOUTH AFRICA', 'EN', 'EN'),
('ZM', 'ZAMBIA', 'EN', 'EN'),
('ZW', 'ZIMBABWE', 'EN', 'EN');


ALTER TABLE `bank`
  ADD CONSTRAINT `bank_ibfk_1` FOREIGN KEY (`country`) REFERENCES `territory` (`code`);


ALTER TABLE `bill`
  ADD CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`currency_id`) REFERENCES `currency` (`id`),
  ADD CONSTRAINT `bill_ibfk_2` FOREIGN KEY (`entity_id`) REFERENCES `legal_entity` (`id`),
  ADD CONSTRAINT `bill_ibfk_3` FOREIGN KEY (`period_id`) REFERENCES `calendar_period` (`id`),
  ADD CONSTRAINT `bill_ibfk_4` FOREIGN KEY (`business_partner_id`) REFERENCES `business_partner` (`id`),
  ADD CONSTRAINT `bill_ibfk_5` FOREIGN KEY (`document_type_id`) REFERENCES `document` (`id`);


ALTER TABLE `bill_details`
  ADD CONSTRAINT `bill_details_ibfk_1` FOREIGN KEY (`bill_id`) REFERENCES `bill` (`id`),
  ADD CONSTRAINT `bill_details_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `item` (`id`),
  ADD CONSTRAINT `bill_details_ibfk_3` FOREIGN KEY (`tax_id`) REFERENCES `tax` (`id`);


ALTER TABLE `budget`
  ADD CONSTRAINT `budget_ibfk_1` FOREIGN KEY (`calendar_id`) REFERENCES `calendar` (`id`),
  ADD CONSTRAINT `budget_ibfk_2` FOREIGN KEY (`entity_id`) REFERENCES `legal_entity` (`id`);


ALTER TABLE `budget_details`
  ADD CONSTRAINT `budget_details_ibfk_1` FOREIGN KEY (`budget_id`) REFERENCES `budget` (`id`),
  ADD CONSTRAINT `budget_details_ibfk_2` FOREIGN KEY (`account_id`) REFERENCES `chart_account` (`id`),
  ADD CONSTRAINT `budget_details_ibfk_3` FOREIGN KEY (`period_id`) REFERENCES `calendar_period` (`id`);


ALTER TABLE `business_partner`
  ADD CONSTRAINT `business_partner_ibfk_1` FOREIGN KEY (`entity_id`) REFERENCES `legal_entity` (`id`);


ALTER TABLE `calendar_period`
  ADD CONSTRAINT `calendar_period_ibfk_1` FOREIGN KEY (`calendar_id`) REFERENCES `calendar` (`id`);


ALTER TABLE `chart_account`
  ADD CONSTRAINT `chart_account_ibfk_1` FOREIGN KEY (`chart_id`) REFERENCES `chart` (`id`);


ALTER TABLE `currency_rate`
  ADD CONSTRAINT `currency_rate_ibfk_1` FOREIGN KEY (`currency_from`) REFERENCES `currency` (`id`),
  ADD CONSTRAINT `currency_rate_ibfk_2` FOREIGN KEY (`currency_to`) REFERENCES `currency` (`id`);


ALTER TABLE `goods_receipt`
  ADD CONSTRAINT `goods_receipt_ibfk_1` FOREIGN KEY (`currency_id`) REFERENCES `currency` (`id`),
  ADD CONSTRAINT `goods_receipt_ibfk_2` FOREIGN KEY (`entity_id`) REFERENCES `legal_entity` (`id`),
  ADD CONSTRAINT `goods_receipt_ibfk_3` FOREIGN KEY (`period_id`) REFERENCES `calendar_period` (`id`),
  ADD CONSTRAINT `goods_receipt_ibfk_4` FOREIGN KEY (`business_partner_id`) REFERENCES `business_partner` (`id`),
  ADD CONSTRAINT `goods_receipt_ibfk_5` FOREIGN KEY (`document_type_id`) REFERENCES `document` (`id`);


ALTER TABLE `goods_receipt_details`
  ADD CONSTRAINT `goods_receipt_details_ibfk_1` FOREIGN KEY (`warehouse_id`) REFERENCES `location` (`id`),
  ADD CONSTRAINT `goods_receipt_details_ibfk_2` FOREIGN KEY (`goods_receipt_id`) REFERENCES `goods_receipt` (`id`),
  ADD CONSTRAINT `goods_receipt_details_ibfk_3` FOREIGN KEY (`item_id`) REFERENCES `item` (`id`),
  ADD CONSTRAINT `goods_receipt_details_ibfk_4` FOREIGN KEY (`tax_id`) REFERENCES `tax` (`id`);


ALTER TABLE `invoice`
  ADD CONSTRAINT `invoice_ibfk_1` FOREIGN KEY (`currency_id`) REFERENCES `currency` (`id`),
  ADD CONSTRAINT `invoice_ibfk_2` FOREIGN KEY (`entity_id`) REFERENCES `legal_entity` (`id`),
  ADD CONSTRAINT `invoice_ibfk_3` FOREIGN KEY (`period_id`) REFERENCES `calendar_period` (`id`),
  ADD CONSTRAINT `invoice_ibfk_4` FOREIGN KEY (`business_partner_id`) REFERENCES `business_partner` (`id`),
  ADD CONSTRAINT `invoice_ibfk_5` FOREIGN KEY (`document_type_id`) REFERENCES `document` (`id`);


ALTER TABLE `invoice_details`
  ADD CONSTRAINT `invoice_details_ibfk_1` FOREIGN KEY (`invoice_id`) REFERENCES `invoice` (`id`),
  ADD CONSTRAINT `invoice_details_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `item` (`id`),
  ADD CONSTRAINT `invoice_details_ibfk_3` FOREIGN KEY (`tax_id`) REFERENCES `tax` (`id`);


ALTER TABLE `item`
  ADD CONSTRAINT `item_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `item_category` (`id`);


ALTER TABLE `item_category`
  ADD CONSTRAINT `item_category_ibfk_1` FOREIGN KEY (`entity_id`) REFERENCES `legal_entity` (`id`);


ALTER TABLE `journal`
  ADD CONSTRAINT `journal_ibfk_1` FOREIGN KEY (`currency_id`) REFERENCES `currency` (`id`),
  ADD CONSTRAINT `journal_ibfk_2` FOREIGN KEY (`entity_id`) REFERENCES `legal_entity` (`id`),
  ADD CONSTRAINT `journal_ibfk_3` FOREIGN KEY (`period_id`) REFERENCES `calendar_period` (`id`);


ALTER TABLE `journal_details`
  ADD CONSTRAINT `journal_details_ibfk_1` FOREIGN KEY (`journal_id`) REFERENCES `journal` (`id`),
  ADD CONSTRAINT `journal_details_ibfk_2` FOREIGN KEY (`account_id`) REFERENCES `chart_account` (`id`),
  ADD CONSTRAINT `journal_details_ibfk_3` FOREIGN KEY (`tax_id`) REFERENCES `tax` (`id`);


ALTER TABLE `legal_entity`
  ADD CONSTRAINT `legal_entity_ibfk_1` FOREIGN KEY (`chart_id`) REFERENCES `chart` (`id`),
  ADD CONSTRAINT `legal_entity_ibfk_2` FOREIGN KEY (`headquarter`) REFERENCES `location` (`id`),
  ADD CONSTRAINT `legal_entity_ibfk_3` FOREIGN KEY (`currency_id`) REFERENCES `currency` (`id`);


ALTER TABLE `location`
  ADD CONSTRAINT `location_ibfk_1` FOREIGN KEY (`country`) REFERENCES `territory` (`code`);


ALTER TABLE `purchase_order`
  ADD CONSTRAINT `purchase_order_ibfk_1` FOREIGN KEY (`currency_id`) REFERENCES `currency` (`id`),
  ADD CONSTRAINT `purchase_order_ibfk_2` FOREIGN KEY (`entity_id`) REFERENCES `legal_entity` (`id`),
  ADD CONSTRAINT `purchase_order_ibfk_3` FOREIGN KEY (`period_id`) REFERENCES `calendar_period` (`id`),
  ADD CONSTRAINT `purchase_order_ibfk_4` FOREIGN KEY (`business_partner_id`) REFERENCES `business_partner` (`id`),
  ADD CONSTRAINT `purchase_order_ibfk_5` FOREIGN KEY (`document_type_id`) REFERENCES `document` (`id`);


ALTER TABLE `purchase_order_details`
  ADD CONSTRAINT `purchase_order_details_ibfk_1` FOREIGN KEY (`purchase_order_id`) REFERENCES `purchase_order` (`id`),
  ADD CONSTRAINT `purchase_order_details_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `item` (`id`),
  ADD CONSTRAINT `purchase_order_details_ibfk_3` FOREIGN KEY (`tax_id`) REFERENCES `tax` (`id`);


ALTER TABLE `quote`
  ADD CONSTRAINT `quote_ibfk_1` FOREIGN KEY (`currency_id`) REFERENCES `currency` (`id`),
  ADD CONSTRAINT `quote_ibfk_2` FOREIGN KEY (`entity_id`) REFERENCES `legal_entity` (`id`),
  ADD CONSTRAINT `quote_ibfk_3` FOREIGN KEY (`period_id`) REFERENCES `calendar_period` (`id`),
  ADD CONSTRAINT `quote_ibfk_4` FOREIGN KEY (`business_partner_id`) REFERENCES `business_partner` (`id`),
  ADD CONSTRAINT `quote_ibfk_5` FOREIGN KEY (`document_type_id`) REFERENCES `document` (`id`);


ALTER TABLE `quote_details`
  ADD CONSTRAINT `quote_details_ibfk_1` FOREIGN KEY (`quote_id`) REFERENCES `quote` (`id`),
  ADD CONSTRAINT `quote_details_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `item` (`id`),
  ADD CONSTRAINT `quote_details_ibfk_3` FOREIGN KEY (`tax_id`) REFERENCES `tax` (`id`);


ALTER TABLE `rfq`
  ADD CONSTRAINT `rfq_ibfk_1` FOREIGN KEY (`currency_id`) REFERENCES `currency` (`id`),
  ADD CONSTRAINT `rfq_ibfk_2` FOREIGN KEY (`entity_id`) REFERENCES `legal_entity` (`id`),
  ADD CONSTRAINT `rfq_ibfk_3` FOREIGN KEY (`period_id`) REFERENCES `calendar_period` (`id`),
  ADD CONSTRAINT `rfq_ibfk_4` FOREIGN KEY (`business_partner_id`) REFERENCES `business_partner` (`id`);


ALTER TABLE `rfq_details`
  ADD CONSTRAINT `rfq_details_ibfk_1` FOREIGN KEY (`rfq_id`) REFERENCES `rfq` (`id`),
  ADD CONSTRAINT `rfq_details_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `item` (`id`),
  ADD CONSTRAINT `rfq_details_ibfk_3` FOREIGN KEY (`tax_id`) REFERENCES `tax` (`id`);


ALTER TABLE `sale_order`
  ADD CONSTRAINT `sale_order_ibfk_1` FOREIGN KEY (`currency_id`) REFERENCES `currency` (`id`),
  ADD CONSTRAINT `sale_order_ibfk_2` FOREIGN KEY (`entity_id`) REFERENCES `legal_entity` (`id`),
  ADD CONSTRAINT `sale_order_ibfk_3` FOREIGN KEY (`period_id`) REFERENCES `calendar_period` (`id`),
  ADD CONSTRAINT `sale_order_ibfk_4` FOREIGN KEY (`business_partner_id`) REFERENCES `business_partner` (`id`),
  ADD CONSTRAINT `sale_order_ibfk_5` FOREIGN KEY (`document_type_id`) REFERENCES `document` (`id`);


ALTER TABLE `sale_order_details`
  ADD CONSTRAINT `sale_order_details_ibfk_1` FOREIGN KEY (`sale_order_id`) REFERENCES `sale_order` (`id`),
  ADD CONSTRAINT `sale_order_details_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `item` (`id`),
  ADD CONSTRAINT `sale_order_details_ibfk_3` FOREIGN KEY (`tax_id`) REFERENCES `tax` (`id`);


ALTER TABLE `shipping`
  ADD CONSTRAINT `shipping_ibfk_1` FOREIGN KEY (`currency_id`) REFERENCES `currency` (`id`),
  ADD CONSTRAINT `shipping_ibfk_2` FOREIGN KEY (`entity_id`) REFERENCES `legal_entity` (`id`),
  ADD CONSTRAINT `shipping_ibfk_3` FOREIGN KEY (`period_id`) REFERENCES `calendar_period` (`id`),
  ADD CONSTRAINT `shipping_ibfk_4` FOREIGN KEY (`business_partner_id`) REFERENCES `business_partner` (`id`),
  ADD CONSTRAINT `shipping_ibfk_5` FOREIGN KEY (`document_type_id`) REFERENCES `document` (`id`);


ALTER TABLE `shipping_details`
  ADD CONSTRAINT `shipping_details_ibfk_1` FOREIGN KEY (`shipping_id`) REFERENCES `shipping` (`id`),
  ADD CONSTRAINT `shipping_details_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `item` (`id`),
  ADD CONSTRAINT `shipping_details_ibfk_3` FOREIGN KEY (`tax_id`) REFERENCES `tax` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
