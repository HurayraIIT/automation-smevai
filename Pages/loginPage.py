class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.login_page_heading_text_xpath = f"/html/body/div[1]/div[1]/div[2]/h2"
        self.login_page_heading_text = f"Login"
        self.username_textbox_name = f"username"
        self.password_textbox_name = f"password"
        self.submit_button_xpath = f"//button[@class='button button__themeColor button__block']"

        def enter_username(self, username):
            pass

        def enter_password(self, password):
            pass

        def click_submit(self):
            pass
