
def fmt(val):
    return f'৳{"{:.2f}".format(val)}'


class LINKS:

    ROOT = "smevai.com"

    TESTING_SITE = "https://testing." + ROOT
    APP_SITE = "https://app." + ROOT
    APP_EMAIL = "abuhurayra183+tpta1@gmail.com"

    TRADING_EMAIL = "abuhurayra183+tpta1@gmail.com"
    SERVICE_EMAIL = "abuhurayra183+tpsa1@gmail.com"
    PASSWORD = "pass1234"

    # Which site do you want to test?
    SITE = TESTING_SITE
    # SITE = APP_SITE

    # Common Pages
    LOGIN_PAGE = SITE + "/login"
    REGISTER_PAGE = SITE + "/register?package=pro&coupon=trial100"
    FORGOT_PASSWORD_PAGE = SITE + "/password/reset"

    # Trading Company Pages

    DASHBOARD = SITE + "/dashboard"

    COMPANY_SETTINGS_PAGE = SITE + "/settings/company"
    INVOICE_SETTINGS_PAGE = SITE + "/settings/company/invoice/settings"
    MANAGE_USERS_PAGE = SITE + "/settings/manage-users"
    WORDPRESS_SETTINGS_PAGE = SITE + "/settings/wordpress"

    PRODUCT_CATEGORY_LIST_PAGE = SITE + "/product/category"
    PRODUCT_CATEGORY_CREATE_PAGE = SITE + "/product/category/create"

    ITEM_LIST_PAGE = SITE + "/product/item"
    ITEM_CREATE_PAGE = SITE + "/product/item/create"

    SUPPLIER_LIST_PAGE = SITE + "/purchase/supplier"
    SUPPLIER_CREATE_PAGE = SITE + "/purchase/supplier/create"

    CUSTOMER_LIST_PAGE = SITE + "/sales/customer"
    CUSTOMER_CREATE_PAGE = SITE + "/sales/customer/create"

    PURCHASE_INVOICE_LIST_PAGE = SITE + "/purchase/invoice"
    PURCHASE_INVOICE_CREATE_PAGE = SITE + "/purchase/invoice/create"

    SALES_INVOICE_LIST_PAGE = SITE + "/sales/invoice"
    SALES_INVOICE_CREATE_PAGE = SITE + "/sales/invoice/create"

    # Transaction
    TRANSACTION_HISTORY_PAGE = SITE + "/transaction/history"

    # Report
    ACCOUNT_PAYABLE_PAGE = SITE + "/report/account/payable"
    ACCOUNT_RECEIVABLE_PAGE = SITE + "/report/account/receivable"
    STOCK_SUMMARY_PAGE = SITE + "/report/stock-summary"
    INCOME_STATEMENT_PAGE = SITE + "/report/income-statement"
    CASH_BOOK_PAGE = SITE + "/report/cash-book"
    BALANCE_SHEET_PAGE = SITE + "/report/balance-sheet"


class DATA:
    # Category data
    CAT1_NAME = "cat001"

    # Item data
    ITEM1_NAME = "item001"
    ITEM1_SKU = "sk001"
    ITEM1_PURCHASE_PRICE = 100
    ITEM1_SALES_PRICE = 200
    ITEM1_DESCRIPTION = "item description"

    # Supplier
    SUPPLIER1_NAME = "supplier001"
    SUPPLIER1_PHONE = "1657887766"

    # Customer
    CUSTOMER1_NAME = "customer001"
    CUSTOMER1_PHONE = "1657887766"

    # PINV = Purchase invoice
    PINV1_INVOICE_NUMBER = "10000001"
    PINV1_ITEM_QUANTITY = 5
    PINV1_ITEM_DISCOUNT = 10
    PINV1_SHIPPING = 50
    PINV1_VAT_PERCENT = 10
    PINV1_INVOICE_SUBTOTAL = 450
    PINV1_INVOICE_TOTAL = 545

    # Purchase invoice creation check data
    # TH = Transaction History
    TH1_ACCOUNT_HEAD = "Purchase"
    TH1_TRANSACTION_TYPE = "Due"
    TH1_AMOUNT = fmt(PINV1_INVOICE_TOTAL)

    # AP = Account Payable
    AP1_SUPPLIER_NAME = SUPPLIER1_NAME
    AP1_TOTAL_PURCHASE = fmt(PINV1_INVOICE_TOTAL)
    AP1_TOTAL_PAID = fmt(0)
    AP1_TOTAL_DUE = fmt(PINV1_INVOICE_TOTAL)

    # SS = Stock Summary
    SS1_ITEM_NAME = ITEM1_NAME
    SS1_PURCHASE_QTY = str(PINV1_ITEM_QUANTITY)
    SS1_SALE_QTY = "0"
    SS1_PURCHASE_RETURN_QTY = "0"
    SS1_SALES_RETURN_QTY = "0"
    SS1_AVAILABLE_STOCK_QTY = str(PINV1_ITEM_QUANTITY)

    # IS = Income Statement
    IS1_TOTAL_SALES	= fmt(0)
    IS1_SALES_RETURN = fmt(0)
    IS1_NET_SALES = fmt(0)
    IS1_TOTAL_PURCHASE = fmt(PINV1_INVOICE_SUBTOTAL * (1 + PINV1_VAT_PERCENT) / 10)
    IS1_PURCHASE_RETURN = fmt(0)
    IS1_PURCHASE_SHIPPING_CHARGE = fmt(PINV1_SHIPPING)
    IS1_TOTAL_COST_OF_PURCHASE = fmt(PINV1_INVOICE_TOTAL)
    IS1_GROSS_PROFIT = fmt(PINV1_INVOICE_TOTAL * (-1))
    IS1_TOTAL_OPERATION_EXPENSES = fmt(0)
    IS1_OPERATION_INCOME = fmt(PINV1_INVOICE_TOTAL * (-1))
    IS1_SALES_SHIPPING_CHARGE = fmt(0)
    IS1_TOTAL_NON_OPERATION_INCOME = fmt(0)
    IS1_NET_PROFIT = fmt(PINV1_INVOICE_TOTAL * (-1))

    # BS = Balance Sheet
    BS1_CASH_WALLET_BALANCE = fmt(0)
    BS1_BANK_WALLET_BALANCE = fmt(0)
    BS1_MOBILE_BANKING_BALANCE = fmt(0)
    BS1_ACCOUNT_RECEIVABLE = fmt(0)
    BS1_INVENTORY = fmt(ITEM1_PURCHASE_PRICE * PINV1_ITEM_QUANTITY)
    BS1_ASSET = fmt(0)
    BS1_VAT_CURRENT_AMOUNT = fmt((PINV1_VAT_PERCENT / 100) * PINV1_INVOICE_SUBTOTAL)
    BS1_TOTAL_ASSET = fmt(PINV1_INVOICE_TOTAL)

    BS1_OWNERS_EQUITY = fmt(0)
    BS1_ACCOUNTS_PAYABLE = fmt(PINV1_INVOICE_TOTAL)
    BS1_TOTAL_EQUITY_AND_LIABILITIES = fmt(PINV1_INVOICE_TOTAL)

    # Sales invoice
    SINV1_INVOICE_NUMBER = "10000001"
    SINV1_ITEM_QUANTITY = 5
    SINV1_ITEM_DISCOUNT = 10
    SINV1_SHIPPING = 100
    SINV1_VAT_PERCENT = 10
    SINV1_INVOICE_SUBTOTAL = 900
    SINV1_INVOICE_TOTAL = 1090
