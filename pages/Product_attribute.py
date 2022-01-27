import time

from assertpy import soft_assertions, assert_that
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.dashboard_menu import DashboardMenu
from utils.config import *


class ProductAttribute:
    add = (By.XPATH, f'/html/body/div/div[2]/div[2]/div[1]/div/a[2]')
    at_name = (By.NAME, f'attribute_name')
    at_value_1 = (By.XPATH, f'//*[@id="attributeFormId"]/div[2]/div/div/div/div/input')

    add_at_value_2 = (By.XPATH, f'//*[@id="attributeFormId"]/div[2]/div/div/div/a')
    at_value_2 = (By.XPATH, f'//*[@id="attributeFormId"]/div[4]/div[2]/div/div/div/div/input')

    add_at_value_3 = (By.XPATH, f'//*[@id="attributeFormId"]/div[4]/div[2]/div/div/div/a[1]')
    at_value_3 = (By.XPATH, f'//*[@id="attributeFormId"]/div[4]/div[3]/div/div/div/div/input')

    add_at_value_4 = (By.XPATH, f'//*[@id="attributeFormId"]/div[4]/div[3]/div/div/div/a[1]')

    save_btn = (By.XPATH, f'//*[@id="attributeFormId"]/div[5]/button')
    cancel_btn = (By.XPATH, f'//*[@id="attributeFormId"]/div[5]/a')

    # Deletion
    action = (By.XPATH, f'//*[@id="attributeTableId"]/tbody/tr/td[4]/div/a')
    delete = (By.XPATH, f'//*[@id="attributeTableId"]/tbody/tr/td[4]/div/ul/li[2]/a')
    con_delete = (By.XPATH, f'//*[@id="deleteModal"]/div/div/div/div/a[2]')
    delete_success_message = (By.XPATH, f'/html/body/div[2]/div/div[2]/div/span')
    delete_success_message_text = "Attribute deleted successfully."

    def __init__(self, browser):
        self.browser = browser

    # def load(self):
    #     self.browser.get()

    def add_attribute(self):
        with soft_assertions():
            menu = DashboardMenu(self.browser)

            menu.click_product_attribute()

            self.browser.find_element(*self.add).click()
            self.browser.find_element(*self.at_name).send_keys("Smart Phones")
            self.browser.find_element(*self.at_value_1).send_keys("Apple")
            self.browser.find_element(*self.add_at_value_2).click()
            self.browser.find_element(*self.at_value_2).send_keys("Samsung")
            self.browser.find_element(*self.add_at_value_3).click()
            self.browser.find_element(*self.at_value_3).send_keys("Sony")

            self.browser.find_element(*self.save_btn).click()

    def delete_attribute(self):
        self.browser.find_element(*self.action).click()
        self.browser.find_element(*self.delete).click()
        self.browser.find_element(*self.con_delete).click()

        time.sleep(1)
        assert_that(self.browser.find_element(*self.delete_success_message).text).\
            is_equal_to(self.delete_success_message_text)