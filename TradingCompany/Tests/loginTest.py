import time
import unittest
from selenium import webdriver
from TradingCompany.Pages.loginPage import LoginPage
from TradingCompany.Pages.dashboardPage import DashboardPage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="/home/hurayra/GitHub/automation-smevai/webdrivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_logout_valid(self):
        self.driver.get("https://app.smevai.com")

        login = LoginPage(self.driver)
        login.enter_username("abuhurayra183+tpta1@gmail.com")
        login.enter_password("pass1234")
        login.click_submit()
        time.sleep(2)

        dashboard = DashboardPage(self.driver)
        dashboard.click_logout()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
