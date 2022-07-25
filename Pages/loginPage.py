import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import DATA


class LoginPage:
    URL = DATA.SITE
    login_page_heading_text_xpath = f"/html/body/div[1]/div[1]/div[2]/h2"
    login_page_heading_text = f"Login"
    username_textbox_name = f"username"
    password_textbox_name = f"password"
    submit_button_xpath = f"//button[@class='button button__themeColor button__block']"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def login(self, username, password):
        self.browser.find_element(By.NAME, self.username_textbox_name).send_keys(username)
        self.browser.find_element(By.NAME, self.password_textbox_name).send_keys(password)
        self.browser.find_element(By.XPATH, self.submit_button_xpath).click()


