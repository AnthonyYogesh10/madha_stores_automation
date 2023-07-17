import time

import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage


@pytest.mark.usefixtures('setup')
class Test_cart_checkout:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(self.driver)
        self.cp = CartPage(self.driver)

    def test_add_product_01(self):
        self.hp.select_product_catg("Talcum Powder")
        self.hp.select_product("நைசில்")
        time.sleep(5)
        # self.hp.click_view_cart_btn()
        self.hp.click_back_btn()
        time.sleep(5)

    def test_checkout_02(self):
        self.hp.click_cart_btn()
        time.sleep(3)
        self.cp.check_add_btn("நைசில் 150g")
        time.sleep(5)
        self.cp.check_sub_btn("நைசில் 150g")
        self.cp.check_sum_of_grand_total()
        time.sleep(5)
