import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.main_page_locators import MainPageLocators
from seletools.actions import drag_and_drop

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем пока элемент становится видимым')
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Скролим до элемента')
    def scroll_to_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        #element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step('Кликаем на элемент')
    def click_on_element(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(MainPageLocators.OVERLAY))
        except:
            pass
        element = self.scroll_to_element(locator, timeout)
        element.click()

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step('Ждем пока элемент исчезнет')
    def wait_element_disappear(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, text, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step('Переход по url')
    def navigate_to(self, url):
        self.driver.get(url)
