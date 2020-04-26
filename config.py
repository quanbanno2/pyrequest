import os


class BaseConfig:
    host = "http://127.0.0.1:8000"
    crm_host = "http://gaofenyun.com:8073"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class MysqlConfig:
    host = "127.0.0.1"
    port = "3306"
    database = "guest_test"
    user = "root"
    password = "123456"
    charset = 'utf8mb4'
