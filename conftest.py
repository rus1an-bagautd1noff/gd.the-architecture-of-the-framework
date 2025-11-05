import pytest
from selenium import webdriver
from ExpendedSearchUI import Search


@pytest.fixture(scope="function")
def driver():
    driver_instance = webdriver.Chrome()
    yield driver_instance
    driver_instance.quit()


@pytest.fixture(scope="function")
def search(driver):
    search_instance = Search(driver)
    return search_instance
