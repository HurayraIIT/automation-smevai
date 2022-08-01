import time

from Pages.TradingCompany.accountPayablePage import AccountPayablePage
from Pages.TradingCompany.accountReceivablePage import AccountReceivablePage
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
    category.create_category(cat_name=DATA.CAT1_NAME)
    print("OK: Create a category")

    # DONE: Create an item
    item = ItemPage(browser)
    item.load_create_page()
    item.create_item(item_name=DATA.ITEM1_NAME,
                     cat_name=DATA.CAT1_NAME,
                     item_sku=DATA.ITEM1_SKU,
                     item_purchase_price=DATA.ITEM1_PURCHASE_PRICE,
                     item_sales_price=DATA.ITEM1_SALES_PRICE,
                     item_description=DATA.ITEM1_DESCRIPTION)
    print("OK: Create an item")

    # DONE: Create a supplier
    supplier = SupplierPage(browser)
    supplier.load_create_page()
    supplier.create_supplier(supplier_name=DATA.SUPPLIER1_NAME,
                             supplier_phone=DATA.SUPPLIER1_PHONE)
    print("OK: Create a supplier")

    # DONE: Create a customer
    customer = CustomerPage(browser)
    customer.load_create_page()
    customer.create_customer(customer_name=DATA.CUSTOMER1_NAME,
                             customer_phone=DATA.CUSTOMER1_PHONE)
    print("OK: Create a customer")

    # DONE: Create a purchase invoice
    purchase = PurchaseInvoicePage(browser)
    purchase.create_purchase_invoice(purchase_inv_number=DATA.PINV1_INVOICE_NUMBER,
                                     purchase_item_quantity=DATA.PINV1_ITEM_QUANTITY,
                                     purchase_item_discount=DATA.PINV1_ITEM_DISCOUNT,
                                     purchase_item_shipping=DATA.PINV1_SHIPPING,
                                     purchase_item_vat_percent=DATA.PINV1_VAT_PERCENT)
    purchase.complete_purchase_invoice(purchase_inv_number=DATA.PINV1_INVOICE_NUMBER)
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
        TOTAL_SALES=DATA.IS1_TOTAL_SALES,
        SALES_RETURN=DATA.IS1_SALES_RETURN,
        NET_SALES=DATA.IS1_NET_SALES,
        TOTAL_PURCHASE=DATA.IS1_TOTAL_PURCHASE,
        PURCHASE_RETURN=DATA.IS1_PURCHASE_RETURN,
        PURCHASE_SHIPPING_CHARGE=DATA.IS1_PURCHASE_SHIPPING_CHARGE,
        TOTAL_COST_OF_PURCHASE=DATA.IS1_TOTAL_COST_OF_PURCHASE,
        GROSS_PROFIT=DATA.IS1_GROSS_PROFIT,
        TOTAL_OPERATION_EXPENSES=DATA.IS1_TOTAL_OPERATION_EXPENSES,
        OPERATION_INCOME=DATA.IS1_OPERATION_INCOME,
        SALES_SHIPPING_CHARGE=DATA.IS1_SALES_SHIPPING_CHARGE,
        TOTAL_NON_OPERATION_INCOME=DATA.IS1_TOTAL_NON_OPERATION_INCOME,
        NET_PROFIT=DATA.IS1_NET_PROFIT)

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
    dashboard1.check_dashboard(total_order=DATA.DB1_TOTAL_ORDER,
                               avg_order_value=DATA.DB1_AVG_ORDER_VALUE,
                               cash_in_hand=DATA.DB1_CASH_IN_HAND,
                               total_stock=DATA.DB1_TOTAL_STOCK)

    # DONE: Create a sales invoice
    sales = SalesInvoicePage(browser)
    sales.create_sales_invoice(sales_inv_number=DATA.SINV1_INVOICE_NUMBER,
                               sales_item_quantity=DATA.SINV1_ITEM_QUANTITY,
                               sales_item_discount=DATA.SINV1_ITEM_DISCOUNT,
                               sales_item_shipping=DATA.SINV1_SHIPPING,
                               sales_item_vat_percent=DATA.SINV1_VAT_PERCENT)
    sales.complete_sales_invoice(sales_inv_number=DATA.SINV1_INVOICE_NUMBER)
    print("OK: Create a sales invoice")

    # DONE: Verify transaction history entry
    transaction2 = TransactionHistoryPage(browser)
    transaction2.check_entry(account_head=DATA.TH2_ACCOUNT_HEAD,
                             transaction_type=DATA.TH2_TRANSACTION_TYPE,
                             amount=DATA.TH2_AMOUNT)
    print("OK: transaction history entry")

    # DONE: Verify Account Receivable Entry
    receivable2 = AccountReceivablePage(browser)
    receivable2.check_entry(customer_name=DATA.AR2_SUPPLIER_NAME,
                            total_sale=DATA.AR2_TOTAL_SELL,
                            total_received=DATA.AR2_TOTAL_RECEIVED,
                            total_due=DATA.AR2_TOTAL_DUE)
    print("OK: Account Receivable Entry")

    # DONE: Verify Stock Summary stock update
    stock2 = StockSummaryPage(browser)
    stock2.check_stock(item_name=DATA.SS2_ITEM_NAME,
                       purchase=DATA.SS2_PURCHASE_QTY,
                       sale=DATA.SS2_SALE_QTY,
                       purchase_return=DATA.SS2_PURCHASE_RETURN_QTY,
                       sales_return=DATA.SS2_SALES_RETURN_QTY,
                       available_stock=DATA.SS2_AVAILABLE_STOCK_QTY)
    print("OK: Stock Summary stock update")

    # DONE: Verify income_statement
    income_statement2 = IncomeStatementPage(browser)
    income_statement2.check_income_statement(
        TOTAL_SALES=DATA.IS2_TOTAL_SALES,
        SALES_RETURN=DATA.IS2_SALES_RETURN,
        NET_SALES=DATA.IS2_NET_SALES,
        TOTAL_PURCHASE=DATA.IS2_TOTAL_PURCHASE,
        PURCHASE_RETURN=DATA.IS2_PURCHASE_RETURN,
        PURCHASE_SHIPPING_CHARGE=DATA.IS2_PURCHASE_SHIPPING_CHARGE,
        TOTAL_COST_OF_PURCHASE=DATA.IS2_TOTAL_COST_OF_PURCHASE,
        GROSS_PROFIT=DATA.IS2_GROSS_PROFIT,
        TOTAL_OPERATION_EXPENSES=DATA.IS2_TOTAL_OPERATION_EXPENSES,
        OPERATION_INCOME=DATA.IS2_OPERATION_INCOME,
        SALES_SHIPPING_CHARGE=DATA.IS2_SALES_SHIPPING_CHARGE,
        TOTAL_NON_OPERATION_INCOME=DATA.IS2_TOTAL_NON_OPERATION_INCOME,
        NET_PROFIT=DATA.IS2_NET_PROFIT)
    print("OK: income_statement")

    # DONE: Verify Balance Sheet
    balance_sheet2 = BalanceSheetPage(browser)
    balance_sheet2.check_balance_sheet(
        cash_wallet=DATA.BS2_CASH_WALLET_BALANCE,
        bank_wallet=DATA.BS2_BANK_WALLET_BALANCE,
        mobile_banking=DATA.BS2_MOBILE_BANKING_BALANCE,
        account_receivable=DATA.BS2_ACCOUNT_RECEIVABLE,
        inventory=DATA.BS2_INVENTORY,
        asset=DATA.BS2_ASSET,
        vat_amount=DATA.BS2_VAT_CURRENT_AMOUNT,
        total_asset=DATA.BS2_TOTAL_ASSET,
        owners_equity=DATA.BS2_OWNERS_EQUITY,
        accounts_payable=DATA.BS2_ACCOUNTS_PAYABLE,
        total_liabilities=DATA.BS2_TOTAL_EQUITY_AND_LIABILITIES)
    print("OK: Balance Sheet")

    # DONE: Verify Dashboard Stock Update
    dashboard2 = DashboardPage(browser)
    dashboard2.check_dashboard(total_order=DATA.DB2_TOTAL_ORDER,
                               avg_order_value=DATA.DB2_AVG_ORDER_VALUE,
                               cash_in_hand=DATA.DB2_CASH_IN_HAND,
                               total_stock=DATA.DB2_TOTAL_STOCK)
    print("OK: Dashboard Stock Update")

    # DONE: Receive sales invoice payment
    sales = SalesInvoicePage(browser)
    sales.receive_sales_payment(sales_inv_number=DATA.SINV1_INVOICE_NUMBER,
                                description="sales invoice payment",
                                received_amount=DATA.SINV2_RECEIVED_AMOUNT,
                                receiving_wallet=DATA.SINV2_RECEIVING_WALLET)
    print("OK: Sales invoice payment received")


def test_temp(browser):
    # DONE: Receive sales invoice payment
    sales = SalesInvoicePage(browser)
    sales.receive_sales_payment(sales_inv_number=DATA.SINV1_INVOICE_NUMBER,
                                description="sales invoice payment",
                                received_amount=DATA.SINV2_RECEIVED_AMOUNT,
                                receiving_wallet=DATA.SINV2_RECEIVING_WALLET)
    print("OK: Sales invoice payment received")

# def fmt2(val):
#     s = f'{"{:,.2f}".format(val)}'
#     return s
#
#
# def test_temp2(browser):
#     print(fmt2(-0))
#     print(fmt2(-12))
#     print(fmt2(-120))
#     print(fmt2(-1209))
#     print(fmt2(-12098))
#     print(fmt2(-120987))
#     print(fmt2(-1209877))

