import time
import pytest
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from assertpy import soft_assertions, assert_that
from utils.config import *
from utils.credentials import *

"""
Staring Chrome webdriver
"""

# @pytest.fixture(scope='module')
opts = Options()
browser = webdriver.Chrome(chrome_options=opts)
browser.maximize_window()
browser.implicitly_wait('10')

"""
ALL URLS
"""

ROOT_URL = "smevai.com"
APP_URL = f"https://app.{ROOT_URL}"
TESTING_URL = f"https://testing.{ROOT_URL}"
BASE_URL = TESTING_URL


"""
Generate Seed
"""

now = datetime.datetime.now()
seed = f"22-{now.month}-{now.day}-{now.hour}-{now.minute}-{now.second}"


"""
Login to the system
"""


def test_login():
    # email = (By.NAME, f'username')
    # password = (By.NAME, f'password')
    # button = (By.XPATH, f'/html/body/div/div[1]/div[2]/form/button')
    # dashboard = (By.XPATH, f'/html/body/div/div[2]/div[2]/div[1]/h2')
    # dashboard_text = "Dashboard"
    browser.get(BASE_URL)
    with soft_assertions():
        browser.get(BASE_URL)
        browser.get(BASE_URL)
        browser.find_element(By.NAME, f'username').send_keys('wpdabh+year22ta1@gmail.com')
        browser.find_element(By.NAME, f'password').send_keys('pass1234')
        browser.find_element(By.XPATH, f'/html/body/div/div[1]/div[2]/form/button').click()
        # assert_that(browser.find_element(By.XPATH, f'/html/body/div/div[2]/div[2]/div[1]/h2').text).is_equal_to('Dashboard')

"""
Create a Category
"""


