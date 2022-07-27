import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from config import LINKS, DATA


class TransactionHistoryPage:
    PAGE_URL = LINKS.TRANSACTION_HISTORY_PAGE

    heading_xpath = (By.XPATH, f"//h2[@class='access__form__title']")
    heading_text = f"Transaction History List"

    account_head_xpath = (By.XPATH, f'//*[@id="transactionHistoryTableId"]/tbody/tr/td[2]/span')
    transaction_type_xpath = (By.XPATH, f'//*[@id="transactionHistoryTableId"]/tbody/tr/td[3]/span')
    amount_xpath = (By.XPATH, f'//*[@id="transactionHistoryTableId"]/tbody/tr/td[6]')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.PAGE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

    def check_entry(self, account_head="Purchase", transaction_type="Due", amount=545):
        # Load Page
        self.browser.get(self.PAGE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

        # Check Values
        assert self.browser.find_element(*self.account_head_xpath).text == account_head
        assert self.browser.find_element(*self.transaction_type_xpath).text == transaction_type
        assert (str(amount) in self.browser.find_element(*self.amount_xpath).text) == True
