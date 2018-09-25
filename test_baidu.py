from selenium import webdriver
import unittest
from time import sleep

# 在整个模块的开始与结束时被执行
def setUpModule():
    pass
def tearDownModule():
    pass

class BaiduTest(unittest.TestCase):
    '''百度搜索测试'''
    # setUpClass/tearDownClass：在测试类的开始与结束时被执
    @classmethod
    def setUpClass(cls):  # 节省了浏览器开启和关闭次数
        cls.dr = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):  # 节省了浏览器开启和关闭次数
        cls.dr.quit()

    # setUp/tearDown ： 在测试用例的开始与结束时被执(即每条用例开始结束都会执行一次)
    def setUp(self):
        # self.dr = webdriver.Chrome()
        self.baseURL = 'http://www.baidu.com'
        with open('./info.txt','r') as info_file:
            self.data = info_file.readlines()

    def tearDown(self):
        pass # self.dr.quit()

    def baidu_search(self, search_key):  # 这不是测试用例，只是一个普通的方法
        '''搜索关键字：HTMLTestRunner'''
        self.dr.find_element_by_id('kw').clear()
        self.dr.find_element_by_id('kw').send_keys(search_key)
        self.dr.find_element_by_id('su').click()
        sleep(2)

    # 以test开头的计算为一条用例

    def test_baidu1(self):
        self.dr.get(self.baseURL)
        self.baidu_search(self.data[0])


    def test_baidu2(self):
        self.dr.get(self.baseURL)
        self.baidu_search(self.data[1])


    def test_baidu3(self):
        self.dr.get(self.baseURL)
        self.baidu_search(self.data[2])


if __name__=='__main__':
    unittest.main()
    # 测试套件，用来存放测试用例的集合
    '''suit = unittest.TestSuite()
    suit.addTest(BaiduTest('test_baidu1'))

    # 测试运行器，用来运行测试套件中的用例
    runner = unittest.TextTestRunner()
    runner.run(suit)'''



#__init__.py 用来标识一个普通的文件夹为标准的python模块。