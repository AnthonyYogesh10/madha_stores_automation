import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def get_menu_bar_btn(self):
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("menu")')

    def get_home_btn_field(self):
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("apps outline")')

    def get_offer_btn_field(self):
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("pricetags outline")')

    def get_account_btn_field(self):
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Account")')

    def get_view_cart_btn(self):
        return self.driver.find_element(AppiumBy.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")

    def get_cart_btn_field(self):
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("cart outline")')

    def get_product_name(self):
        return self.driver.find_elements(AppiumBy.XPATH,
                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.TextView[1]")

    def click_home_btn(self):
        self.get_home_btn_field().click()

    def click_offer_btn(self):
        self.get_offer_btn_field().click()

    def click_view_cart_btn(self):
        view_cart_btn = self.get_view_cart_btn()
        view_cart_btn.click()
    def click_account_btn(self):
        self.get_account_btn_field().click()
        time.sleep(5)

    def click_cart_btn(self):
        self.get_cart_btn_field().click()

    def retrieve_index_0f_product(self, cart_product):
        product_name = self.get_product_name()
        index = 0  # To retrieve the index of product to access specific add btn because add btn have common element
        # and same index.//android.view.View/android.view.View/android.widget.TextView
        for product in product_name:
            if product.text == cart_product:
                index = product_name.index(product)
                # print("index value is : ", index)

        return index

    def select_product_catg(self, category_name):
        # product_category = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("' + category_name + '")')
        product_category = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                    'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollForward().scrollIntoView(new UiSelector().text("' + category_name + '"))')
        time.sleep(3)
        product_category.click()
        time.sleep(3)

    def select_product(self, product_name):
        product = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                                         '.scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("' + product_name + '").instance(0))')
        time.sleep(3)
        index = self.retrieve_index_0f_product(product_name)
        print(index)
        add_btn = self.driver.find_elements(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]")
        add_btn[index].click()

    def click_back_btn(self):
        self.driver.back()