-- MySQL dump 10.13  Distrib 5.7.38, for Linux (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	5.7.38-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Homework7_hw7`
--

DROP TABLE IF EXISTS `Homework7_hw7`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Homework7_hw7` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `column1` int(10) unsigned NOT NULL,
  `pub_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Homework7_hw7`
--

LOCK TABLES `Homework7_hw7` WRITE;
/*!40000 ALTER TABLE `Homework7_hw7` DISABLE KEYS */;
INSERT INTO `Homework7_hw7` VALUES (1,4108056005,'2022-04-20 07:31:17.071602');
/*!40000 ALTER TABLE `Homework7_hw7` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'Homework7','0001_initial','2022-04-20 07:29:39.441782'),(2,'contenttypes','0001_initial','2022-04-20 07:29:39.450942'),(3,'auth','0001_initial','2022-04-20 07:29:42.320495'),(4,'admin','0001_initial','2022-04-20 07:29:42.342622'),(5,'admin','0002_logentry_remove_auto_add','2022-04-20 07:29:42.407437'),(6,'admin','0003_logentry_add_action_flag_choices','2022-04-20 07:29:42.418725'),(7,'contenttypes','0002_remove_content_type_name','2022-04-20 07:29:42.435894'),(8,'auth','0002_alter_permission_name_max_length','2022-04-20 07:29:42.456004'),(9,'auth','0003_alter_user_email_max_length','2022-04-20 07:29:42.534350'),(10,'auth','0004_alter_user_username_opts','2022-04-20 07:29:42.545890'),(11,'auth','0005_alter_user_last_login_null','2022-04-20 07:29:42.570313'),(12,'auth','0006_require_contenttypes_0002','2022-04-20 07:29:42.618644'),(13,'auth','0007_alter_validators_add_error_messages','2022-04-20 07:29:42.630864'),(14,'auth','0008_alter_user_username_max_length','2022-04-20 07:29:42.687761'),(15,'auth','0009_alter_user_last_name_max_length','2022-04-20 07:29:42.770649'),(16,'auth','0010_alter_group_name_max_length','2022-04-20 07:29:42.782114'),(17,'auth','0011_update_proxy_permissions','2022-04-20 07:29:42.791820'),(18,'auth','0012_alter_user_first_name_max_length','2022-04-20 07:29:42.803017'),(19,'mobilemarket','0001_initial','2022-04-20 07:29:43.304596'),(20,'mobilemarket','0002_alter_product_pmodel','2022-04-20 07:29:43.467145'),(21,'mobilemarket','0003_alter_product_pmodel','2022-04-20 07:29:43.680732'),(22,'mysite','0001_initial','2022-04-20 07:29:43.687384'),(23,'mysite','0002_product','2022-04-20 07:29:43.693719'),(24,'mysite','0003_alter_product_size','2022-04-20 07:29:43.704123'),(25,'sessions','0001_initial','2022-04-20 07:29:43.710569');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mobilemarket_maker`
--

DROP TABLE IF EXISTS `mobilemarket_maker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mobilemarket_maker` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `country` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobilemarket_maker`
--

LOCK TABLES `mobilemarket_maker` WRITE;
/*!40000 ALTER TABLE `mobilemarket_maker` DISABLE KEYS */;
/*!40000 ALTER TABLE `mobilemarket_maker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mobilemarket_pmodel`
--

DROP TABLE IF EXISTS `mobilemarket_pmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mobilemarket_pmodel` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `url` varchar(200) NOT NULL,
  `maker_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mobilemarket_pmodel_maker_id_9f200c72_fk_mobilemarket_maker_id` (`maker_id`),
  CONSTRAINT `mobilemarket_pmodel_maker_id_9f200c72_fk_mobilemarket_maker_id` FOREIGN KEY (`maker_id`) REFERENCES `mobilemarket_maker` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobilemarket_pmodel`
--

LOCK TABLES `mobilemarket_pmodel` WRITE;
/*!40000 ALTER TABLE `mobilemarket_pmodel` DISABLE KEYS */;
/*!40000 ALTER TABLE `mobilemarket_pmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mobilemarket_pphoto`
--

DROP TABLE IF EXISTS `mobilemarket_pphoto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mobilemarket_pphoto` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(20) NOT NULL,
  `url` varchar(200) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mobilemarket_pphoto_product_id_cdab29a7_fk_mobilemar` (`product_id`),
  CONSTRAINT `mobilemarket_pphoto_product_id_cdab29a7_fk_mobilemar` FOREIGN KEY (`product_id`) REFERENCES `mobilemarket_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobilemarket_pphoto`
--

LOCK TABLES `mobilemarket_pphoto` WRITE;
/*!40000 ALTER TABLE `mobilemarket_pphoto` DISABLE KEYS */;
/*!40000 ALTER TABLE `mobilemarket_pphoto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mobilemarket_product`
--

DROP TABLE IF EXISTS `mobilemarket_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mobilemarket_product` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(15) NOT NULL,
  `description` longtext NOT NULL,
  `year` int(10) unsigned NOT NULL,
  `price` int(10) unsigned NOT NULL,
  `pmodel_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `mobilemarket_product_pmodel_id_fa4ec90f_fk_mobilemar` (`pmodel_id`),
  CONSTRAINT `mobilemarket_product_pmodel_id_fa4ec90f_fk_mobilemar` FOREIGN KEY (`pmodel_id`) REFERENCES `mobilemarket_pmodel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobilemarket_product`
--

LOCK TABLES `mobilemarket_product` WRITE;
/*!40000 ALTER TABLE `mobilemarket_product` DISABLE KEYS */;
/*!40000 ALTER TABLE `mobilemarket_product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-17 19:01:03
