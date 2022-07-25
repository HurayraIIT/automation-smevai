from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DashboardPage:
    def __init__(self, browser):
        self.browser = browser

        self.dashboard_title_text = f"Dashboard"
        self.dashboard_title_text_xpath = f"//h2[normalize-space()='Dashboard']"
        self.logout_button_link_xpath = f"//span[normalize-space()='Log Out']"

    def load(self):
        self.browser.get("https://app.smevai.com/dashboard")

    def click_logout(self):
        self.browser.find_element(By.XPATH, self.logout_button_link_xpath).click()