def test_category():
    page_url = f"{BASE_URL}/product/category"
    create_category_page_url = f"{BASE_URL}/product/category/create"
    inp_category_name = (By.NAME, f'category_name')
    btn_category_save = (By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/form/div[2]/button')
    category_name = f'cat-{seed}'

    browser.get(BASE_URL)

    with soft_assertions():
        browser.get(create_category_page_url)
        browser.find_element(By.NAME, f'category_name').send_keys(category_name)
        browser.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/form/div[2]/button').click()
        browser.find_element(By.XPATH, f'//*[@id="categoryTableId_filter"]/label/input').send_keys(category_name)
        browser.implicitly_wait(10)
        assert_that(browser.find_element(By.XPATH, f'//*[@id="categoryTableId"]/tbody/tr/td[2]').text).is_equal_to(category_name)


"""
Create an item
"""


def test_item():
    url_product_item = f'{BASE_URL}/product/item'
    url_product_item_create = f'{BASE_URL}/product/item/create'
    item_name = f'item-{seed}'
    category_name = f'cat-{seed}'
    item_sku = f'sk-{seed}'
    purchase_price = 100
    sales_price = 200
    description = f'description-{seed}-this is the item description'

    browser.get(url_product_item)

    with soft_assertions():
        browser.get(url_product_item_create)
        browser.find_element(By.NAME, f'product_name').send_keys(item_name)

        browser.find_element(By.XPATH, f'//*[@id="createProduct"]/div[1]/div[2]/div/div/select').click()
        sel = Select(browser.find_element(By.XPATH, f'//*[@id="createProduct"]/div[1]/div[2]/div/div/select'))
        sel.select_by_visible_text(category_name)

        browser.find_element(By.NAME, f'product_sku').send_keys(item_sku)
        browser.find_element(By.NAME, f'purchase_price').send_keys(purchase_price)
        browser.find_element(By.NAME, f'sales_price').send_keys(sales_price)
        # browser.find_element(By.NAME, f'description').send_keys(description)
        browser.find_element(By.XPATH, f'//*[@id="createProduct"]/div[2]/button').click()

        browser.implicitly_wait(10)
        browser.find_element(By.XPATH, f'//*[@id="productTableId_filter"]/label/input').send_keys(item_name)
        browser.implicitly_wait(10)
        assert_that(browser.find_element(By.XPATH, f'//*[@id="productTableId"]/tbody/tr/td[2]').text).is_equal_to(item_name)


"""
Create supplier
"""


def test_supplier():
    url_supplier = f'{BASE_URL}/purchase/supplier'
    url_supplier_create = f'{BASE_URL}/purchase/supplier/create'
    supplier_name = f'sup-{seed}'
    supplier_phone = f'15544332211'
    supplier_email = f'wpdabh+{seed}@gmail.com'

    browser.get(url_supplier)

    with soft_assertions():
        browser.get(url_supplier_create)
        browser.find_element(By.NAME, f'name').send_keys(supplier_name)
        browser.find_element(By.NAME, f'phone').send_keys(supplier_phone)
        browser.find_element(By.NAME, f'email').send_keys(supplier_email)
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(1)
        browser.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/form/div[2]/button').click()

        browser.implicitly_wait(10)
        browser.find_element(By.XPATH, f'//*[@id="supplierTableId_filter"]/label/input').send_keys(supplier_name)
        browser.implicitly_wait(10)
        assert_that(browser.find_element(By.XPATH, f'//*[@id="supplierTableId"]/tbody/tr/td[2]').text).is_equal_to(supplier_name)


"""
Create Customer
"""


def test_customer():
    url_customer = f'{BASE_URL}/sales/customer'
    url_customer_create = f'{BASE_URL}/sales/customer/create'
    customer_name = f'cus-{seed}'
    customer_phone = f'15544332212'
    customer_email = f'wpdabh+{seed}@gmail.com'

    browser.get(url_customer)

    with soft_assertions():
        browser.get(url_customer_create)
        browser.find_element(By.NAME, f'name').send_keys(customer_name)
        browser.find_element(By.NAME, f'phone').send_keys(customer_phone)
        browser.find_element(By.NAME, f'email').send_keys(customer_email)
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(1)
        browser.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div[2]/div/form/div[2]/button').click()

        browser.implicitly_wait(10)
        browser.find_element(By.XPATH, f'//*[@id="customerTableId_filter"]/label/input').send_keys(customer_name)
        browser.implicitly_wait(10)
        assert_that(browser.find_element(By.XPATH, f'//*[@id="customerTableId"]/tbody/tr/td[2]').text).is_equal_to(customer_name)


"""
Create Purchase Invoice
"""


def test_purchase():
    url_purchase = f'{BASE_URL}/purchase/invoice'
    url_purchase_create = f'{BASE_URL}/purchase/invoice/create'
    supplier_name = f'sup-{seed}'
    item_name = f'item-{seed}'

    browser.get(url_purchase)

    with soft_assertions():
        browser.get(url_purchase_create)

        browser.find_element(By.XPATH, f'//*[@id="purchaseInvoice"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]').send_keys("aaaaa")
        time.sleep(3)

        browser.find_element(By.XPATH, f'//*[@id="purchaseInvoice"]/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/input')\
            .send_keys(supplier_name,Keys.DOWN)\
            .wait(5)\
            .send_keys(Keys.ENTER)

        browser.find_element(By.XPATH, f'//*[@id="purchaseInvoice"]/div/div[3]/div/div/div/div/div/div[2]/input').send_keys(item_name)\
            .wait(5)\
            .send_keys(Keys.DOWN, Keys.ENTER)

        browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(1)
        browser.find_element(By.XPATH, f'//*[@id="purchaseInvoice"]/div/div[9]/button[2]').click()

        browser.implicitly_wait(10)


"""
Create something
"""


def test_name():
    pass
    page_url = f''
    item_name = f'item-{seed}'

    browser.get(BASE_URL)

    with soft_assertions():
        browser.get(BASE_URL)
        # browser.find_element(By.XPATH, f'').send_keys()