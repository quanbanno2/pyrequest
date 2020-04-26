import unittest
import requests
import sys
from config import BaseConfig

sys.path.append(BaseConfig.BASE_DIR)


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.host = BaseConfig.host
        cls.crm_host = BaseConfig.crm_host

    @staticmethod
    def post(url, data=None, json=None, **kwargs):
        r = requests.post(url, data, json, **kwargs)
        return r

    @staticmethod
    def get(url, params=None, **kwargs):
        r = requests.get(url, params, **kwargs)
        return r


def run():
    unittest.main()
