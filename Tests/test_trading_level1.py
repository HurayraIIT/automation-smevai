import time
from Pages.loginPage import LoginPage
from Pages.TradingCompany.dashboardPage import DashboardPage
from config import DATA


def test_trading_level1(browser):
    login = LoginPage(browser)
    login.load()
    login.login(DATA.TRADING_EMAIL, DATA.PASSWORD)
    time.sleep(2)

    dashboard = DashboardPage(browser)
    dashboard.load()
    dashboard.click_logout()
    time.sleep(5)
