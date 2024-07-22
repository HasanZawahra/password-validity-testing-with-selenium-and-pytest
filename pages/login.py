from selenium.webdriver.common.by import By
from .common import Common

class login(Common):

    locators = {
        "PASSWORD" : (By.ID, 'password'),
        "BUTTON" : (By.TAG_NAME, 'button'),
        "MESSAGE" : (By.ID, 'message')
    }

    def enter_password(self, password):
        self.wait_for(self.locators["PASSWORD"]).send_keys(password)

    def click_button(self):
        self.find(self.locators["BUTTON"]).click()

    def text_message(self):
        return self.find(self.locators["MESSAGE"]).text

    def clear_password(self):
        self.wait_for(self.locators["PASSWORD"]).clear()