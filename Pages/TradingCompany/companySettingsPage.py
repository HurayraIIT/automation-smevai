import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import LINKS


class CompanySettingsPage:
    URL = LINKS.COMPANY_SETTINGS_PAGE

    heading_xpath = (By.XPATH, f"//h3[normalize-space()='Company Settings']")
    heading_text = f"Company Settings"

    factory_reset_button_xpath = (By.XPATH, f"//button[@data-test='factory-reset']")
    factory_reset_title = f"Factory reset confirmation needed."
    factory_reset_title_xpath = (By.XPATH, "//h4[@class='mb20 text-center']")

    vat_applicable_checkbox_xpath = (By.XPATH, f"//div[@class='form__group']//span[@class='label__text'][normalize-space()='VAT Applicable']")
    password_input_xpath = (By.XPATH, f"//input[@data-test='password']")
    confirm_button_xpath = (By.XPATH, f"//button[@data-test='confirm']")
    cancel_button_xpath = (By.XPATH, f"//button[@data-test='cancel']")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

    def perform_factory_reset(self):
        self.browser.find_element(*self.factory_reset_button_xpath).click()
        print(self.browser.find_element(*self.factory_reset_title_xpath).text)
        print(self.factory_reset_title)
        # assert self.browser.find_element(*self.factory_reset_title_xpath).text == self.factory_reset_title_text

        time.sleep(1.5)
        self.browser.find_element(*self.vat_applicable_checkbox_xpath).click()
        self.browser.find_element(*self.password_input_xpath).send_keys(LINKS.PASSWORD)
        self.browser.find_element(*self.confirm_button_xpath).click()
        time.sleep(1.5)

        assert ("/settings/company" in self.browser.current_url) == True
