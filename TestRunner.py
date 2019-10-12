import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os

# 定义输出的文件位置和名字
DIR = os.getcwd()+"\\report_html\\"

nowtime = time.strftime("%Y%m%d%H%M")

filename = nowtime + "report.html"
# discover方法执行测试套件

test_dir = os.getcwd()+"\\testsuites\\"

discover = unittest.defaultTestLoader.discover(
    test_dir,
    pattern='test_a*.py',
    top_level_dir=None
)

with open(DIR + filename, 'wb') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title='猪猪建材商家Saas平台',
        description='执行情况',
        # tester='tester'
    )
    runner.run(discover)



