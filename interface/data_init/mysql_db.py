import pymysql
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from config import MysqlConfig

from data_init import testdata


class DB:

    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=MysqlConfig.host,
                                              port=int(MysqlConfig.port),
                                              user=MysqlConfig.user,
                                              password=MysqlConfig.password,
                                              db=MysqlConfig.database)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # clear table data
    def clear(self, table_name) -> None:
        # real_sql = "truncate table " + table_name + ";"
        real_sql = "delete from {};".format(table_name)
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    # insert sql statement
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
            # print(table_data[key])

        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO {} ({}) VALUES ({})".format(table_name, key, value)
        # print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    # close database
    def close(self):
        self.connection.close()

    # init data
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()


if __name__ == '__main__':
    aabb = DB()
    # aabb.clear("sign_guest")
    aabb.init_data(testdata.datas)
    # data = {"id": '1', "realname": "alen", "phone": "12345678", "email": "adsfaf@gmail.com", "sign": 0,
    #         "create_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "event_id": 3}
    # aabb.insert('sign_guest', data)
