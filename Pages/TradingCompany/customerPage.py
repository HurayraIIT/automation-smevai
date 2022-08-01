import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import LINKS


class CustomerPage:
    LIST_URL = LINKS.CUSTOMER_LIST_PAGE
    CREATE_URL = LINKS.CUSTOMER_CREATE_PAGE

    create_heading_xpath = (By.XPATH, f"//h2[@class='access__form__title']")
    create_heading_text = f"Create Customer"

    list_heading_xpath = (By.XPATH, f"//h2[@class='access__form__title']")
    list_heading_text = f"Customer List"

    customer_name_xpath = (By.XPATH, f"//input[@name='name']")
    customer_phone_xpath = (By.XPATH, f"//input[@name='phone']")

    customer_country_code_xpath = (By.XPATH, f'//*[@id="phoneNumCountryCode"]/div[1]/div/div/span')
    customer_country_code_input_xpath = (By.XPATH, f'//*[@id="phoneNumCountryCode"]/span/span/span[1]/input')
    customer_country_code_result_xpath = (By.XPATH, f'//*[@id="select2-phoneCountryCode-results"]/li[1]')

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

    def create_customer(self, customer_name="customer001", customer_phone="01657887766"):

        self.browser.find_element(*self.customer_name_xpath).send_keys(customer_name)
        self.browser.find_element(*self.customer_phone_xpath).send_keys(customer_phone)

        element = self.browser.find_element(*self.customer_country_code_xpath)
        element.click()
        self.browser.find_element(*self.customer_country_code_input_xpath).send_keys('+88')
        time.sleep(2)
        self.browser.find_element(*self.customer_country_code_result_xpath).click()
        # select = Select(element)
        # select.select_by_visible_text("+88")
        time.sleep(1)

        self.browser.find_element(*self.save_btn_xpath).click()
        time.sleep(2)
        assert self.browser.current_url == self.LIST_URL
