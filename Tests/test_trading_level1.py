import time
from Pages.loginPage import LoginPage
from Pages.TradingCompany.dashboardPage import DashboardPage
from Pages.TradingCompany.categoryPage import CategoryPage
from Pages.TradingCompany.itemPage import ItemPage
from Pages.TradingCompany.supplierPage import SupplierPage
from Pages.TradingCompany.customerPage import CustomerPage
from Pages.TradingCompany.purchaseInvoicePage import PurchaseInvoicePage
from Pages.TradingCompany.companySettingsPage import CompanySettingsPage
from config import LINKS, DATA


def test_trading_level1(browser):
    # DONE: Login Into Trading Site
    login = LoginPage(browser)
    login.load()
    login.login(LINKS.TRADING_EMAIL, LINKS.PASSWORD)

    # DONE: Perform Factory Reset
    company_settings = CompanySettingsPage(browser)
    company_settings.load()
    company_settings.perform_factory_reset()

    # DONE: Create a category
    category = CategoryPage(browser)
    category.load_create_page()
    category.create_category(cat_name=DATA.cat_name)

    # DONE: Create an item
    item = ItemPage(browser)
    item.load_create_page()
    item.create_item(item_name=DATA.item_name,
                     cat_name=DATA.cat_name,
                     item_sku=DATA.item_sku,
                     item_purchase_price=DATA.item_purchase_price,
                     item_sales_price=DATA.item_sales_price,
                     item_description=DATA.item_description)

    # DONE: Create a supplier
    supplier = SupplierPage(browser)
    supplier.load_create_page()
    supplier.create_supplier(supplier_name=DATA.supplier_name, supplier_phone=DATA.supplier_phone)

    # DONE: Create a customer
    customer = CustomerPage(browser)
    customer.load_create_page()
    customer.create_customer(customer_name=DATA.customer_name, customer_phone=DATA.customer_phone)

    # DONE: Create a purchase invoice
    purchase = PurchaseInvoicePage(browser)
    purchase.load_create_page()
    purchase.create_purchase_invoice(purchase_inv_number=DATA.PURCHASE_INVOICE_NUMBER,
                                     purchase_item_quantity=DATA.PURCHASE_ITEM_QUANTITY,
                                     purchase_item_discount=DATA.PURCHASE_ITEM_DISCOUNT,
                                     purchase_item_shipping=DATA.PURCHASE_SHIPPING,
                                     purchase_item_vat_percent=DATA.PURCHASE_VAT_PERCENT)

    # TODO: Create a sales invoice

    # TODO: Create


