#coding=utf-8
from appium import webdriver
from util.opera_yaml import OperaYaml
import time

class BaseDriver:

    def get_driver(self,i):
        config_file = OperaYaml()
        devices=config_file.get_value('user_info_'+str(i),'deviceName')
        port = config_file.get_value('user_info_'+str(i),'port')
        print type(port)
        # 封装driver
        desired_capabilities = {
            "platformName": "android",
            "deviceName":devices,
            "automationName": "UiAutomator2",
            "app": "C:\\Users\\liuyj\\Desktop\\app-localtest-release.apk",
            "appWaitActivity": "hospital.com.mainlib.login.LoginActivity",
            "noReset": "True",
            "unicodeKeyboard": "True",
            "resetKeyboard": "True"
        }
        print 'start create driver...'
        driver = webdriver.Remote("http://127.0.0.1:"+str(port)+"/wd/hub", desired_capabilities)
        time.sleep(10)
        return driver

if __name__=="__main__":
    bd=BaseDriver()
    driver=bd.get_driver(0)
