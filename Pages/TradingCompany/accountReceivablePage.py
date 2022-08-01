import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from config import LINKS, DATA


class AccountReceivablePage:
    PAGE_URL = LINKS.ACCOUNT_RECEIVABLE_PAGE

    heading_xpath = (By.XPATH, f"//h2[@class='access__form__title']")
    heading_text = f"Account Receivable List"

    customer_name_xpath = (By.XPATH, f'//*[@id="accountReceivableTableId"]/tbody/tr/td[2]')
    total_sale_xpath = (By.XPATH, f'//*[@id="accountReceivableTableId"]/tbody/tr/td[4]')
    total_received_xpath = (By.XPATH, f'//*[@id="accountReceivableTableId"]/tbody/tr/td[5]')
    total_due_xpath = (By.XPATH, f'//*[@id="accountReceivableTableId"]/tbody/tr/td[6]')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.PAGE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

    def check_entry(self,
                    customer_name="customer001",
                    total_sale='৳1,090.00',
                    total_received='৳0.00',
                    total_due='৳1,090.00'):
        # Load Page
        self.browser.get(self.PAGE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

        # Check Values
        assert self.browser.find_element(*self.customer_name_xpath).text == customer_name
        assert self.browser.find_element(*self.total_sale_xpath).text == total_sale
        assert self.browser.find_element(*self.total_received_xpath).text == total_received
        assert self.browser.find_element(*self.total_due_xpath).text == total_due
