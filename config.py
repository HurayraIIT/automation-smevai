
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


class DATA:
    # Category data
    cat_name = "cat001"

    # Item data
    item_name = "item001"
    item_sku = "sk001"
    item_purchase_price = 100
    item_sales_price = 200
    item_description = "item description"

    # Supplier
    supplier_name = "supplier001"
    supplier_phone = "1657887766"

    # Customer
    customer_name = "customer001"
    customer_phone = "1657887766"

    # Purchase invoice
    PURCHASE_INVOICE_NUMBER = "10000001"
    PURCHASE_ITEM_QUANTITY = 5
    PURCHASE_ITEM_DISCOUNT = 10
    PURCHASE_SHIPPING = 50
    PURCHASE_VAT_PERCENT = 10
    PURCHASE_INVOICE_SUBTOTAL = 450
    PURCHASE_INVOICE_TOTAL = 545

    # Sales invoice
    SALES_INVOICE_NUMBER = "10000001"
    SALES_ITEM_QUANTITY = 5
    SALES_ITEM_DISCOUNT = 10
    SALES_SHIPPING = 100
    SALES_VAT_PERCENT = 10
    SALES_INVOICE_SUBTOTAL = 900
    SALES_INVOICE_TOTAL = 1090
