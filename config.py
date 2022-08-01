
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
    # SITE = TESTING_SITE
    SITE = APP_SITE

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
    CAT_NAME = "cat001"

    # Item data
    ITEM_NAME = "item001"
    ITEM_SKU = "sk001"
    ITEM_PURCHASE_PRICE = 100
    ITEM_SALES_PRICE = 200
    ITEM_DESCRIPTION = "item description"

    # Supplier
    SUPPLIER_NAME = "supplier001"
    SUPPLIER_PHONE = "1657887766"

    # Customer
    CUSTOMER_NAME = "customer001"
    CUSTOMER_PHONE = "1657887766"

    # Purchase invoice
    PURCHASE_INVOICE_NUMBER = "10000001"
    PURCHASE_ITEM_QUANTITY = 5
    PURCHASE_ITEM_DISCOUNT = 10
    PURCHASE_SHIPPING = 50
    PURCHASE_VAT_PERCENT = 10
    PURCHASE_INVOICE_SUBTOTAL = 450
    PURCHASE_INVOICE_TOTAL = 545

    # Purchase invoice creation check data
    # TH = Transaction History
    TH1_ACCOUNT_HEAD = "Purchase"
    TH1_TRANSACTION_TYPE = "Due"
    TH1_AMOUNT = fmt(PURCHASE_INVOICE_TOTAL)

    # AP = Account Payable
    AP1_SUPPLIER_NAME = SUPPLIER_NAME
    AP1_TOTAL_PURCHASE = fmt(PURCHASE_INVOICE_TOTAL)
    AP1_TOTAL_PAID = fmt(0)
    AP1_TOTAL_DUE = fmt(PURCHASE_INVOICE_TOTAL)

    # SS = Stock Summary
    SS1_ITEM_NAME = ITEM_NAME
    SS1_PURCHASE_QTY = str(PURCHASE_ITEM_QUANTITY)
    SS1_SALE_QTY = "0"
    SS1_PURCHASE_RETURN_QTY = "0"
    SS1_SALES_RETURN_QTY = "0"
    SS1_AVAILABLE_STOCK_QTY = str(PURCHASE_ITEM_QUANTITY)

    # IS = Income Statement
    IS1_TOTAL_SALES	= fmt(0)
    IS1_SALES_RETURN = fmt(0)
    IS1_NET_SALES = fmt(0)
    IS1_TOTAL_PURCHASE = fmt(PURCHASE_INVOICE_SUBTOTAL*(1+PURCHASE_VAT_PERCENT)/10)
    IS1_PURCHASE_RETURN = fmt(0)
    IS1_PURCHASE_SHIPPING_CHARGE = fmt(PURCHASE_SHIPPING)
    IS1_TOTAL_COST_OF_PURCHASE = fmt(PURCHASE_INVOICE_TOTAL)
    IS1_GROSS_PROFIT = fmt(PURCHASE_INVOICE_TOTAL * (-1))
    IS1_TOTAL_OPERATION_EXPENSES = fmt(0)
    IS1_OPERATION_INCOME = fmt(PURCHASE_INVOICE_TOTAL * (-1))
    IS1_SALES_SHIPPING_CHARGE = fmt(0)
    IS1_TOTAL_NON_OPERATION_INCOME = fmt(0)
    IS1_NET_PROFIT = fmt(PURCHASE_INVOICE_TOTAL * (-1))

    # BS = Balance Sheet
    BS1_CASH_WALLET_BALANCE = fmt(0)
    BS1_BANK_WALLET_BALANCE = fmt(0)
    BS1_MOBILE_BANKING_BALANCE = fmt(0)
    BS1_ACCOUNT_RECEIVABLE = fmt(0)
    BS1_INVENTORY = fmt(ITEM_PURCHASE_PRICE*PURCHASE_ITEM_QUANTITY)
    BS1_ASSET = fmt(0)
    BS1_VAT_CURRENT_AMOUNT = fmt((PURCHASE_VAT_PERCENT/100)*PURCHASE_INVOICE_SUBTOTAL)
    BS1_TOTAL_ASSET = fmt(PURCHASE_INVOICE_TOTAL)

    BS1_OWNERS_EQUITY = fmt(0)
    BS1_ACCOUNTS_PAYABLE = fmt(PURCHASE_INVOICE_TOTAL)
    BS1_TOTAL_EQUITY_AND_LIABILITIES = fmt(PURCHASE_INVOICE_TOTAL)

    # Sales invoice
    SALES_INVOICE_NUMBER = "10000001"
    SALES_ITEM_QUANTITY = 5
    SALES_ITEM_DISCOUNT = 10
    SALES_SHIPPING = 100
    SALES_VAT_PERCENT = 10
    SALES_INVOICE_SUBTOTAL = 900
    SALES_INVOICE_TOTAL = 1090
