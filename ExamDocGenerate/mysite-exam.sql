DROP TABLE IF EXISTS `mysite_exam_subjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysite_exam_subjects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(63) NOT NULL DEFAULT '' COMMENT '学科名称：高数，英语之列',
  `subset1` varchar(63) COMMENT '学科子类：英语四级,六级',
  `subset2` varchar(63) COMMENT '学科子类：英语四级,六级',
  `desc` varchar(255) COMMENT '学科介绍',
  `add_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `deleted` tinyint(1) DEFAULT '0' COMMENT '逻辑删除',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1036007 DEFAULT CHARSET=utf8mb4 COMMENT='类目表';
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS `mysite_exam_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysite_exam_items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_id` int(11) NOT NULL COMMENT '学科号：高数，英语之类',
  `type` int(11) NOT NULL DEFAULT '1' COMMENT '题型：选择题(1)，填空题(2)，问答题(3) 之类',
  `level` int(11) NOT NULL DEFAULT '1' COMMENT '级别：简单(1)，普通(2)，困难(3)，噩梦(4)',
  `keywords` varchar(255) COMMENT '[冒泡排序，算法，排序问题]',
  `short_desc` varchar(255)COMMENT '这是模拟题目',
  `question` text COMMENT '{json}',
  `answer` text COMMENT '{json}',
  `score` int(11) NOT NULL COMMENT '2, 5, 10 分每题',
  `analysis` text COMMENT '解析',
  `add_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `deleted` tinyint(1) DEFAULT '0' COMMENT '逻辑删除',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COMMENT='考试表';
/*!40101 SET character_set_client = @saved_cs_client */;

DROP TABLE IF EXISTS `mysite_exams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysite_exams` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_id` int(11) NOT NULL COMMENT '学科号：高数，英语之类',
  `level` int(11) NOT NULL DEFAULT '1' COMMENT '试卷级别：简单，普通，困难，噩梦',
  `total_score` int(11) NOT NULL COMMENT '100分',
  `keywords` varchar(255) COMMENT '[武汉纺织大学，专升本模拟考试]',
  `short_desc` varchar(255) COMMENT '这是模拟题目',
  `content` text COMMENT '{json}',
  `add_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `deleted` tinyint(1) DEFAULT '0' COMMENT '逻辑删除',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COMMENT='考试表';
/*!40101 SET character_set_client = @saved_cs_client */;
