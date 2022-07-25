from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.registration_page_title_text_name = f""

    def load(self):
        self.browser.get("https://app.smevai.com/register")

    def click_register(self):
        pass
