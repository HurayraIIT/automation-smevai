import time
from Pages.loginPage import LoginPage
from Pages.dashboardPage import DashboardPage


def test_login_logout_valid(browser):
    # driver.get("https://app.smevai.com")

    login = LoginPage(browser)
    login.load()
    login.enter_username("abuhurayra183+tpta1@gmail.com")
    login.enter_password("pass1234")
    login.click_submit()
    time.sleep(2)

    dashboard = DashboardPage(browser)
    dashboard.load()
    dashboard.click_logout()
    time.sleep(5)
