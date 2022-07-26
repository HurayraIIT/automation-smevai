import time
from Pages.loginPage import LoginPage
from Pages.TradingCompany.dashboardPage import DashboardPage
from Pages.TradingCompany.categoryPage import CategoryPage
from Pages.TradingCompany.itemPage import ItemPage
from Pages.TradingCompany.supplierPage import SupplierPage
from Pages.TradingCompany.customerPage import CustomerPage
from Pages.TradingCompany.companySettingsPage import CompanySettingsPage
from config import DATA


def test_trading_level1(browser):
    # DONE: Login Into Trading Site
    login = LoginPage(browser)
    login.load()
    login.login(DATA.TRADING_EMAIL, DATA.PASSWORD)
    time.sleep(2)

    # DONE: Perform Factory Reset
    company_settings = CompanySettingsPage(browser)
    company_settings.load()
    company_settings.perform_factory_reset()

    # DONE: Create a category
    category = CategoryPage(browser)
    category.load_create_page()
    category.create_category("cat001")

    # TODO: Create an item
    item = ItemPage(browser)
    item.load_create_page()
    item.create_item(item_name="item01",
                     cat_name="cat001",
                     item_sku="sk01",
                     item_purchase_price=100,
                     item_sales_price=200,
                     item_description="item description")

    # DONE: Create a supplier
    supplier = SupplierPage(browser)
    supplier.load_create_page()
    supplier.create_supplier(supplier_name="supplier001", supplier_phone="1657887766")

    # DONE: Create a customer
    customer = CustomerPage(browser)
    customer.load_create_page()
    customer.create_customer(customer_name="customer001", customer_phone="1657887766")

    # TODO: Create a purchase invoice

    # TODO: Create a sales invoice

    # TODO: Create


