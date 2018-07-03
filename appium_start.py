# coding=utf-8
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.get_by_local import GetByLocal

def get_driver():
    # 封装driver
    desired_capabilities = {
        "platformName": "android",
        "deviceName": "8593d3b4",
        "automationName": "UiAutomator2",
        "app": "C:\\Users\\liuyj\\Desktop\\app-localtest-release.apk",
        # "deviceName": "5EF0217C09001391",
        # "app": "C:\\Users\\liuyj\\Desktop\\Ctrip.apk",
        "appWaitActivity": "hospital.com.mainlib.login.LoginActivity",
        # "appWaitActivity": "ctrip.android.publicproduct.home.view.CtripHomeActivity",
        "noReset": "True",
        "unicodeKeyboard": "True",
        "resetKeyboard": "True"
    }

    driver = webdriver.Remote("http://127.0.0.1:4700/wd/hub", desired_capabilities)
    time.sleep(10)
    return driver


# 获取屏幕的宽高
def get_size(driver):
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width, height


# 向左边滑动
def swipe_left(driver):
    # [100,200]
    x1 = get_size(driver)[0] / 10 * 9
    y1 = get_size(driver)[1] / 2
    x = get_size(driver)[0] / 10
    driver.swipe(x1, y1, x, y1, 2000)


# 向右边滑动
def swipe_right(driver):
    # [100,200]
    x1 = get_size(driver)[0] / 10
    y1 = get_size(driver)[1] / 2
    x = get_size(driver)[0] / 10 * 9
    driver.swipe(x1, y1, x, y1, 2000)


# 向上滑动
def swipe_up(driver):
    # [100,200]direction
    x1 = get_size(driver)[0] / 2
    y1 = get_size(driver)[1] / 10 * 6
    y = get_size(driver)[1] / 10 * 2
    driver.swipe(x1, y1, x1, y, 1000)


# 向下滑动
def swipe_down(driver):
    # [100,200]
    x1 = get_size(driver)[0] / 2
    y1 = get_size(driver)[1] / 10
    y = get_size(driver)[1] / 10 * 9
    driver.swipe(x1, y1, x1, y)


# 根据传入的direction参数，滑动屏幕
def swipe_on(driver, direction):
    if direction == "up":
        swipe_up(driver)
    elif direction == "down":
        swipe_down(driver)
    elif direction == "left":
        swipe_left(driver)
    else:
        swipe_right(driver)


def login_by_id(driver):
    # id定位实现登录
    driver.find_element_by_id('com.hospital.localtest:id/mLoginName').send_keys('dasheng13')
    driver.find_element_by_id('com.hospital.localtest:id/mPassword').send_keys('123456')
    driver.find_element_by_id('com.hospital.localtest:id/mLogin').click()
    time.sleep(10)
    driver.find_element_by_id('com.hospital.localtest:id/btn_ychz').click()


def login_by_node(driver):
    # class_name定位
    element = driver.find_element_by_id('android:id/content')
    element1 = element.find_element_by_class_name('android.view.ViewGroup')
    element2 = element1.find_element_by_class_name('android.widget.LinearLayout')
    print element2.find_element_by_class_name('android.widget.TextView').text


def login_by_xpath(driver):
    # xpath定位
    driver.find_element_by_xpath('//*[contains(@text,"dasheng")]').clear()
    time.sleep(2)
    driver.find_element_by_xpath('//android.widget.EditText[@text="请输入登录用户名"]').send_keys('dasheng13')


def login_by_list(driver):
    # list定位
    elements = driver.find_elements_by_class_name('android.widget.EditText')
    for i in elements:
        i.click()
        time.sleep(3)
    elements[0].send_keys('dasheng13')
    elements[1].send_keys('123456')


def login_by_uiautomator(driver):
    # uiautomator定位
    driver.find_element_by_android_uiautomator('new UiSelector().text("dasheng13")').clear()
    driver.find_element_by_android_uiautomator('new UiSelector().text("请输入登录用户名")').send_keys('dasheng13')
    driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.hospital.localtest:id/mPassword")').send_keys('123456')


def get_web_view():
    # 定位H5
    time.sleep(10)
    webview = driver.contexts
    for viw in webview:
        if 'WEBVIEW_cn.com.open.mooc' in viw:
            driver.switch_to.context(viw)
            break
    driver.find_element_by_link_text('C').click()
    try:
        driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
    except Exception as e:

        driver.switch_to.context(webview[0])
        driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
        raise e
    print webview


def get_tost():
    #获取toast元素
    time.sleep(2)
    driver.find_element_by_id('com.hospital.localtest:id/mLoginName').clear()
    # driver.find_element_by_id('com.hospital.localtest:id/mPassword').send_keys('111111')
    driver.find_element_by_id('com.hospital.localtest:id/mLogin').click()
    tost_element = ("xpath", "//*[@text='请输入6-16位用户名!']")
    WebDriverWait(driver, 20, 0.01).until(EC.presence_of_element_located(tost_element))


if __name__ == "__main__":
    driver = get_driver()
    # print get_tost()
    getbylocal=GetByLocal(driver)
    print getbylocal.get_element('username')
