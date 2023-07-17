import re
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def get_all_products(self):
        return self.driver.find_elements(AppiumBy.XPATH,
                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.ListView[1]/android.view.View")

    def get_product_name(self):
        return self.driver.find_elements(AppiumBy.XPATH,
                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.ListView[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.TextView[1]")

    def get_price_of_all_product(self):
        return self.driver.find_elements(AppiumBy.XPATH,
                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.ListView[1]/android.view.View/android.view.View/android.view.View/android.widget.TextView")

    def retrieve_index_0f_product(self, cart_product):
        product_name = self.get_product_name()
        index = 0  # To retrieve the index of product to access specific add btn because add btn have common element
        # and same index.//android.view.View/android.view.View/android.widget.TextView
        for product in product_name:
            if product.text == cart_product:
                index = product_name.index(product)
                print("index value is : ", index)

        return index

    def get_add_btn(self, index):
        products = self.get_all_products()
        add_btn = products[index].find_element(AppiumBy.XPATH,
                                               ".//android.view.View/android.view.View/android.view.View/android.widget.Image[2]")
        # Here we get all prod then
        # find index of element, and then we click the add btn
        return add_btn
        # inner_elements = products[index].find_elements(AppiumBy.XPATH,".//android.view.View/android.view.View/android.view.View/android.widget.TextView")

    def get_sub_btn(self, index):
        products = self.get_all_products()
        sub_btn = products[index].find_element(AppiumBy.XPATH,
                                               ".//android.view.View/android.view.View/android.view.View/android.widget.Image[1]")

        return sub_btn

    def get_grand_total(self):
        grand_total = self.driver.find_element(AppiumBy.XPATH,
                                               "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.TextView[1]")
        return grand_total

    def click_add_btn(self, product_name):
        index_value = self.retrieve_index_0f_product(product_name)
        for i in range(5):
            self.get_add_btn(index_value).click()
        # print("index_value", index_value)

    def click_sub_btn(self, product_name):
        index_value = self.retrieve_index_0f_product(product_name)
        for i in range(5):
            self.get_sub_btn(index_value).click()

    def specific_product_datas(self, product_name):
        product_detail = []
        index_value = self.retrieve_index_0f_product(product_name)
        product_list = self.get_all_products()
        product_datas = product_list[index_value].find_elements(AppiumBy.XPATH,
                                                                ".//android.view.View/android.view.View/android.widget.TextView")
        for product in product_datas:
            product_detail.append(product.text)

        return product_detail

    def check_add_btn(self, product_name):

        self.click_add_btn(product_name)
        time.sleep(2)
        product = self.specific_product_datas(product_name)
        product_name = product[0]

        prices = product[1]
        split_prices = re.split(r"\s\xa0\s", prices)  # split the whitespace and xa0
        mrp_price = split_prices[0]  # ₹180
        product_mrp_price = int(''.join(filter(str.isdigit, mrp_price)))

        product_off_price = 0
        if len(split_prices) > 1 and split_prices[1] != '':
            off_price = split_prices[1]  # ₹150  now to remove ₹ and conv into int
            product_off_price = int(''.join(filter(str.isdigit, off_price)))
        else:
            product_off_price = 10000000

        product_price = 0
        if product_mrp_price > product_off_price:
            product_price = product_off_price
        else:
            product_price = product_mrp_price

        product_quantity = int(product[2])

        total = product[3]
        conv_total = ''.join(filter(str.isdigit, total))
        product_total = int(conv_total) // 100

        print("name of the product : ", product_name)
        print("price : ₹", product_price)
        print("quantity :", product_quantity)
        print("expected total price of product : ₹", product_quantity * product_price)
        print("actual total price of product :₹", product_total)
        if (product_quantity * product_price) == product_total:
            print("total value was correct when click + btn")

        else:
            print("the + button not working properly")

    def check_sub_btn(self, product_name):
        self.click_sub_btn(product_name)
        time.sleep(2)
        product = self.specific_product_datas(product_name)

        prices = product[1]
        split_prices = re.split(r"\s\xa0\s", prices)  # split the whitespace and xa0
        mrp_price = split_prices[0]  # ₹180
        product_mrp_price = int(''.join(filter(str.isdigit, mrp_price)))

        product_off_price = 0
        if len(split_prices) > 1 and split_prices[1] != '':
            off_price = split_prices[1]  # ₹150  now to remove ₹ and conv into int
            product_off_price = int(''.join(filter(str.isdigit, off_price)))
        else:
            product_off_price = 1000000

        product_price = 0
        if product_mrp_price > product_off_price:
            product_price = product_off_price
        else:
            product_price = product_mrp_price

        product_quantity = int(product[2])

        total = product[3]
        conv_total = ''.join(filter(str.isdigit, total))
        product_total = int(conv_total) // 100

        print("expected total price of product : ₹", product_quantity * product_price)
        print("actual total price of product :₹", product_total)
        if (product_quantity * product_price) == product_total:
            print("total value was correct when click - btn")

        else:
            print("the - button not working properly")

    def check_sum_of_grand_total(self):
        str_list = []
        int_list = []
        remove_symbol = []
        all_total = self.get_price_of_all_product()

        for t in all_total:
            str_list.append(t.text)

        for string in str_list:
            remove_sym = ''.join(filter(lambda x: x != " " and x.isdigit(), string))
            remove_symbol.append(remove_sym)

        time.sleep(2)

        for remove in remove_symbol:
            int_val = int(remove) // 100
            int_list.append(int_val)
        # print(remove_symbol)
        expected_grand_total = sum(int_list)
        grand_total = self.get_grand_total().text
        conv_total_wo_symbols = ''.join(filter(str.isdigit, grand_total))
        actual_grand_total = int(conv_total_wo_symbols) // 100

        print("expected_grand_total : ₹", expected_grand_total)
        print("actual_grand_total : ₹", actual_grand_total)

        if expected_grand_total == actual_grand_total:
            print("grand total works good")
        else:
            print("sum of grand total is failed")
