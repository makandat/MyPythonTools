-- バイナリーデータ
CREATE TABLE `Binaries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `original` varchar(300) DEFAULT NULL,
  `datatype` char(10) DEFAULT NULL,
  `data` blob,
  `info` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
