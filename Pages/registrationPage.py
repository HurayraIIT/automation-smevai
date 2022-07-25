from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import DATA


class RegistrationPage:
    registration_page_title_text_name = f""
    URL = DATA.REGISTER_PAGE

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def click_register(self):
        pass
