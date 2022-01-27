from assertpy import soft_assertions, assert_that
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utils.config import *


class Accounts:
    profile_menu = (By.XPATH, f'/html/body/div[1]/div[2]/div[1]/div')
    my_account = (By.XPATH, f'/html/body/div[1]/div[2]/div[1]/div/div/ul/li[1]/a')
    password_settings = (By.XPATH, f'//*[@id="nav-company-tab"]')
    current_pass = (By.NAME, f'current_password')
    new_pass = (By.NAME, f'password')
    con_pass = (By.NAME, f'password_confirmation')
    pass_update_btn = (By.XPATH, f'//*[@id="nav-company"]/form/div[2]/button')

    success_message = (By.XPATH, f'/html/body/div[2]/div/div[2]/div/span')
    success_message_text = "Password updated successfully."

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get()

    def testcase(self):
        with soft_assertions():
            self.browser.find_element(*self.profile_menu).click()
            self.browser.find_element(*self.my_account).click()
            self.browser.find_element(*self.password_settings).click()

            self.browser.find_element(*self.current_pass).clear()
            self.browser.find_element(*self.current_pass).send_keys('pass1234')
            self.browser.find_element(*self.new_pass).clear()
            self.browser.find_element(*self.new_pass).send_keys('pass1234')
            self.browser.find_element(*self.con_pass).clear()
            self.browser.find_element(*self.con_pass).send_keys('pass1234')
            self.browser.find_element(*self.pass_update_btn).click()

            assert_that(self.browser.find_element(*self.success_message).text).\
                is_equal_to(self.success_message_text)
