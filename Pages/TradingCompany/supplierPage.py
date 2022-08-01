import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from config import LINKS


class SupplierPage:
    LIST_URL = LINKS.SUPPLIER_LIST_PAGE
    CREATE_URL = LINKS.SUPPLIER_CREATE_PAGE

    create_heading_xpath = (By.XPATH, f"//h2[@class='access__form__title']")
    create_heading_text = f"Create Supplier"

    list_heading_xpath = (By.XPATH, f"//h2[@class='access__form__title']")
    list_heading_text = f"Supplier List"

    supplier_name_xpath = (By.XPATH, f"//input[@name='name']")
    supplier_phone_xpath = (By.XPATH, f"//input[@name='phone']")

    supplier_country_code_xpath = (By.XPATH, f'//*[@id="phoneNumCountryCode"]/div[1]/div/div/span')
    supplier_country_code_input_xpath = (By.XPATH, f'//*[@id="phoneNumCountryCode"]/span/span/span[1]/input')
    supplier_country_code_result_xpath = (By.XPATH, f'//*[@id="select2-phoneCountryCode-results"]/li[1]')

    save_btn_xpath = (By.XPATH, f"//button[@class='button button__themeColor']")
    cancel_btn_xpath = (By.XPATH, f"//a[@class='button']")

    def __init__(self, browser):
        self.browser = browser

    def load_create_page(self):
        self.browser.get(self.CREATE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.create_heading_xpath).text == self.create_heading_text

    def load_list_page(self):
        self.browser.get(self.LIST_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.list_heading_xpath).text == self.list_heading_text

    def create_supplier(self, supplier_name="supplier001", supplier_phone="01657887766"):

        self.browser.find_element(*self.supplier_name_xpath).send_keys(supplier_name)
        self.browser.find_element(*self.supplier_phone_xpath).send_keys(supplier_phone)

        element = self.browser.find_element(*self.supplier_country_code_xpath)
        element.click()
        self.browser.find_element(*self.supplier_country_code_input_xpath).send_keys('+88')
        time.sleep(2)
        self.browser.find_element(*self.supplier_country_code_result_xpath).click()
        # select = Select(element)
        # select.select_by_visible_text("+88")
        time.sleep(1)

        self.browser.find_element(*self.save_btn_xpath).click()
        time.sleep(2)
        assert self.browser.current_url == self.LIST_URL
