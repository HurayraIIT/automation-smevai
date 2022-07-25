import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='module')
def browser():
    opts = Options()
    path = f"/home/hurayra/GitHub/automation-smevai/webdrivers/chromedriver"
    driver = webdriver.Chrome(executable_path=path, chrome_options=opts)
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver
    # driver.close()
    # driver.quit()
    # print("Test Completed")