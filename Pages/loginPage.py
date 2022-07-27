import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import LINKS


class LoginPage:
    URL = LINKS.SITE
    heading_xpath = (By.XPATH, f"//h2[@class='access__form__title']")
    heading_text = f"Login"
    username_xpath = (By.XPATH, f"//input[@data-test='username']")
    password_xpath = (By.XPATH, f"//input[@data-test='password']")
    submit_xpath = (By.XPATH, f"//button[@data-test='submit']")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

    def login(self, username, password):
        self.browser.find_element(*self.username_xpath).send_keys(username)
        self.browser.find_element(*self.password_xpath).send_keys(password)
        self.browser.find_element(*self.submit_xpath).click()
        time.sleep(2)
        assert ("dashboard" in self.browser.current_url) == True
