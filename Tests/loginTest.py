import time
import sys
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

        login = LoginPage(driver)
        driver.find_element(By.NAME, login.username_textbox_name).send_keys("wpdabh+autota1@gmail.com")
        driver.find_element(By.NAME, login.password_textbox_name).send_keys("pass1234")
        driver.find_element(By.XPATH, login.submit_button_xpath).click()


        time.sleep(7)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
