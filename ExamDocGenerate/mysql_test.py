import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="mysite", password="mysite123456", database="mysite")

# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 查询语句
sql = "SELECT * FROM MYSITE_EXAMS"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      subject_id = row[1]
      level = row[2]
       # 打印结果
      print ("id=%s,subject_id=%s,level=%s" % \
             (id, subject_id, level))
except:
   print ("Error: unable to fetch data")
 
# 关闭数据库连接
db.close()

#------------------------------------------------------------------------------------------------------

# 打开数据库连接
db = pymysql.connect(host="localhost", user="mysite", password="mysite123456", database="mysite")
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 插入语句
sql1 = "INSERT INTO MYSITE_EXAMS(subject_id, level, total_score) \
       VALUES ('%s', '%s',  %s)" % \
       (5, 1, 20)
sql2 = "INSERT INTO MYSITE_EXAMS(subject_id, level, total_score) \
       VALUES ('%s', '%s',  %s)" % \
       ('t', 1, 20)
try:
   # 执行sql语句
   cursor.execute(sql1)
   cursor.execute(sql2)
   # 执行sql语句
   db.commit()
except:
   print ("Error: unable to insert data")
   # 发生错误时回滚
   db.rollback()
 
# 关闭数据库连接
db.close()