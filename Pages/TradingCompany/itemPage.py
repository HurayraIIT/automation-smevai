import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import LINKS


class ItemPage:
    LIST_URL = LINKS.ITEM_LIST_PAGE
    CREATE_URL = LINKS.ITEM_CREATE_PAGE

    create_heading_xpath = (By.XPATH, f"//h2[normalize-space()='Create Item']")
    create_heading_text = f"Create Item"

    list_heading_xpath = (By.XPATH, f"//h2[normalize-space()='Product List']")
    list_heading_text = f"Product List"

    item_name_xpath = (By.XPATH, f"//input[@name='product_name']")
    category_select_xpath = (By.XPATH, f"//select[@name='category_id']")

    item_sku_xpath = (By.XPATH, f"//input[@name='product_sku']")
    purchase_price_xpath = (By.XPATH, f"//input[@name='purchase_price']")
    sales_price_xpath = (By.XPATH, f"//input[@name='sales_price']")
    description_xpath = (By.XPATH, f"//textarea[@name='description']")

    save_btn_xpath = (By.XPATH, f"//button[@type='submit']")
    cancel_btn_xpath = (By.XPATH, f"//a[@class='button']")

    def __init__(self, browser):
        self.browser = browser

    def load_create_page(self):
        self.browser.get(self.CREATE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.create_heading_xpath).text == self.create_heading_text

    def load_list_page(self):
        self.browser.get(self.LIST_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.list_heading_xpath).text == self.list_heading_text

    def create_item(self, item_name="item01",
                    cat_name="cat01",
                    item_sku="sk01",
                    item_purchase_price=100,
                    item_sales_price=100,
                    item_description="item description"):

        self.browser.find_element(*self.item_name_xpath).send_keys(item_name)
        self.browser.find_element(*self.item_sku_xpath).send_keys(item_sku)
        self.browser.find_element(*self.purchase_price_xpath).send_keys(item_purchase_price)
        self.browser.find_element(*self.sales_price_xpath).send_keys(item_sales_price)
        self.browser.find_element(*self.description_xpath).send_keys(item_description)

        self.browser.find_element(*self.category_select_xpath).click()
        time.sleep(1)
        self.browser.find_element(*self.category_select_xpath).send_keys(cat_name)
        time.sleep(1)
        self.browser.find_element(*self.category_select_xpath).send_keys(Keys.ENTER)
        time.sleep(1)

        self.browser.find_element(*self.save_btn_xpath).click()
        time.sleep(2)
        assert self.browser.current_url == self.LIST_URL
