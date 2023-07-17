import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


class MsgPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def start_msg_app(self):
        self.driver.start_activity('com.android.mms', '.ui.MmsTabActivity')
        # driver.start_activity is used to switch to another app
        time.sleep(6)

    def get_all_received_msg_contacts_fields(self):
        return self.driver.find_elements(AppiumBy.ID, "com.android.mms:id/from")

    def get_otp_msg_list_field(self):
        return self.driver.find_elements(AppiumBy.ID, "com.android.mms:id/msg_list_item")

    def get_message_text_field(self):
        return self.driver.find_element(AppiumBy.ID, "com.android.mms:id/message_body")

    def select_received_msg_contact(self):
        all_received_msg_contacts = self.get_all_received_msg_contacts_fields()
        all_received_msg_contacts[0].click()
        time.sleep(5)

    def click_otp_msg_list(self):
        otp_message_list = self.get_otp_msg_list_field()
        time.sleep(5)
        otp_message_list[2].click()
        time.sleep(4)

    def verification_code(self):
        message_text = self.get_message_text_field().text
        verification_code = ''.join(filter(str.isdigit, message_text))
        print(verification_code)
        return verification_code
