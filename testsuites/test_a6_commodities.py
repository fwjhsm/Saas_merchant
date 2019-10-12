import json
import random
import re
from time import sleep
from selenium import webdriver
import unittest
from selenium.webdriver.support.select import Select
from Saas_merchant.config import address_ip
from Saas_merchant.config.random_key import random_key
from Saas_merchant.config.random_mobile import random_mobile
from Saas_merchant.config.random_str import random_str
from Saas_merchant.config.redis_link import redis_link
from Saas_merchant.sreenshots.get_windows_img import get_windows_img


class indexCustomer(unittest.TestCase):
    """ 商品管理测试用例 """
    def setUp(self):
        # 隐藏浏览器
        # option = webdriver.ChromeOptions()
        # option.add_argument("headless")
        # self.driver = webdriver.Chrome(chrome_options=option)
        self.driver = webdriver.Chrome()  #显示浏览器
        self.url = address_ip.customermanage()
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # 取出cookies,添加cookies
        f1 = open("cookies.txt",'r')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for i in cookie:
            self.driver.add_cookie(i)

        self.driver.refresh()
        #点击商品管理按钮
        self.driver.find_elements_by_class_name("ant-menu-submenu-title")[1].click()
        sleep(2)

    def test_02(self):
        """测试发布商品顶部标题会否正确跳转"""
        driver = self.driver
        # 点击发布商品按钮
        driver.find_elements_by_class_name("ant-menu-item")[1].click()
        # 点击请选择商品分类
        driver.find_element_by_link_text("请选择商品分类").click()
        sleep(1)
        driver.find_element_by_link_text("完成基础信息").click()
        sleep(2)
        driver.find_element_by_link_text("销售信息").click()
        sleep(2)
        driver.find_element_by_link_text("商品描述").click()
        sleep(2)
        driver.find_element_by_link_text("提交审核").click()
        get_windows_img(driver)
        print("test_02")
        sleep(2)

    def test_03(self):
       """创建商品分组"""

       driver = self.driver
       driver.find_element_by_link_text("商品分组管理").click()
       sleep(2)
       # 点击添加分组按钮
       driver.find_elements_by_class_name("ant-btn-primary")[0].click()
       driver.find_element_by_class_name("ant-input").clear()

       driver.find_element_by_class_name("ant-input").send_keys("商品分组1")
       driver.find_elements_by_class_name("ant-btn-primary")[1].click()
       sleep(2)
       get_windows_img(driver)

    def test_04(self):
        """发布商品全部功能"""
        driver = self.driver   #ant-select-dropdown-menu-item
        # 点击发布商品按钮
        driver.find_elements_by_class_name("ant-menu-item")[1].click()
        # 选择商品分类 三级分类
        driver.find_elements_by_class_name("ant-select-arrow-icon")[0].click()
        driver.find_elements_by_class_name("ant-select-dropdown-menu-item")[2].click()

        driver.find_elements_by_class_name("ant-select-arrow-icon")[1].click()
        driver.find_elements_by_class_name("ant-select-dropdown-menu-item")[9].click()

        driver.find_elements_by_class_name("ant-select-arrow-icon")[2].click()
        driver.find_elements_by_class_name("ant-select-dropdown-menu-item")[25].click()
        sleep(3)
        # 输入商品标题

        for i in range(random.randint(1, 1000), 1001):
            driver.find_element_by_id("shopTitle").send_keys("自动化测试用商品名称"+str(i))
            break
        # 选择商品分组
        driver.find_elements_by_class_name("ant-select-arrow-icon")[3].click()
        driver.find_element_by_class_name("ant-select-tree-title").click()



    def tearDown(self):
        self.driver.quit()