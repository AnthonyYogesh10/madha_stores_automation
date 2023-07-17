import time


class switching:
    def __init__(self, driver):
        self.driver = driver

    def switch_to_madha_store(self):
        self.driver.activate_app('com.madhastore.pushnotificaiton')
        time.sleep(7)
