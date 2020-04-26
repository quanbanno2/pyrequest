import pymysql
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from config import MysqlConfig

connection = pymysql.connect(host=MysqlConfig.host,
                             user=MysqlConfig.user,
                             password=MysqlConfig.password,
                             db=MysqlConfig.database,
                             charset=MysqlConfig.charset)

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `guest_test`.`auth_user` "
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)

finally:
    connection.close()
