import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем пока элемент становится видимым')
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Скролим до элемента')
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        return element

    @allure.step('Кликаем на элекмент')
    def click_on_element(self, locator, timeout=10):
        element = self.scroll_to_element(locator, timeout)
        element.click()

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text







