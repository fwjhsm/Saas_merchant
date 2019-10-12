import os
import time
from selenium import webdriver

def get_windows_img(driver):
    """
    把file_path保存到我们项目根目录的一个文件夹.\Screenshots下
    """

    file_path = os.getcwd() + "\\sreenshots\\"
    rq = time.strftime('%Y-%m-%d %H_%M_%S')
    screen_name = file_path + rq + '.png'
    return driver.get_screenshot_as_file(screen_name)


def get_images(func):

    def sreenshot_error(webdriver,*args,**kwargs):
        file_path = os.getcwd() + "\\sreenshots\\"
        rq = time.strftime('%Y-%m-%d %H_%M_%S')
        screen_name = file_path + rq + '.png'
        try:
            func(webdriver,*args,**kwargs)
            webdriver.get_screenshot_as_file(screen_name)
        except Exception as e:
            print("定位错误 %s" % e)

        return sreenshot_error

