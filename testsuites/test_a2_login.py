import json
from time import sleep
from selenium import webdriver
import unittest

from Saas_merchant.config import address_ip
from Saas_merchant.config.mysql_mobile import mysql_mobile
from Saas_merchant.config.mysql_password import mysql_password
from Saas_merchant.config.random_mobile import random_mobile
from Saas_merchant.config.random_str import random_str
from Saas_merchant.config.redis_link import redis_link
from Saas_merchant.sreenshots.get_windows_img import get_windows_img


class login(unittest.TestCase):
    """登录测试用例"""
    def setUp(self):
        # 隐藏浏览器
        #
        # option = webdriver.ChromeOptions()
        # option.add_argument("headless")
        # self.driver = webdriver.Chrome(chrome_options=option)

        self.driver = webdriver.Chrome()  #显示浏览器
        self.url = address_ip.login()
        self.driver.get(self.url)
        # self.driver.add_cookie({"name":"SellerMid","value":"%7B%22userCode%22%3A%222019070900003%22%2C%22shopId%22%3A2058%2C%22shopState%22%3A1%2C%22shopStatus%22%3A1%7D"})
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        sleep(2)

    def test_04(self):
        """正确密码登录"""
        try:
            driver = self.driver
            # driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(mysql_mobile())
            driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(mysql_mobile())
            mobile = driver.find_element_by_xpath('//*[@id="mobile"]').get_attribute("value")

            driver.find_element_by_xpath('//*[@id="password"]').send_keys(redis_link(mobile))
            driver.find_element_by_xpath('//*[@id="__next"]/section/main/aside/div[2]/div/div[3]/div[1]/form/div[3]/button').click()
            sleep(3)
            title = driver.title
            print(title)
            # 取到cookies


            self.assertEqual(title,"商家中心-商家中心")
        except Exception as e:
            get_windows_img(self.driver)

    def test_02(self):
        """账户不存在登录"""

        driver = self.driver
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(random_mobile())
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456..")
        driver.find_element_by_xpath(
            '//*[@id="__next"]/section/main/aside/div[2]/div/div[3]/div[1]/form/div[3]/button').click()
        sleep(3)
        text = driver.find_element_by_xpath('//*[@id="__next"]/section/main/aside/div[2]/div/div[3]/div[1]/form/div[1]/div/div/div').text

        try:
            self.assertEqual(text,"账户不存在")
            get_windows_img(driver)
        except Exception as e:
           raise "账户不存在出错%s"%e

    def test_03(self):
        """账号输入框校验"""
        driver = self.driver

        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(random_str())
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(random_str())
        driver.find_element_by_xpath(
            '//*[@id="__next"]/section/main/aside/div[2]/div/div[3]/div[1]/form/div[3]/button').click()
        sleep(3)
        text = driver.find_element_by_xpath('/html/body/div/section/main/aside/div[2]/div/div[3]/div[1]/form/div[1]/div/div/div').text
        try:
            self.assertEqual(text,"请输入正确的手机号码")
            get_windows_img(driver)
        except Exception:
            get_windows_img(driver)

    def test_01(self):
        """正确验证码登录 并保存cookie"""
        driver = self.driver

        driver.find_element_by_xpath(
            '//*[@id="__next"]/section/main/aside/div/div/div[1]/div/div/div/div/div[1]/div[2]').click()
        sleep(2)
        driver.find_elements_by_xpath('//*[@id="mobile"]')[1].send_keys(mysql_mobile())
        #获取输入框手机号
        text = driver.find_elements_by_xpath('//*[@id="mobile"]')[1].get_attribute("value")

        driver.find_element_by_class_name("clickSend").click()
        sleep(2)
        #redis_link() 根据text，自动去redis中获取值
        driver.find_element_by_id("captchaCode").send_keys(redis_link(text))
        driver.find_element_by_xpath(
        '// * [ @ id = "__next"] / section / main / aside / div / div / div[3] / div[2] / form / div[3] / button').click()
        sleep(2)

        # 取到cookies
        cookies = driver.get_cookies()
        f = open("cookies.txt", "w")
        f.write(json.dumps(cookies))
        f.close()
        # //*[@id="__next"]/section/main/aside/div/div/div[1]/div/div/div/div/div[1]/div[2]
        text = driver.title
        try:
            self.assertEqual("商家中心-商家中心", text)
            get_windows_img(driver)
        except Exception:
            get_windows_img(driver)

    def test_05(self):
        """错误验证码登录"""
        driver = self.driver

        driver.find_element_by_xpath("/html/body/div/section/main/aside/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]").click()
        sleep(2)
        driver.find_elements_by_xpath('//*[@id="mobile"]')[1].send_keys(mysql_mobile())
        sleep(2)
        driver.find_element_by_class_name("clickSend").click()
        driver.find_element_by_id("captchaCode").send_keys("1234")
        driver.find_element_by_xpath("/html/body/div/section/main/aside/div[2]/div/div[3]/div[2]/form/div[3]/button").click()
        text = driver.find_element_by_class_name("ant-form-explain").text

        try:
            self.assertEqual("短信验证码错误或已失效",text)
            get_windows_img(driver)
        except Exception:
            get_windows_img(driver)

    def test_06(self):
        """二维码失效验证"""
        driver = self.driver
        try:
            driver.find_element_by_class_name("scanCode").click()
            sleep(3)
            text = driver.find_element_by_class_name("text-white").text

            self.assertEqual("二维码失效", text)
            get_windows_img(driver)
        except:
            get_windows_img(driver)

    def test_07(self):
        """注册功能按钮"""
        driver = self.driver
        driver.find_element_by_link_text("去注册").click()
        try:
            title = driver.title
            self.assertEqual("注册", title)
            get_windows_img(driver)
        except Exception as e:
            raise e

    def tearDown(self):
        self.driver.quit()

