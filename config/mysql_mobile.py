import random
import re

import pymysql


localhost = "192.168.199.240"
port = 3306
username = "root"
password = "Pass123!"
# 链接数据库
db = pymysql.connect(host=localhost,
                     port=port,
                     user=username,
                     passwd=password,
                     database="manager",
                     charset = "utf8"
                     )
j = random.randint(1,1000)

# 从数据库中获取商家手机号，只获取已入驻商家手机号  随机获取是个值
sql = """SELECT t1.mobile from t_material_user_account t1,t_material_shop t2 where t1.user_code = t2.user_code
 order by rand() limit 10"""
cur = db.cursor()
cur.execute(sql)  #执行sql语句
results = cur.fetchall()
def mysql_mobile():
    for i in results:
        i = str(i)
        value = re.search("(\d+)",i).group()

        value1 = re.match(r"([1][35789][0-9]{9})",str(value))
        return value1.group(0)
db.close()
# mysql_mobile()
print(mysql_mobile())

