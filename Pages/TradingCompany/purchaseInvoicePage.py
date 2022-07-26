import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import LINKS, DATA


class PurchaseInvoicePage:
    LIST_URL = LINKS.PURCHASE_INVOICE_LIST_PAGE
    CREATE_URL = LINKS.PURCHASE_INVOICE_CREATE_PAGE

    create_heading_xpath = (By.XPATH, f"//h2[@class='access__form__title']")
    create_heading_text = f"Create Purchase Invoice"

    list_heading_xpath = (By.XPATH, f"//h2[@class='access__form__title']")
    list_heading_text = f"Purchase Invoice List"

    invoice_number_xpath = (By.XPATH, f"//input[@placeholder='XXXXXXXX']")

    supplier_multiselect_xpath = (By.XPATH, f"//div[@class='supplier__details__block']//div[@class='multiselect']")
    supplier_multiselect_after_xpath = (By.XPATH, f"//input[@placeholder='Search supplier']")

    product_multiselect_xpath = (By.XPATH, f"//span[normalize-space()='Search & add products']")
    product_multiselect_after_xpath = (By.XPATH, f"//input[@placeholder='Search & add products']")

    item_quantity_xpath = (By.XPATH, f"//div[@class='table__col col__qty']//input[@placeholder='eg: 10']")
    item_discount_xpath = (By.XPATH, f"//div[@class='table__col col__discount']//input[@placeholder='eg: 10']")

    select_additional_items_xpath = (By.XPATH, f"//div[@class='table__col col__head col__total']//div[@class='d-flex']")
    shipping_input_xpath = (By.XPATH, f"(//input[@placeholder='eg: 300.00'])[1]")
    vat_input_xpath = (By.XPATH, f"(//input[@placeholder='eg: 300.00'])[2]")

    add_signature_xpath = (By.XPATH, f"//span[@class='label__text']")
    default_note_btn_xpath = (By.XPATH, f"//button[normalize-space()='Default Note']")

    save_btn_xpath = (By.XPATH, f"//button[normalize-space()='Save']")
    cancel_btn_xpath = (By.XPATH, f"//button[normalize-space()='Cancel']")

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

    def create_purchase_invoice(self, purchase_inv_number="10000001",
                    purchase_item_quantity=5,
                    purchase_item_discount=10,
                    purchase_item_shipping=50,
                    purchase_item_vat_percent=10):

        self.browser.find_element(*self.invoice_number_xpath).send_keys(purchase_inv_number)

        self.browser.find_element(*self.supplier_multiselect_xpath).click()
        time.sleep(1)
        self.browser.find_element(*self.supplier_multiselect_after_xpath).send_keys(DATA.supplier_name)
        time.sleep(1)
        self.browser.find_element(*self.supplier_multiselect_after_xpath).send_keys(Keys.ENTER)
        time.sleep(1)

        self.browser.find_element(*self.product_multiselect_xpath).click()
        time.sleep(1)
        self.browser.find_element(*self.product_multiselect_after_xpath).send_keys(DATA.item_name)
        time.sleep(1)
        self.browser.find_element(*self.product_multiselect_after_xpath).send_keys(Keys.ENTER)
        time.sleep(1)

        self.browser.find_element(*self.item_quantity_xpath).clear()
        self.browser.find_element(*self.item_quantity_xpath).send_keys(purchase_item_quantity)
        self.browser.find_element(*self.item_discount_xpath).clear()
        self.browser.find_element(*self.item_discount_xpath).send_keys(purchase_item_discount)

        # TODO: FIX THIS
        self.browser.find_element(*self.select_additional_items_xpath).click()
        time.sleep(1)
        self.browser.find_element(*self.select_additional_items_xpath).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        self.browser.find_element(*self.select_additional_items_xpath).send_keys(Keys.ENTER)
        time.sleep(1)
        self.browser.find_element(*self.select_additional_items_xpath).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        self.browser.find_element(*self.select_additional_items_xpath).send_keys(Keys.ENTER)
        time.sleep(1)

        self.browser.find_element(*self.shipping_input_xpath).send_keys(purchase_item_shipping)
        self.browser.find_element(*self.vat_input_xpath).send_keys(purchase_item_vat_percent)

        self.browser.find_element(*self.add_signature_xpath).click()

        self.browser.find_element(*self.save_btn_xpath).click()
        time.sleep(2)
        assert self.browser.current_url == self.LIST_URL
        time.sleep(3)

        # assert self.browser.find_element(*self.factory_reset_title_xpath).text == self.factory_reset_title_text

