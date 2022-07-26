import time
from Pages.loginPage import LoginPage
from Pages.TradingCompany.dashboardPage import DashboardPage
from Pages.TradingCompany.categoryPage import CategoryPage
from Pages.TradingCompany.companySettingsPage import CompanySettingsPage
from config import DATA


def test_trading_level1(browser):
    # Login Into Trading Site
    login = LoginPage(browser)
    login.load()
    login.login(DATA.TRADING_EMAIL, DATA.PASSWORD)
    time.sleep(2)

    # TODO: Perform Factory Reset
    company_settings = CompanySettingsPage(browser)
    company_settings.load()
    company_settings.perform_factory_reset()

    # TODO: Create a category
    category = CategoryPage(browser)
    category.load_create_page()
    category.create_category("cat001")

    # TODO: Create an item

    # TODO: Create a supplier

    # TODO: Create a customer

    # TODO: Create a purchase invoice

    # TODO: Create a sales invoice

    # TODO: Create


