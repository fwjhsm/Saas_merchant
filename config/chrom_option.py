from selenium import webdriver


class option_Chrom():
    def option(self):
        # 隐藏浏览器
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=option)
        return self.driver
