from selenium import webdriver
import unittest
from time import sleep

from Saas_merchant.config import address_ip
from Saas_merchant.config.chrom_option import option_Chrom

from Saas_merchant.config.mysql_mobile import mysql_mobile
from Saas_merchant.config.random_mobile import random_mobile
from Saas_merchant.config.redis_link import redis_link
from Saas_merchant.sreenshots.get_windows_img import get_windows_img

class register(unittest.TestCase):
    """注册测试用例"""
    def setUp(self):

        # 隐藏浏览器
        # option = webdriver.ChromeOptions()
        # option.add_argument("headless")
        # self.driver = webdriver.Chrome(chrome_options=option)

        self.driver = webdriver.Chrome()   #显示浏览器
        self.url = address_ip.register()

        self.driver.get(self.url)
        # self.driver.add_cookie({"name":"SellerMid","value":"%7B%22userCode%22%3A%222019070900003%22%2C%22shopId%22%3A2058%2C%22shopState%22%3A1%2C%22shopStatus%22%3A1%7D"})
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        sleep(2)
        pass

    def test_01(self):
        """已注册手机号重新注册"""
        driver = self.driver
        driver.find_elements_by_class_name("ant-input-lg")[0].send_keys(mysql_mobile())
        driver.find_element_by_class_name("btn-sendCode").click()
        text = driver.find_element_by_class_name("ant-form-explain").text
        try:
            self.assertEqual("您已注册请直接登录",text)
            get_windows_img(driver)

        except:
            get_windows_img(driver)

    def test_02(self):
        """未注册手机号注册 设置密码不一致校验"""
        driver = self.driver

        driver.find_elements_by_class_name("ant-input-lg")[0].send_keys(random_mobile())
        driver.find_element_by_class_name("btn-sendCode").click()
        sleep(4)
        mobile = driver.find_elements_by_class_name("ant-input-lg")[0].get_attribute("value")
        driver.find_elements_by_class_name("ant-input-lg")[1].send_keys(redis_link(mobile))
        driver.find_element_by_xpath("/html/body/div/section/section/div[3]/div/form/div[4]/div/div/span/button").click()
        sleep(2)
    #     设置密码  两次密码不一致校验
        driver.find_elements_by_class_name("ant-input-lg")[0].send_keys("A2SSass11..")
        driver.find_elements_by_class_name("ant-input-lg")[1].send_keys("A2SSass11.")
        sleep(3)
        password_hint = driver.find_element_by_class_name("ant-form-explain").text
        #
        try:
            self.assertIn("两次密码输入不一致", password_hint)
            get_windows_img(driver)
        except Exception:
            get_windows_img(driver)
    def test_03(self):
        """未注册手机号注册 设置密码强度较弱"""
        driver = self.driver
        driver.find_elements_by_class_name("ant-input-lg")[0].send_keys(random_mobile())
        sleep(2)
        driver.find_element_by_class_name("btn-sendCode").click()
        mobile = driver.find_elements_by_class_name("ant-input-lg")[0].get_attribute("value")
        print(mobile,"输入框的手机号")
        print(type(mobile),"输入框的手机号类型")
        sleep(2)
        driver.find_elements_by_class_name("ant-input-lg")[1].send_keys(redis_link(mobile))
        driver.find_element_by_xpath(
            "/html/body/div/section/section/div[3]/div/form/div[4]/div/div/span/button").click()
        sleep(2)
        #     设置密码  两次密码不一致校验
        driver.find_elements_by_class_name("ant-input-lg")[0].send_keys("123456789")
        driver.find_elements_by_class_name("ant-input-lg")[1].send_keys("123456789")
        sleep(3)
        password_hint = driver.find_element_by_class_name("ant-form-explain").text
            #
        try:
            self.assertIn("密码强度较弱", password_hint)
            get_windows_img(driver)
        except Exception:
            get_windows_img(driver)

    def test_04(self):
        """未注册手机号注册 密码长度较短"""
        driver = self.driver

        driver.find_elements_by_class_name("ant-input-lg")[0].send_keys(random_mobile())

        driver.find_element_by_class_name("btn-sendCode").click()
        sleep(1)
        mobile = driver.find_elements_by_class_name("ant-input-lg")[0].get_attribute("value")
        driver.find_elements_by_class_name("ant-input-lg")[1].send_keys(redis_link(mobile))
        driver.find_element_by_xpath(
            "/html/body/div/section/section/div[3]/div/form/div[4]/div/div/span/button").click()
        sleep(2)
        #     设置密码  两次密码不一致校验
        driver.find_elements_by_class_name("ant-input-lg")[0].send_keys("1234")
        driver.find_elements_by_class_name("ant-input-lg")[1].send_keys("1234")
        sleep(3)
        password_hint = driver.find_element_by_class_name("ant-form-explain").text
        #
        try:
            self.assertIn("请输入6~20位密码", password_hint)
            get_windows_img(driver)
        except Exception:
            get_windows_img(driver)


    def test_05(self):
        """未注册手机号注册 注册成功"""
        driver = self.driver

        driver.find_elements_by_class_name("ant-input-lg")[0].send_keys(random_mobile())
        driver.find_element_by_class_name("btn-sendCode").click()
        sleep(2)
        mobile = driver.find_elements_by_class_name("ant-input-lg")[0].get_attribute("value")
        driver.find_elements_by_class_name("ant-input-lg")[1].send_keys(redis_link(mobile))
        driver.find_element_by_xpath(
            "/html/body/div/section/section/div[3]/div/form/div[4]/div/div/span/button").click()

        sleep(2)
        #     设置密码  两次密码不一致校验
        driver.find_elements_by_class_name("ant-input-lg")[0].send_keys("123456..")
        driver.find_elements_by_class_name("ant-input-lg")[1].send_keys("123456..")
        # sleep(3)
        # password_hint = driver.find_element_by_class_name("ant-form-explain").text
        driver.find_elements_by_class_name("ant-btn-block")[0].click()
        sleep(2)
        try:
            get_windows_img(driver)
        except Exception:
            get_windows_img(driver)


    def tearDown(self):
        self.driver.quit()


