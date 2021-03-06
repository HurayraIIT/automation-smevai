import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from config import LINKS, DATA


class BalanceSheetPage:
    PAGE_URL = LINKS.BALANCE_SHEET_PAGE

    heading_xpath = (By.XPATH, f"//h2[@class='access__form__title']")
    heading_text = f"Balance Sheet"

    cash_wallet_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td[2]/span[2]')
    bank_wallet_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[2]/td[2]/span[2]')
    mobile_banking_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[3]/td[2]/span[2]')
    account_receivable_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[4]/td[2]/span[2]')
    inventory_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[5]/td[2]/span[2]')
    asset_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[6]/td[2]/span[2]')
    vat_amount_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[7]/td[2]/span[2]')

    owners_equity_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td[4]/span[2]')
    accounts_payable_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[2]/td[4]/span[2]')

    total_asset_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tfoot/tr/td[2]/span[2]')
    total_liabilities_xpath = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tfoot/tr/td[4]/span[2]')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.PAGE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

    def check_balance_sheet(
            self,
            cash_wallet="0.00",
            bank_wallet="0.00",
            mobile_banking="0.00",
            account_receivable="0.00",
            inventory="500.00",
            asset="0.00",
            vat_amount="45.00",
            total_asset="545.00",
            owners_equity="0.00",
            accounts_payable="545.00",
            total_liabilities="545.00"):
        # Load Page
        self.browser.get(self.PAGE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.heading_xpath).text == self.heading_text

        # Check Balance Sheet
        assert self.browser.find_element(*self.total_asset_xpath).text == self.browser.find_element(*self.total_liabilities_xpath).text
        assert self.browser.find_element(*self.total_asset_xpath).text == total_asset
        assert self.browser.find_element(*self.total_liabilities_xpath).text == total_liabilities

        assert self.browser.find_element(*self.cash_wallet_xpath).text == cash_wallet
        assert self.browser.find_element(*self.bank_wallet_xpath).text == bank_wallet
        assert self.browser.find_element(*self.mobile_banking_xpath).text == mobile_banking
        assert self.browser.find_element(*self.account_receivable_xpath).text == account_receivable
        assert self.browser.find_element(*self.inventory_xpath).text == inventory
        assert self.browser.find_element(*self.asset_xpath).text == asset
        assert self.browser.find_element(*self.vat_amount_xpath).text == vat_amount

        assert self.browser.find_element(*self.owners_equity_xpath).text == owners_equity
        assert self.browser.find_element(*self.accounts_payable_xpath).text == accounts_payable

        time.sleep(1)
