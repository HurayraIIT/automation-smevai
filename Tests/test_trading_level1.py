import time

from Pages.TradingCompany.accountPayablePage import AccountPayablePage
from Pages.TradingCompany.incomeStatementPage import IncomeStatementPage
from Pages.TradingCompany.stockSummaryPage import StockSummaryPage
from Pages.TradingCompany.transactionHistoryPage import TransactionHistoryPage
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
    print("OK: Logged IN")

    # DONE: Perform Factory Reset
    company_settings = CompanySettingsPage(browser)
    company_settings.load()
    company_settings.perform_factory_reset()
    print("OK: Perform Factory Reset")

    # DONE: Create a category
    category = CategoryPage(browser)
    category.load_create_page()
    category.create_category(cat_name=DATA.cat_name)
    print("OK: Create a category")

    # DONE: Create an item
    item = ItemPage(browser)
    item.load_create_page()
    item.create_item(item_name=DATA.item_name,
                     cat_name=DATA.cat_name,
                     item_sku=DATA.item_sku,
                     item_purchase_price=DATA.item_purchase_price,
                     item_sales_price=DATA.item_sales_price,
                     item_description=DATA.item_description)
    print("OK: Create an item")

    # DONE: Create a supplier
    supplier = SupplierPage(browser)
    supplier.load_create_page()
    supplier.create_supplier(supplier_name=DATA.supplier_name, supplier_phone=DATA.supplier_phone)
    print("OK: Create a supplier")

    # DONE: Create a customer
    customer = CustomerPage(browser)
    customer.load_create_page()
    customer.create_customer(customer_name=DATA.customer_name, customer_phone=DATA.customer_phone)
    print("OK: Create a customer")

    # DONE: Create a purchase invoice
    purchase = PurchaseInvoicePage(browser)
    purchase.create_purchase_invoice(purchase_inv_number=DATA.PURCHASE_INVOICE_NUMBER,
                                     purchase_item_quantity=DATA.PURCHASE_ITEM_QUANTITY,
                                     purchase_item_discount=DATA.PURCHASE_ITEM_DISCOUNT,
                                     purchase_item_shipping=DATA.PURCHASE_SHIPPING,
                                     purchase_item_vat_percent=DATA.PURCHASE_VAT_PERCENT)
    purchase.complete_purchase_invoice(purchase_inv_number=DATA.PURCHASE_INVOICE_NUMBER)
    print("OK: Create a purchase invoice")

    # Verify transaction history entry
    transaction = TransactionHistoryPage(browser)
    transaction.check_entry(account_head="Purchase", transaction_type="Due", amount=DATA.PURCHASE_INVOICE_TOTAL)
    print("OK: transaction history entry")

    # Verify Account Payable Entry
    payable = AccountPayablePage(browser)
    payable.check_entry(supplier_name=DATA.supplier_name,
                        total_purchase=DATA.PURCHASE_INVOICE_TOTAL,
                        total_paid=0,
                        total_due=DATA.PURCHASE_INVOICE_TOTAL)
    print("OK: Account Payable Entry")

    # Verify Stock Summary stock update
    stock = StockSummaryPage(browser)
    stock.check_stock(item_name=DATA.item_name,
                      purchase=DATA.PURCHASE_ITEM_QUANTITY,
                      sale=0,
                      purchase_return=0,
                      sales_return=0,
                      available_stock=DATA.PURCHASE_ITEM_QUANTITY)
    print("OK: Stock Summary stock update")

    # Verify income_statement
    income_statement = IncomeStatementPage(browser)
    # print("{:.2f}".format(DATA.PURCHASE_INVOICE_SUBTOTAL*(1+DATA.PURCHASE_VAT_PERCENT)/10))
    income_statement.check_income_statement(
        total_purchase="{:.2f}".format(DATA.PURCHASE_INVOICE_SUBTOTAL * (1 + DATA.PURCHASE_VAT_PERCENT) / 10),
        purchase_shipping_charge=DATA.PURCHASE_SHIPPING,
        total_cost_of_purchase=DATA.PURCHASE_INVOICE_TOTAL,
        gross_profit=DATA.PURCHASE_INVOICE_TOTAL * (-1),
        operation_income=DATA.PURCHASE_INVOICE_TOTAL * (-1),
        net_profit=DATA.PURCHASE_INVOICE_TOTAL * (-1))
    print("OK: income_statement")

    # TODO: Create a sales invoice

    # TODO: Create


def test_temp(browser):
    # Verify income_statement
    income_statement = IncomeStatementPage(browser)
    # print("{:.2f}".format(DATA.PURCHASE_INVOICE_SUBTOTAL*(1+DATA.PURCHASE_VAT_PERCENT)/10))
    income_statement.check_income_statement(total_purchase="{:.2f}".format(DATA.PURCHASE_INVOICE_SUBTOTAL*(1+DATA.PURCHASE_VAT_PERCENT)/10),
                                            purchase_shipping_charge=DATA.PURCHASE_SHIPPING,
                                            total_cost_of_purchase=DATA.PURCHASE_INVOICE_TOTAL,
                                            gross_profit=DATA.PURCHASE_INVOICE_TOTAL*(-1),
                                            operation_income=DATA.PURCHASE_INVOICE_TOTAL*(-1),
                                            net_profit=DATA.PURCHASE_INVOICE_TOTAL*(-1))
    print("OK: income_statement")