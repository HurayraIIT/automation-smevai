import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from config import LINKS, DATA


class IncomeStatementPage:
    PAGE_URL = LINKS.INCOME_STATEMENT_PAGE

    heading_xpath = (By.XPATH, f"//h2[@class='access__form__title']")
    heading_text = f"Income Statement"

    TOTAL_SALES_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td/table[1]/thead/tr[2]/th[2]/span[2]')
    SALES_RETURN_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td/table[1]/tbody/tr/td[2]/span[2]')
    NET_SALES_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td/table[1]/tfoot/tr/td[2]/span[2]')
    TOTAL_PURCHASE_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td/table[2]/thead/tr/th[2]/span[2]')
    PURCHASE_RETURN_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td/table[2]/tbody/tr[1]/td[2]/span[2]')
    PURCHASE_SHIPPING_CHARGE_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td/table[2]/tbody/tr[2]/td[2]/span[2]')
    TOTAL_COST_OF_PURCHASE_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td/table[2]/tfoot/tr/td[2]/span[2]')
    GROSS_PROFIT_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[2]/td/table/tfoot/tr/td[2]/span[2]')
    TOTAL_OPERATION_EXPENSES_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[3]/td/table/tfoot/tr/td[2]/span[2]')
    OPERATION_INCOME_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[4]/td/table/thead/tr/th[2]/span[2]')
    SALES_SHIPPING_CHARGE_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[4]/td/table/tbody/tr/td[2]/span[2]')
    TOTAL_NON_OPERATION_INCOME_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[4]/td/table/tfoot/tr/td[2]/span[2]')
    NET_PROFIT_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[5]/td/table/tfoot/tr/td[2]/span[2]')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.PAGE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

    def check_income_statement(self,
                               TOTAL_SALES="0.00",
                               SALES_RETURN="0.00",
                               NET_SALES="0.00",
                               TOTAL_PURCHASE="0.00",
                               PURCHASE_RETURN="0.00",
                               PURCHASE_SHIPPING_CHARGE="0.00",
                               TOTAL_COST_OF_PURCHASE="0.00",
                               GROSS_PROFIT="0.00",
                               TOTAL_OPERATION_EXPENSES="0.00",
                               OPERATION_INCOME="0.00",
                               SALES_SHIPPING_CHARGE="0.00",
                               TOTAL_NON_OPERATION_INCOME="0.00",
                               NET_PROFIT="0.00"):
        # Load Page
        self.browser.get(self.PAGE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

        # Check Stock
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(1)

        assert self.browser.find_element(*self.TOTAL_SALES_xpath).text == TOTAL_SALES
        assert self.browser.find_element(*self.SALES_RETURN_xpath).text == SALES_RETURN
        assert self.browser.find_element(*self.NET_SALES_xpath).text == NET_SALES
        assert self.browser.find_element(*self.TOTAL_PURCHASE_xpath).text == TOTAL_PURCHASE
        assert self.browser.find_element(*self.PURCHASE_RETURN_xpath).text == PURCHASE_RETURN
        assert self.browser.find_element(*self.PURCHASE_SHIPPING_CHARGE_xpath).text == PURCHASE_SHIPPING_CHARGE
        assert self.browser.find_element(*self.TOTAL_COST_OF_PURCHASE_xpath).text == TOTAL_COST_OF_PURCHASE
        assert self.browser.find_element(*self.GROSS_PROFIT_xpath).text == GROSS_PROFIT
        assert self.browser.find_element(*self.TOTAL_OPERATION_EXPENSES_xpath).text == TOTAL_OPERATION_EXPENSES
        assert self.browser.find_element(*self.OPERATION_INCOME_xpath).text == OPERATION_INCOME
        assert self.browser.find_element(*self.SALES_SHIPPING_CHARGE_xpath).text == SALES_SHIPPING_CHARGE
        assert self.browser.find_element(*self.TOTAL_NON_OPERATION_INCOME_xpath).text == TOTAL_NON_OPERATION_INCOME
        assert self.browser.find_element(*self.NET_PROFIT_xpath).text == NET_PROFIT

        time.sleep(1)
