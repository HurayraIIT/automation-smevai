import time

from Pages.TradingCompany.accountPayablePage import AccountPayablePage
from Pages.TradingCompany.balanceSheetPage import BalanceSheetPage
from Pages.TradingCompany.incomeStatementPage import IncomeStatementPage
from Pages.TradingCompany.salesInvoicePage import SalesInvoicePage
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
    category.create_category(cat_name=DATA.CAT_NAME)
    print("OK: Create a category")

    # DONE: Create an item
    item = ItemPage(browser)
    item.load_create_page()
    item.create_item(item_name=DATA.ITEM_NAME,
                     cat_name=DATA.CAT_NAME,
                     item_sku=DATA.ITEM_SKU,
                     item_purchase_price=DATA.ITEM_PURCHASE_PRICE,
                     item_sales_price=DATA.ITEM_SALES_PRICE,
                     item_description=DATA.ITEM_DESCRIPTION)
    print("OK: Create an item")

    # DONE: Create a supplier
    supplier = SupplierPage(browser)
    supplier.load_create_page()
    supplier.create_supplier(supplier_name=DATA.SUPPLIER_NAME,
                             supplier_phone=DATA.SUPPLIER_PHONE)
    print("OK: Create a supplier")

    # DONE: Create a customer
    customer = CustomerPage(browser)
    customer.load_create_page()
    customer.create_customer(customer_name=DATA.CUSTOMER_NAME,
                             customer_phone=DATA.CUSTOMER_PHONE)
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
    transaction.check_entry(account_head=DATA.TH1_ACCOUNT_HEAD,
                            transaction_type=DATA.TH1_TRANSACTION_TYPE,
                            amount=DATA.TH1_AMOUNT)
    print("OK: transaction history entry")

    # Verify Account Payable Entry
    payable = AccountPayablePage(browser)
    payable.check_entry(supplier_name=DATA.AP1_SUPPLIER_NAME,
                        total_purchase=DATA.AP1_TOTAL_PURCHASE,
                        total_paid=DATA.AP1_TOTAL_PAID,
                        total_due=DATA.AP1_TOTAL_DUE)
    print("OK: Account Payable Entry")

    # Verify Stock Summary stock update
    stock = StockSummaryPage(browser)
    stock.check_stock(item_name=DATA.SS1_ITEM_NAME,
                      purchase=DATA.SS1_PURCHASE_QTY,
                      sale=DATA.SS1_SALE_QTY,
                      purchase_return=DATA.SS1_PURCHASE_RETURN_QTY,
                      sales_return=DATA.SS1_SALES_RETURN_QTY,
                      available_stock=DATA.SS1_AVAILABLE_STOCK_QTY)
    print("OK: Stock Summary stock update")

    # Verify income_statement
    income_statement = IncomeStatementPage(browser)
    income_statement.check_income_statement(
        total_purchase=DATA.IS1_TOTAL_PURCHASE,
        purchase_shipping_charge=DATA.IS1_PURCHASE_SHIPPING_CHARGE,
        total_cost_of_purchase=DATA.IS1_TOTAL_COST_OF_PURCHASE,
        gross_profit=DATA.IS1_GROSS_PROFIT,
        operation_income=DATA.IS1_OPERATION_INCOME,
        net_profit=DATA.IS1_NET_PROFIT)
    print("OK: income_statement")

    # Verify Balance Sheet
    balance_sheet = BalanceSheetPage(browser)
    balance_sheet.check_balance_sheet(
        cash_wallet=DATA.BS1_CASH_WALLET_BALANCE,
        bank_wallet=DATA.BS1_BANK_WALLET_BALANCE,
        mobile_banking=DATA.BS1_MOBILE_BANKING_BALANCE,
        account_receivable=DATA.BS1_ACCOUNT_RECEIVABLE,
        inventory=DATA.BS1_INVENTORY,
        asset=DATA.BS1_ASSET,
        vat_amount=DATA.BS1_VAT_CURRENT_AMOUNT,
        total_asset=DATA.BS1_TOTAL_ASSET,
        owners_equity=DATA.BS1_OWNERS_EQUITY,
        accounts_payable=DATA.BS1_ACCOUNTS_PAYABLE,
        total_liabilities=DATA.BS1_TOTAL_EQUITY_AND_LIABILITIES)
    print("OK: Balance Sheet")

    # Verify Dashboard Stock Update
    dashboard1 = DashboardPage(browser)
    dashboard1.check_dashboard(total_stock=DATA.PURCHASE_ITEM_QUANTITY)
    print("OK: Dashboard Stock Update")

    # TODO: Create a sales invoice

    # TODO: Create


def test_temp(browser):
    # DONE: Create a sales invoice
    sales = SalesInvoicePage(browser)
    sales.create_sales_invoice(sales_inv_number=DATA.SALES_INVOICE_NUMBER,
                               sales_item_quantity=DATA.SALES_ITEM_QUANTITY,
                               sales_item_discount=DATA.SALES_ITEM_DISCOUNT,
                               sales_item_shipping=DATA.SALES_SHIPPING,
                               sales_item_vat_percent=DATA.SALES_VAT_PERCENT)
    # sales.complete_sales_invoice(sales_inv_number=DATA.SALES_INVOICE_NUMBER)
    print("OK: Create a sales invoice")