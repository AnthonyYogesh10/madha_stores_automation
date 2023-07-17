import time

import pytest

from pages.home_page import HomePage


@pytest.mark.usefixtures('setup')
class Test_add_cart:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(self.driver)

    def test_add_product(self):
        self.hp.select_product_catg("Talcum Powder")
        self.hp.select_product("யார்லி ஜாஸ்மின்")
