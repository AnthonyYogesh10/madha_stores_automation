import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


class SigninPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def get_ph_number(self):
        return self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")

    def get_signin_btn(self):
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("SIGN IN")')

    def get_otp_input_field(self):
        return self.driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.EditText')

    def get_verify_btn_field(self):
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("VERIFY OTP")')

    def enter_ph_number(self, ph_number):
        self.get_ph_number().send_keys(ph_number)
        time.sleep(2)

    def click_signin_btn(self):
        self.get_signin_btn().click()
        time.sleep(10)

    def enter_otp(self, verification_code):
        self.get_otp_input_field().send_keys(verification_code)
        time.sleep(3)

    def click_verify_btn(self):
        self.get_verify_btn_field().click()
        time.sleep(7)
