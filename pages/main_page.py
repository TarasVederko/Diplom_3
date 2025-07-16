import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Кликаем на кнопку Конструктор в шапке')
    def click_on_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликаем на кнопку Лента заказов в шапке')
    def click_on_order_feed_button(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Кликаем на кнопку Личный кабинет')
    def click_on_personal_account_button(self):
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Ждем загрузки меню инградиентов')
    def wait_for_ingredients_menu(self):
        self.wait_for_element(MainPageLocators.INGREDIENTS_MENU)

    @allure.step('Получаем текст загловка конструктора')
    def get_text_on_title_constructor(self):
        return self.get_text_on_element(MainPageLocators.TITLE_CONSTRUCT_BURGER)


