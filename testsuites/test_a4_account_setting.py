import json
import re
from time import sleep
from selenium import webdriver
import unittest

from Saas_merchant.config import address_ip
from Saas_merchant.config.random_mobile import random_mobile
from Saas_merchant.config.redis_link import redis_link
from Saas_merchant.sreenshots.get_windows_img import get_windows_img


class indexAccountSetting(unittest.TestCase):
    """ 主页账户设置测试用例 """
    def setUp(self):
        # 隐藏浏览器

        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=option)
        # self.driver = webdriver.Chrome()  #隐藏
        self.url = address_ip.setting()
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
        sleep(2)
        driver = self.driver
        driver.find_elements_by_class_name("anticon")[10].click()
        driver.find_element_by_link_text("账户资料").click()
        text = driver.find_elements_by_class_name("text-muted")[1].text
        self.assertIn("昵称", text)
        get_windows_img(driver)

    def test_01(self):
        """更改昵称"""

        driver = self.driver
        driver.find_elements_by_class_name("ant-btn-background-ghost")[1].click()
        value = "昵称" + str(random_mobile())
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys(value)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/form/div[2]/div/div/span/div/button[2]").click()
        sleep(5)
        self.assertIn("","")
        get_windows_img(driver)

    def test_02(self):
        """更改绑定手机号"""
        driver = self.driver
        # 获取当前绑定手机号
        value = driver.find_elements_by_class_name("text-darkgrey")[1].text
        # 使用 re 提取出手机号
        value = re.match("(\d+)",value)

        driver.find_elements_by_class_name("accountDatumBtn")[0].click()
        driver.find_element_by_class_name("ant-btn-background-ghost").click()
        sleep(3)
        # 根据手机号发送验证码
        driver.find_element_by_id("userCode").send_keys(redis_link(value.group(0)))
        driver.find_elements_by_class_name("ant-btn-primary")[1].click()
        sleep(3)
        #重置手机号
        driver.find_element_by_id("userPhone").send_keys(random_mobile())
        # 获取手机文本框手机号
        mobile = driver.find_element_by_id("userPhone").get_attribute("value")
        # 点击发送
        driver.find_element_by_class_name("ant-btn-background-ghost").click()

        # 根据获取手机号，从redis中获取验证码
        sleep(2)
        driver.find_element_by_id("userCode").send_keys(redis_link(mobile))
        # 点击提交
        driver.find_element_by_xpath('//*[@id="__next"]/section/section/section/main/form/div[3]/div/div/span/div/button').click()
        sleep(5)
        # 截图
        get_windows_img(driver)

    def test_03(self):
        """更改密码"""

        driver = self.driver
        # 获取当前绑定手机号
        value = driver.find_elements_by_class_name("text-darkgrey")[1].text
        # 使用 re 提取出手机号
        value = re.match("(\d+)", value)
        # 点击更改密码按钮
        driver.find_elements_by_class_name("accountDatumBtn")[1].click()
        # 点击发送验证码按钮
        driver.find_element_by_class_name("ant-btn-background-ghost ").click()
        sleep(1)
        # 根据手机号填入验证码
        driver.find_element_by_id("userCode").send_keys(redis_link(value.group()))
        # 点击下一步按钮
        driver.find_elements_by_class_name("ant-btn-block")[1].click()
        # 输入密码，确认密码
        driver.find_element_by_id("password").send_keys("123456..")
        driver.find_element_by_id("confirm").send_keys("123456..")
        # 点击完成按钮
        driver.find_element_by_class_name("ant-btn-primary ").click()
        get_windows_img(driver)


    def tearDown(cls):
        cls.driver.quit()
