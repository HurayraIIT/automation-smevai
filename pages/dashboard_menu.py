from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utils.config import *


class DashboardMenu:
    product = (By.XPATH, f'//*[@id="nav_accordion"]/li[2]/a/span[2]')
    product_attribute = (By.XPATH, f'//*[@id="product"]/li[1]/a')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get()

    def click_product_attribute(self):
        self.browser.find_element(*self.product).click()
        self.browser.find_element(*self.product_attribute).click()
