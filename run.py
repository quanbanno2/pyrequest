import unittest
import time

from HTMLTestRunner import HTMLTestRunner

cases = unittest.defaultTestLoader.discover("./interface", "test_*.py")

time_tag = time.strftime("%Y-%m-%d %H:%M:%S")

with(open('./reports/' + time_tag + '_result.html', 'wb')) as fp:
    runner = HTMLTestRunner(stream=fp,
                            title='发布会签到系统接口自动化测试',
                            description='运行环境：MySQL(PyMySQL), Requests, unittest ')
    runner.run(cases, rerun=0, save_last_run=False)
