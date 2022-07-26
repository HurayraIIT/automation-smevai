import time
from Pages.loginPage import LoginPage
from Pages.TradingCompany.dashboardPage import DashboardPage
from config import LINKS


def test_login_logout_valid(browser):
    login = LoginPage(browser)
    login.load()
    login.login(LINKS.TRADING_EMAIL, LINKS.PASSWORD)
    time.sleep(2)

    dashboard = DashboardPage(browser)
    dashboard.load()
    dashboard.click_logout()
    time.sleep(5)
