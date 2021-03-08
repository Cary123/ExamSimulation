import random
# 导入pymysql模块
import pymysql
 
from docxtpl import DocxTemplate
from docxtpl import InlineImage
 
from docx.shared import Mm,Inches,Pt
import datetime
 
def jisuan():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    if a + b <= 100:
        print("%s + %s =  " % (a, b))
        nums_n = "%s + %s = " % (a, b)
    elif a - b < 0:
        print(" %s - %s =  " % (b, a))
        nums_n = "%s - %s = " % (b, a)
    else:
        if a > b:
            print("%s - %s =  " % (a, b))
            nums_n = "%s - %s =  " % (a, b)
        else:
            if a + b > 100:
                print(" %s - %s =  " % (b, a))
                nums_n = "%s - %s =  " % (b, a)
            else:
                print("%s + %s =  " % (a, b))
                nums_n = "%s + %s =  " % (a, b)


def yy_def():
    re = random.randint(1, 274)
    # 获取连接
    conn = pymysql.connect(host="localhost",
                           db="mysite",
                           user="mysite",
                           password="mysite123456",
                           port=3306,
                           charset="utf8")
    # 获取游标
    cur = conn.cursor()
    print(cur)
    # SQL 查询语句
    sql = "SELECT * FROM YY \
           WHERE ID = %s" % re
    try:
        # 执行SQL语句
        cur.execute(sql)
        # 获取所有记录列表
        results = cur.fetchall()
        print(results[0][1])
        yy = results[0][1]
    except:
        print("未获取到")
    cur.close()
    conn.commit()
    conn.close()
    print('sql执行成功')
    return yy

 
ii = 1
aa = 1
i = 1
n_zd = {}
yy_zd = {}
timu_yy = {}
while aa <= 60:
 
    while i <= 28:
        n_key = "n%s" % i
        print(n_key)
        n_zd[n_key] = jisuan()
        print(n_zd)
        i += 1
 
    while ii <= 2:
        y_key = "y%s" % ii
        print(y_key)
        yy_zd[y_key] = yy_def()
        print(yy_zd)
        ii += 1
 
    aa_key = "t1"
    timu_yy[aa_key] = aa
    data_dic = {**timu_yy, **n_zd, **yy_zd}
    print(data_dic)
    doc = DocxTemplate('tpll.docx')   # 加载模板文件
    doc.render(data_dic) #填充数据
    # doc_name = "数学暑假作业%s" % aa + datetime.datetime.now().strftime('%Y%m%d%H%M') + ".docx"
    doc_name = "./数学/数学暑假作业%s.docx" % aa
    doc.save(doc_name) #保存目标文件
    aa += 1
    i = 1
    ii = 1