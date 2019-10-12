import json
import os
from time import sleep
from selenium import webdriver
import unittest

from Saas_merchant.config import address_ip
from Saas_merchant.config.random_str import random_str
from Saas_merchant.sreenshots.get_windows_img import get_windows_img


class indexShop(unittest.TestCase):
    """主页我的店铺测试用例"""
    def setUp(self):
        # 隐藏浏览器
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=option)

        # self.driver = webdriver.Chrome()  #显示浏览器
        self.url = address_ip.index()
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
        self.driver.find_element_by_xpath("/html/body/div/section/section/section/aside/div/ul/li[2]/div").click()
        self.driver.find_element_by_link_text("我的店铺").click()


    def test_02(self):
        """验证cookies正确添加"""
        title = self.driver.title
        try:
            self.assertEqual("商家中心-商家中心",title)
            get_windows_img(self.driver)
        except Exception as e:
            print("添加cookie失败%s" % e)

    def test_03(self):
        driver = self.driver
        driver.find_element_by_class_name("ant-btn-lg").click()
        sleep(2)


    def test_04(self):
        """店铺管理-我的店铺"""
        print(self._testMethodName)
        driver = self.driver
        text = driver.find_elements_by_class_name("text-muted")[1].text
        try:
            self.assertEqual("联系人",text)
            get_windows_img(driver)
        except Exception as e:
            print("验证失败%s" % e)

    def test_05(self):
        """店铺管理-公司信息修改"""
        driver = self.driver

        # 点击公司信息
        driver.find_elements_by_class_name("ant-tabs-tab")[1].click()
        driver.find_element_by_class_name("ant-btn-block").click()
        # driver.find_element_by_id("businessScope").click()
        # 公司名称填写
        driver.find_element_by_id("companyName").clear()
        driver.find_element_by_id("companyName").send_keys("大大大大大公司")
        # 信用代码填写
        driver.find_element_by_id("creditNum").send_keys("123456789123456789")
        # 公司法人填写
        driver.find_element_by_id("legalName").send_keys("马化腾")
        driver.find_element_by_id("instroduction").send_keys("小小的公司 -- ")
        sleep(4)
        try:
            driver.find_elements_by_class_name("ant-btn-block")[0].click()
            get_windows_img(driver)
        except Exception as e:
            print("定位错误%s" % e)
            get_windows_img(driver)
            # """# 添加装饰器失败 #"""

    def test_06(self):
        """店铺管理-对公账号"""
        driver = self.driver
        driver.find_elements_by_class_name("ant-tabs-tab")[2].click()
        driver.find_element_by_id("accountName").send_keys("吴江开户行")
        driver.find_element_by_id("accountBlank").send_keys("123456789101112131")
        # 点击上传图片按钮
        driver.find_element_by_class_name("avatar-uploader-trigger").click()
        # 调用上传图片文件
        os.system(r"G:\dk测试工具\pycharm\猪猪建材PC\Saas_merchant\config\upfile.exe")
        sleep(5)
        # 点击保存
        driver.find_elements_by_class_name("ant-btn-primary")[1].click()
        get_windows_img(driver)
        sleep(5)

        get_windows_img(driver)
        print("test_04")

    def test_07(self):
        """店铺管理-店铺图集"""
        driver = self.driver
        driver.find_elements_by_class_name("ant-tabs-tab")[3].click()
        # 点击上传按钮
        sleep(2)
        driver.find_element_by_class_name("ant-upload-text").click()
        # 调用上传图片文件
        sleep(3)
        os.system(r"G:\dk测试工具\pycharm\猪猪建材PC\Saas_merchant\config\upfile.exe")
        sleep(4)
        # 点击上传按钮
        driver.find_element_by_class_name("ant-upload-text").click()
        # 调用上传图片文件
        os.system(r"G:\dk测试工具\pycharm\猪猪建材PC\Saas_merchant\config\upfile.exe")

        sleep(3)
        get_windows_img(driver)
        print("test_07")



        pass
    #
    def test_08(self):
        """店铺管理-店铺公告"""
        driver = self.driver
        # 点击店铺公告
        # driver.find_element_by_class_name("ant-tabs-tab-active").click()
        driver.find_element_by_xpath("/html/body/div[1]/section/section/section/main/div/div/div[1]/div/div/div/div/div[1]/div[5]").click()
        sleep(2)
        text1 = driver.find_elements_by_class_name("ant-btn-primary")[1].text
        # 验证是否发布成功  获取输入框的值
        print(text1)
        if text1 == "修 改":
            get_windows_img(driver)
            print("已有内容不可修改")
        # 店铺公告输入数据
        else:
            driver.find_element_by_id("shopNotices").send_keys("这是我的店铺公告，一天只准修改一次")
            # 点击发布按钮
            sleep(3)
            driver.find_elements_by_class_name("ant-btn-primary")[1].click()
            sleep(3)

    def tearDown(self):
        self.driver.quit()