from pages.Product_attribute import ProductAttribute
from pages.accounts import Accounts
from pages.login import Login


# def test_login(browser):
#     log = Login(browser)
#     log.load()
#     log.testcase()


# def test_add_product_attribute(browser):
#     product = ProductAttribute(browser)
#     product.add_attribute()
#
#
# def test_delete_product_attribute(browser):
#     product = ProductAttribute(browser)
#     product.delete_attribute()

def test_update_pass(browser):
    acc = Accounts(browser)
    acc.testcase()
