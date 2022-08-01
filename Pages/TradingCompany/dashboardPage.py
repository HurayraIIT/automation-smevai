from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import LINKS
import time


class DashboardPage:

    PAGE_URL = LINKS.DASHBOARD
    heading_text = f"Dashboard"
    heading_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[1]/h2')

    logout_button_link_xpath = (By.XPATH, f"//span[normalize-space()='Log Out']")

    total_order_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/h3')
    avg_order_value_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div[2]/h3/span[2]')
    cash_in_hand_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div[3]/div/div/div[2]/h3/span[2]')
    total_stock_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div[4]/div/div/div[2]/h3')

    # Top Bar XPATH
    topbar_cash_wallet_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[2]/a/span/span/span[2]')
    topbar_bank_wallet_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[3]/a/span/span/span[2]')
    topbar_mobilebanking_wallet_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div[4]/a/span/span/span[2]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.PAGE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

    def check_dashboard(self,
                        total_order="0",
                        avg_order_value="৳1,090.00",
                        cash_in_hand="৳0.00",
                        total_stock="5"):
        self.browser.get(self.PAGE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

        assert self.browser.find_element(*self.total_order_xpath).text == total_order
        assert self.browser.find_element(*self.avg_order_value_xpath).text == avg_order_value
        assert self.browser.find_element(*self.cash_in_hand_xpath).text == cash_in_hand
        assert self.browser.find_element(*self.total_stock_xpath).text == total_stock

    def click_logout(self):
        self.browser.find_element(*self.logout_button_link_xpath).click()

    def check_topbar(self, cash="0.00", bank="0.00", mobile="0.00"):
        # Navigate to dashboard
        self.browser.get(self.PAGE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

        assert self.browser.find_element(*self.topbar_cash_wallet_xpath).text == cash
        assert self.browser.find_element(*self.topbar_bank_wallet_xpath).text == bank
        assert self.browser.find_element(*self.topbar_mobilebanking_wallet_xpath).text == mobile
