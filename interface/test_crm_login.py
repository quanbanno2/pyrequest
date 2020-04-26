from common1 import TestCase, run
from ddt import ddt, data, unpack
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

# from data_init.testdata import init_data


@ddt
class TestCrmLogin(TestCase):

    def setUp(self):
        self.base_url = self.crm_host + "/crm-web/doLogin.action"

    @data(
        ['{"loginName":"高分云辅导督导1","password":"e10adc3949ba59abbe56e057f20f883e"}', '高分云辅导督导1', True]
    )
    @unpack
    def test_crm_login(self, requestJson, loginName, flag):
        request_data = {"requestJson": requestJson}
        r = self.post(self.base_url, data=request_data)
        rj = r.json()
        # print(rj["data"][0]["loginName"])
        # print(rj)
        # print(rj["flag"])
        self.assertEqual(rj["data"][0]["loginName"], loginName)
        self.assertEqual(rj["flag"], flag)


if __name__ == '__main__':
    # init_data()
    run()
