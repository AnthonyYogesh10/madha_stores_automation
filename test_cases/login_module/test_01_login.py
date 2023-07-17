import time

import pytest

from pages.home_page import HomePage
from pages.msg_app_page import MsgPage
from pages.sigin_page import SigninPage
from utilities.switch_back_madha_store import switching


@pytest.mark.usefixtures("setup")
class Test_login:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(self.driver)
        self.sp = SigninPage(self.driver)
        self.msg = MsgPage(self.driver)
        self.switch_to = switching(self.driver)

    def test_signup_and_login(self):
        self.hp.click_account_btn()
        self.sp.enter_ph_number("9597705096")
        self.sp.click_signin_btn()

        # Switched to message app
        self.msg.start_msg_app()
        self.msg.select_received_msg_contact()
        self.msg.click_otp_msg_list()
        verification_code = self.msg.verification_code()
        time.sleep(4)

        # Switch to again madha_store
        self.switch_to.switch_to_madha_store()

        # verify_code_input
        self.sp.enter_otp(verification_code)
        self.sp.click_verify_btn()
