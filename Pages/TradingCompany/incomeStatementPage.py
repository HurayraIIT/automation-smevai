import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from config import LINKS, DATA


class IncomeStatementPage:
    PAGE_URL = LINKS.INCOME_STATEMENT_PAGE

    heading_xpath = (By.XPATH, f"//h2[@class='access__form__title']")
    heading_text = f"Income Statement"

    net_sales_xpath = (By.XPATH,
                       f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td/table[1]/tfoot/tr/td[2]')
    total_purchase_xpath = (By.XPATH,
                            f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td/table[2]/thead/tr/th[2]')
    purchase_shipping_charge_xpath = (By.XPATH,
                            f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td/table[2]/tbody/tr[2]/td[2]')
    total_cost_of_purchase_xpath = (By.XPATH,
                                      f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td/table[2]/tfoot/tr/td[2]')
    gross_profit_xpath = (By.XPATH,
                            f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[2]/td/table/tfoot/tr/td[2]')
    total_operation_expenses_xpath = (By.XPATH,
                            f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[3]/td/table/tfoot/tr/td[2]')
    operation_income_xpath = (By.XPATH,
                            f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[4]/td/table/thead/tr/th[2]')
    net_profit_xpath = (By.XPATH,
                            f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[5]/td/table/tfoot/tr/td[2]')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.PAGE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

    def check_income_statement(self,
                               net_sales="৳0.00",
                               total_purchase="৳495.00",
                               purchase_shipping_charge="৳50.00",
                               total_cost_of_purchase="৳545.00",
                               gross_profit="৳-545.00",
                               total_operation_expenses="৳0.00",
                               operation_income="৳-545.00",
                               net_profit="৳-545.00"):
        # Load Page
        self.browser.get(self.PAGE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

        # Check Stock
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(1)

        assert self.browser.find_element(*self.net_sales_xpath).text == net_sales
        assert self.browser.find_element(*self.total_purchase_xpath).text == total_purchase
        assert self.browser.find_element(*self.purchase_shipping_charge_xpath).text == purchase_shipping_charge
        assert self.browser.find_element(*self.total_cost_of_purchase_xpath).text == total_cost_of_purchase
        assert self.browser.find_element(*self.gross_profit_xpath).text == gross_profit
        assert self.browser.find_element(*self.total_operation_expenses_xpath).text == total_operation_expenses
        assert self.browser.find_element(*self.operation_income_xpath).text == operation_income
        assert self.browser.find_element(*self.net_profit_xpath).text == net_profit

        time.sleep(1)
