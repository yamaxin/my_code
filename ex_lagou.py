from selenium import webdriver
import unittest, time
from selenium.webdriver.common.action_chains import ActionChains

class LaGouTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_lagou(self):
        self.LoginLaGou()
        self.search()

        for page in range(30):
            page = 0
            for i in range(15):
                # 获取列表信息
                job_titles = self.driver.find_elements_by_css_selector('.position_link > h3')
                money = self.driver.find_elements_by_css_selector('.money')
                companys = self.driver.find_elements_by_css_selector('.company_name > a')
                # 职位
                job_title = str(job_titles[i].text)
                # 薪资
                salary = str(money[i].text)
                # 公司
                company_name = str(companys[i].text)
                list_text = '职位：%s' % job_title, '薪资：%s' % salary, '公司：%s' % company_name
                print(list_text)

                # 获取当前窗口
                list_handle = self.driver.current_window_handle
                # 点击招聘信息，打开招聘信息窗口
                job_info = job_titles[i].click()

                # 切换至招聘信息窗口
                handles = self.driver.window_handles

                for handle in handles:
                    if handle != list_handle:
                        self.driver.switch_to.window(handle)  # 切换到招聘信息页面
                    time.sleep(5)
                # 招聘信息页面-职位诱惑信息
                job_advantage = str(self.driver.find_element_by_css_selector('.advantage + p').text)
                # 招聘信息页面-职位描述信息
                job_bt = str(self.driver.find_element_by_xpath('// *[ @ id = "job_detail"] / dd[2] / div').text)

                page_text = '招聘信息-职位诱惑：%s' % job_advantage, '招聘信息-职位描述：%s' % job_bt
                print(page_text)
                self.driver.close()  # 关闭当前招聘信息窗口

                # 切换回第一个窗口（列表页面）
                self.driver.switch_to.window(list_handle)

                # 文本文件写入信息
                job_data = str(list_text)+ str(page_text)
                self.write_data(job_data)

            # 翻页
            self.next_page()
            page += 1
            time.sleep(10)


    def LoginLaGou(self):
        '''登录拉勾网'''
        self.driver.get("https://www.lagou.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # 点击登录按钮
        select_wuhan = self.driver.find_element_by_link_text("武汉站")
        select_wuhan.click()
        login = self.driver.find_element_by_xpath("//ul[@class='lg_tbar_r']/li[1]/a")
        login.click()
        time.sleep(3)

        # 输入用户名密码登录
        username = self.driver.find_element_by_xpath("//form[@class='active']/div[1]/input")
        password = self.driver.find_element_by_xpath("//form[@class='active']/div[2]/input")
        submit = self.driver.find_element_by_xpath("//form[@class='active']/div[5]/input")
        username.send_keys('18672968031')
        password.send_keys('15872411180k')
        submit.click()
        time.sleep(10)

    def search(self):
        '''搜索测试开发'''
        search_box = self.driver.find_element_by_css_selector('#search_input')
        search_button = self.driver.find_element_by_css_selector('#search_button')
        search_box.send_keys('测试开发')
        search_button.click()
        time.sleep(5)

    def write_data(self, job_data):
        with open("job_info.txt", 'a+')as f:
            data = job_data.encode("gbk","ignore").decode("gbk")
            f.write(data)
            f.write("\n")
            f.close()

    def next_page(self):
        '''翻页'''
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        next_page = self.driver.find_element_by_css_selector('.pager_next ')
        ActionChains(self.driver).move_to_element(next_page).perform()
        time.sleep(3)
        next_page.click()

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()



