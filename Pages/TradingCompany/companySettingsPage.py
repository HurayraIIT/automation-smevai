import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import DATA


class CompanySettingsPage:
    URL = DATA.COMPANY_SETTINGS_PAGE

    company_settings_page_heading_text_xpath = (By.XPATH, f"//h3[normalize-space()='Company Settings']")
    company_settings_page_heading_text = f"Company Settings"

    factory_reset_title_text = f"Factory reset confirmation needed."
    factory_reset_title_xpath = (By.XPATH, f'//*[@id="factoryResetModal"]/div/div/div/h4')

    factory_reset_button_xpath = (By.XPATH, f"//button[@class='button button__danger button--xs factoryResetBtn']")
    vat_applicable_checkbox_name = (By.NAME, f"vat_applicable")
    password_input_name = (By.NAME, f"factoryResetPassword")
    confirm_button_xpath = (By.XPATH, f'//*[@id="factoryResetModal"]/div/div/div/div/button[2]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)
        assert self.browser.find_element(*self.company_settings_page_heading_text_xpath).text == self.company_settings_page_heading_text

    def perform_factory_reset(self):
        self.browser.find_element(*self.factory_reset_button_xpath).click()
        print(self.browser.find_element(*self.factory_reset_title_xpath).text)
        print(self.factory_reset_title_text)
        # assert self.browser.find_element(*self.factory_reset_title_xpath).text == self.factory_reset_title_text

        # self.browser.find_element(*self.vat_applicable_checkbox_name).click()
        # self.browser.find_element(*self.password_input_name).send_keys(DATA.PASSWORD)
        # self.browser.find_element(*self.confirm_button_xpath).click()
        #
        # assert ("/settings/company" in self.browser.current_url) == True

