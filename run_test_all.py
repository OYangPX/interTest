import os
import time

from interTest.comment import REPORT_PATH

import  unittest
import HTMLTestRunner



#获取测试用例路径
case_dir = os.path.join(os.getcwd(),'test/anti')



def all_case():
    discover = unittest.defaultTestLoader.discover(case_dir,pattern='test*.py', top_level_dir=None)

    return discover

if __name__ == '__main__':

    # 1、获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    # 2、html报告文件路径
    report_file = os.path.join(REPORT_PATH, "test-"+now+".html")

    # 3、打开一个文件，将result写入此file中
    with open(report_file, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                               title='接口测试',
                                               description='base')

        runner.run(all_case())
