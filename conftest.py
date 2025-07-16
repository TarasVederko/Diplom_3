import pytest
from selenium import webdriver
from url import *


@pytest.fixture
def driver_chrom():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(main_site)

    yield driver
    driver.quit()

@pytest.fixture
def driver_fox():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(main_site)

    yield driver
    driver.quit()