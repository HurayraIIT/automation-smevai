from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import DATA


class DashboardPage:

    URL = DATA.DASHBOARD
    dashboard_title_text = f"Dashboard"
    dashboard_title_text_xpath = (By.XPATH, f"//h2[normalize-space()='Dashboard']")
    logout_button_link_xpath = (By.XPATH, f"//span[normalize-space()='Log Out']")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)
        assert self.browser.find_element(*self.dashboard_title_text_xpath).text == self.dashboard_title_text

    def click_logout(self):
        self.browser.find_element(*self.logout_button_link_xpath).click()
