SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for dytt_movies
-- ----------------------------
DROP TABLE IF EXISTS `dytt_movies`;
CREATE TABLE `dytt_movies` (
  `mid` int(11) NOT NULL AUTO_INCREMENT,
  `mhome` varchar(80) DEFAULT '' COMMENT '网站名字',
  `classic` varchar(50) DEFAULT NULL COMMENT '视频分类',
  `mname` varchar(50) NOT NULL COMMENT '电影名称',
  `mdesc` text,
  `mtime` datetime DEFAULT NULL COMMENT '上映时间',
  `hot` int(11) DEFAULT NULL COMMENT '热度',
  `makedate` date DEFAULT NULL COMMENT '创建日期',
  `maketime` time DEFAULT NULL COMMENT '创建时间',
  `modifydate` date DEFAULT NULL COMMENT '修改日期',
  `modifytime` time DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for dytt_download
-- ----------------------------
DROP TABLE IF EXISTS `dytt_download`;
CREATE TABLE `dytt_download` (
  `downid` int(11) NOT NULL AUTO_INCREMENT COMMENT '下载ID',
  `mid` int(11) NOT NULL COMMENT '电影ID',
  `downloadurl` text NOT NULL COMMENT '下载地址',
  `makedate` date DEFAULT NULL COMMENT '创建日期',
  `maketime` time DEFAULT NULL COMMENT '创建时间',
  `modifydate` date DEFAULT NULL COMMENT '修改日期',
  `modifytime` time DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`downid`,`mid`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for dytt_log
-- ----------------------------
DROP TABLE IF EXISTS `dytt_log`;
CREATE TABLE `dytt_log` (
  `logid` int(11) NOT NULL AUTO_INCREMENT COMMENT '日志id',
  `home` varchar(100) DEFAULT NULL COMMENT '发生对象',
  `errorinfo` text COMMENT '错误描述',
  `datetime` datetime DEFAULT NULL COMMENT '发生时间',
  PRIMARY KEY (`logid`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
