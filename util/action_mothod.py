# coding=utf-8
from base.base_driver import BaseDriver
from get_by_local import GetByLocal
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ActionMothod:
    def __init__(self, i):
        base_driver = BaseDriver()
        self.driver = base_driver.get_driver(i)
        self.get_by_local = GetByLocal(self.driver)

    def input(self, *args):
        '''
        封装输入操作
        '''
        print "start input..."
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return element, u"元素没有找到"
        element.send_keys(args[1])

    def on_click(self, *args):
        '''
        封装点击操作
        '''
        print 'start click ...'
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return element, u"元素没有找到"
        element.click()

    def sleep_time(self, *args):
        '''
        封装sleep操心
        '''
        time.sleep(args[0])

    # 获取屏幕的宽高
    def get_size(self, *args):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左边滑动
    def swipe_left(self, *args):
        # [100,200]
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1, 2000)

    # 向右边滑动
    def swipe_right(self, *args):
        # [100,200]
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x, y1, 2000)

    # 向上滑动
    def swipe_up(self, *args):
        # [100,200]direction
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 6
        y = self.get_size()[1] / 10 * 2
        self.driver.swipe(x1, y1, x1, y, 1000)

    # 向下滑动
    def swipe_down(self, *args):
        # [100,200]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y)

    def get_element(self, *args):
        element = self.get_by_local.get_element(args[0])
        if element == None:
            print u"元素未找到"
            return None
        return element

    def get_tost_element(self, *args):
        '''
        获取tostelement
        '''
        time.sleep(2)
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % args[0])
            toast_element=WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_loc))
            return toast_element
        except:
            self.driver.save_screenshot('../jpg/test.jpg')
            return None


if __name__ == "__main__":
    am = ActionMothod(0)
    # am.on_click('forget_password')
    time.sleep(2)
    # am.on_click('over_login')
    am.on_click('login_button')
    result =am.get_tost_element('请输入6-8位密码')
    if result:
        print "------------------pass--------------------"
    else:
        print "------------------fail--------------------"

