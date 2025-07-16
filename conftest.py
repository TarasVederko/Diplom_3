import pytest
from selenium import webdriver
from url import *


@pytest.fixture
def driver(request):
    browser = request.param
    if browser == 'driver_chrom':
        driver = webdriver.Chrome()
    elif browser == 'driver_fox':
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.get(main_site)
    yield driver
    driver.quit()