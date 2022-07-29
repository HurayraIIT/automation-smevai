import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from config import LINKS, DATA


class AccountPayablePage:
    PAGE_URL = LINKS.ACCOUNT_PAYABLE_PAGE

    heading_xpath = (By.XPATH, f"//h2[@class='access__form__title']")
    heading_text = f"Account Payable List"

    supplier_name_xpath = (By.XPATH, f'//*[@id="accountPayableTableId"]/tbody/tr/td[2]')
    total_purchase_xpath = (By.XPATH, f'//*[@id="accountPayableTableId"]/tbody/tr/td[4]')
    total_paid_xpath = (By.XPATH, f'//*[@id="accountPayableTableId"]/tbody/tr/td[5]')
    total_due_xpath = (By.XPATH, f'//*[@id="accountPayableTableId"]/tbody/tr/td[6]')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.PAGE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

    def check_entry(self,
                    supplier_name="supplier001",
                    total_purchase=545,
                    total_paid=0,
                    total_due=545):
        # Load Page
        self.browser.get(self.PAGE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

        # Check Values
        assert self.browser.find_element(*self.supplier_name_xpath).text == supplier_name
        assert (str(total_purchase) in self.browser.find_element(*self.total_purchase_xpath).text) == True
        assert (f"{str(total_paid)}.00" in self.browser.find_element(*self.total_paid_xpath).text) == True
        assert (str(total_due) in self.browser.find_element(*self.total_due_xpath).text) == True
