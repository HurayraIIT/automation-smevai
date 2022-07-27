import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from config import LINKS, DATA


class StockSummaryPage:
    PAGE_URL = LINKS.STOCK_SUMMARY_PAGE

    heading_xpath = (By.XPATH, f"//h2[@class='access__form__title']")
    heading_text = f"Stock Summary List"

    item_name_xpath = (By.XPATH, f'//*[@id="stockSummaryTableId"]/tbody/tr/td[2]')
    purchase_xpath = (By.XPATH, f'//*[@id="stockSummaryTableId"]/tbody/tr/td[5]')
    sale_xpath = (By.XPATH, f'//*[@id="stockSummaryTableId"]/tbody/tr/td[6]')
    purchase_return_xpath = (By.XPATH, f'//*[@id="stockSummaryTableId"]/tbody/tr/td[7]')
    sales_return_xpath = (By.XPATH, f'//*[@id="stockSummaryTableId"]/tbody/tr/td[8]')
    available_stock_xpath = (By.XPATH, f'//*[@id="stockSummaryTableId"]/tbody/tr/td[9]')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.PAGE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

    def check_stock(self,
                    item_name="item001",
                    purchase=5,
                    sale=0,
                    purchase_return=0,
                    sales_return=0,
                    available_stock=5):
        # Load Page
        self.browser.get(self.PAGE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

        # Check Stock
        assert self.browser.find_element(*self.item_name_xpath).text == item_name
        assert self.browser.find_element(*self.purchase_xpath).text == str(purchase)
        assert self.browser.find_element(*self.sale_xpath).text == str(sale)
        assert self.browser.find_element(*self.purchase_return_xpath).text == str(purchase_return)
        assert self.browser.find_element(*self.sales_return_xpath).text == str(sales_return)
        assert self.browser.find_element(*self.available_stock_xpath).text == str(available_stock)
        time.sleep(1)
