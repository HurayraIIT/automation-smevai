from assertpy import soft_assertions, assert_that
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from utils.credentials import *
from utils.config import *


class Login:
    email = (By.NAME, f'username')
    password = (By.NAME, f'password')
    button = (By.XPATH, f'/html/body/div/div[1]/div[2]/form/button')
    dashboard = (By.XPATH, f'/html/body/div/div[2]/div[2]/div[1]/h2')
    dashboard_text = "Dashboard"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(BASE_URL)

    def testcase(self):
        with soft_assertions():
            self.browser.find_element(*self.email).send_keys(email)
            self.browser.find_element(*self.password).send_keys(password)
            self.browser.find_element(*self.button).click()

            assert_that(self.browser.find_element(*self.dashboard).text).is_equal_to(self.dashboard_text)
            




