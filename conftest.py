import pytest
from selenium import webdriver
from urllib3 import request

from url import *


@pytest.fixture(params=['driver_chrom', 'driver_fox'])
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