
class DATA:

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
