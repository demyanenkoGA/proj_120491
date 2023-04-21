import pytest
from selenium import webdriver


@pytest.fixture()
def set_up():
    print("\nStart test\n")
    # driver = webdriver.Chrome()
    # url = 'https://www.saucedemo.com/'
    # driver.get(url)
    # driver.maximize_window()
    yield
    # driver.quit()
    print("\nFinish test\n")


@pytest.fixture(scope="module")
def set_group():
    print("\nEnter System\n")
    yield
    print("\nExit System\n")
