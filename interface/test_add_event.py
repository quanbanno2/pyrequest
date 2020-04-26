from common1 import TestCase, run
from ddt import ddt, data, unpack
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from data_init.testdata import init_data


@ddt
class TestAddEvent(TestCase):

    def setUp(self):
        self.base_url = self.host + "/api/add_event/"

    @data(
        ['5', "测试沙龙", "", 10021, "深圳", "2020-05-05 12:00:00", "参数错误"],
        ['2', "测试沙龙", "2000", 10022, "深圳", "2020-05-05 12:00:00", "发布会已存在"],
        ['5', "红米Pro发布会", "2000", 10023, "深圳", "2020-05-05 12:00:00", "发布会名称已存在"],
        ['5', "测试沙龙", "2000", 10024, "深圳", "2020-05-15 12:-0:00",
         "开始时间格式错误. It must be in YYYY-MM-DD HH:MM:SS format."],
        ['5', "测试沙龙", "200", 200, "深圳", "2020-05-05 12:00:00", "添加成功"],
    )
    @unpack
    def test_add_event(self, eid, name, limit, status, address, start_time, message):
        request_data = {"eid": eid, "name": name, "limit": limit, "address": address, "start_time": start_time}
        r = self.post(self.base_url, data=request_data)
        rj = r.json()
        print(rj)
        self.assertEqual(rj["status"], status)
        self.assertEqual(rj["message"], message)


if __name__ == '__main__':
    init_data()
    run()
