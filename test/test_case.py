#encoding:utf-8

import os
import unittest
import HTMLTestRunner
import requests
import time
import ddt

from interTest.comment.ReadYaml import YamlReader
from interTest.comment import REPORT_PATH,BASE_PATH
from interTest.comment.log import logger


@ddt.ddt
class AntiFeature(unittest.TestCase):

    @classmethod
    def setUpClass(self):
       logger.info('××××××××××××××××start××××××××××××××××××\n')

    case_path = os.path.join(BASE_PATH, 'config', 'case.yaml')
    case_data = YamlReader(case_path).data


    @ddt.file_data(case_path)
    #@ddt.data(*case_data)
    @ddt.unpack
    def test_case(self,**kwargs):
        logger.info('【测试数据】：%s' % kwargs)
        for key in kwargs.keys():
            self.case_no = kwargs.get('case_no')
            self.case_name = kwargs['case_name']
            self.method = kwargs.get('method')
            self.header = kwargs.get('header')
            self.data = kwargs.get('data', '')
            self.url = kwargs.get('url')
            self.check = kwargs.get('check')
            self.api_url = kwargs.get('api_url')
            self.cookie = kwargs.get('cookie', {})
            self.is_json = kwargs.get('is_json', '')

        url = '%s' % self.url
        logger.info('执行测试案例编号：%s 测试案例名称：%s' % (self.case_no, self.case_name))
        print('执行测试案例编号：%s 测试案例名称：%s' % (self.case_no, self.case_name))
        logger.info('请求参数：%s' % self.data)
        print('请求参数：%s' % self.data)
        try:
            if self.method == 'post':
                if self.is_json:
                    res = requests.post(url, json=self.data, headers=self.header, cookies=self.cookie)
                else:
                    res = requests.post(url, data=self.data, headers=self.header, cookies=self.cookie)
            elif self.method == 'get':
                res = requests.get(url, params=self.data, headers=self.header, cookies=self.cookie)
            elif self.method == 'put':
                res = requests.get(url, params=self.data, headers=self.header, cookies=self.cookie)
            elif self.method == 'delete':
                res = requests.get(url, params=self.data, headers=self.header, cookies=self.cookie)
            elif self.method == 'options':
                res = requests.get(url, params=self.data, headers=self.header, cookies=self.cookie)
            elif self.method == 'patch':
                res = requests.get(url, params=self.data, headers=self.header, cookies=self.cookie)
        except BaseException as Error:
            logger.info('接口请求链接异常：%s\n' % Error)
            raise Error



        # 验证结果
        logger.info('请求接口地址：%s' % res.url)
        print('请求接口地址：%s' % res.url)
        logger.info('接口响应结果:%s' % res.json())

        print('接口执行结果：%s' % res.json())
        logger.info('检查条件：%s\n' % (self.check))

        # 检查值为字典
        # if self.check is
        for ch_key, ch_val in self.check.items():
            self.assertEqual(res.json().get(ch_key), self.check[ch_key])
        # 检查值为list
        for key in self.check:
            self.assertIn(key, res.text)


    @classmethod
    def tearDownClass(self):
        '''测试结束'''
        logger.info('××××××××××××××××end××××××××××××××××××')




if __name__ == "__main__":

    #添加测试案例到测试集
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AntiFeature))



    # 1、获取当前时间，这样便于下面的使用
    now = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    # 2、html报告文件路径
    report_file = os.path.join(REPORT_PATH, "test-" + now + ".html")
    print(report_file)
    # 3、打开一个文件，将result写入此file中
    with open(report_file, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                               title='接口测试',
                                               description='base')

        runner.run(suite)

