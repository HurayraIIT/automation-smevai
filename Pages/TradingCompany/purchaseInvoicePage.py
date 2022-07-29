import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

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

    select_additional_items_xpath = (By.XPATH, f'//*[@id="purchaseInvoice"]/div/div[6]/div/div[2]/div/div/select')
    shipping_input_xpath = (By.XPATH, f'//*[@id="purchaseInvoice"]/div/div[6]/div[2]/div[3]/input')
    vat_input_xpath = (By.XPATH, f'//*[@id="purchaseInvoice"]/div/div[6]/div[3]/div[2]/input')

    add_signature_xpath = (By.XPATH, f"//span[@class='label__text']")
    default_note_btn_xpath = (By.XPATH, f"//button[normalize-space()='Default Note']")

    save_btn_xpath = (By.XPATH, f"//button[normalize-space()='Save']")
    cancel_btn_xpath = (By.XPATH, f"//button[normalize-space()='Cancel']")

    # List Page Locators
    search_xpath = (By.XPATH, f'//*[@id="purchaseTableId_filter"]/label/input')
    search_result_action_xpath = (By.XPATH, f'//*[@id="purchaseTableId"]/tbody/tr/td[10]/div/a')
    complete_button_xpath = (By.XPATH, f'//*[@id="purchaseTableId"]/tbody/tr/td[10]/div/ul/li[8]/a')
    update_confirm_xpath = (By.XPATH, f'//*[@id="invoiceStatusModal"]/div/div/div/div/a[2]')
    update_cancel_xpath = (By.XPATH, f'//*[@id="invoiceStatusModal"]/div/div/div/div/a[1]')
    completed_status_xpath = (By.XPATH, f'//*[@id="purchaseTableId"]/tbody/tr/td[5]/span')

    def __init__(self, browser):
        self.browser = browser

    # def load_create_page(self):
    #     self.browser.get(self.CREATE_URL)
    #     time.sleep(1)
    #     assert self.browser.find_element(*self.create_heading_xpath).text == self.create_heading_text

    # def load_list_page(self):
    #     self.browser.get(self.LIST_URL)
    #     time.sleep(1)
    #     assert self.browser.find_element(*self.list_heading_xpath).text == self.list_heading_text

    def create_purchase_invoice(self,
                                purchase_inv_number="10000001",
                                purchase_item_quantity=5,
                                purchase_item_discount=10,
                                purchase_item_shipping=50,
                                purchase_item_vat_percent=10):
        # Load Create Page
        self.browser.get(self.CREATE_URL)
        time.sleep(1)
        assert self.browser.find_element(*self.create_heading_xpath).text == self.create_heading_text

        # Enter Values
        self.browser.find_element(*self.invoice_number_xpath).clear()
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

        time.sleep(1)
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(1)

        # Additional Items

        element = self.browser.find_element(*self.select_additional_items_xpath)
        element.click()
        select = Select(element)
        select.select_by_visible_text("VAT")
        time.sleep(1)
        select.select_by_visible_text("Shipping Charge")
        time.sleep(1)

        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(1)

        self.browser.find_element(*self.shipping_input_xpath).click()
        self.browser.find_element(*self.shipping_input_xpath).clear()
        self.browser.find_element(*self.shipping_input_xpath).send_keys(purchase_item_shipping)
        time.sleep(1)

        self.browser.find_element(*self.vat_input_xpath).click()
        self.browser.find_element(*self.vat_input_xpath).clear()
        self.browser.find_element(*self.vat_input_xpath).send_keys(purchase_item_vat_percent)
        time.sleep(2)

        self.browser.find_element(*self.add_signature_xpath).click()
        self.browser.find_element(*self.save_btn_xpath).click()
        time.sleep(2)
        assert self.browser.current_url == self.LIST_URL

    def complete_purchase_invoice(self, purchase_inv_number):
        # Load list page
        self.browser.get(self.LIST_URL)
        time.sleep(1)
        # assert self.browser.find_element(*self.list_heading_xpath).text == self.list_heading_text

        # DONE: Search invoice by invoice number
        self.browser.find_element(*self.search_xpath).click()
        self.browser.find_element(*self.search_xpath).clear()
        self.browser.find_element(*self.search_xpath).send_keys(purchase_inv_number)
        time.sleep(1)

        # DONE: Mark it complete
        self.browser.find_element(*self.search_result_action_xpath).click()
        time.sleep(0.5)
        self.browser.find_element(*self.complete_button_xpath).click()
        time.sleep(1)
        self.browser.find_element(*self.update_confirm_xpath).click()
        time.sleep(1.5)

        # DONE: Check if invoice is completed
        assert self.browser.find_element(*self.completed_status_xpath).text == "Completed"
