import random
import re
import pymysql
from Saas_merchant.config.mysql_mobile import mysql_mobile

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
# 根据查询到的手机号 获取该用户加密后密码
sql = """select password from t_material_user_account where mobile = %s"""
cur = db.cursor()
cur.execute(sql,[mysql_mobile()])  #执行sql语句

# 获得一条数据
results = cur.fetchone()

def mysql_password():
    # re 提取出密码
    value = re.search("(\w+)",str(results)).group()
    return value

db.close()

print(mysql_password())