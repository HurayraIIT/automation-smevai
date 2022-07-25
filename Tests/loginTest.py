import time
import sys
import os
import unittest
from selenium import webdriver
from Pages.loginPage import LoginPage
from Pages.dashboardPage import DashboardPage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="/home/hurayra/GitHub/automation-smevai/webdrivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://app.smevai.com")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
