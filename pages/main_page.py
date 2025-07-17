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

    @allure.step('Кликаем по булочке Флюоресцентная булка R2-D3')
    def click_on_bun_r2_d3(self):
        self.click_on_element(MainPageLocators.BUN_R2_D3)

    @allure.step('Кликаем по булочке Краторная булка N-200i')
    def click_on_bun_n_200i(self):
        self.click_on_element(MainPageLocators.BUN_N_200I)

    @allure.step('Ждем появления окна с деталями инградиента')
    def wait_for_details_window(self):
        self.wait_for_element(MainPageLocators.WINDOW_DETAIL_INGREDIENT)

    @allure.step('Ждем пока окно с деталями исчезнет')
    def wait_details_window_disappear(self):
        self.wait_element_disappear(MainPageLocators.WINDOW_DETAIL_INGREDIENT)

    @allure.step('Получаем текс заголова окна детали инградиента')
    def get_text_title_details_window(self):
        return self.get_text_on_element(MainPageLocators.TITLE_DETAIL_INGREDIENT)

    @allure.step('Кликаем по крестику в окне детали инградента')
    def click_on_cross_details_window(self):
        self.click_on_element(MainPageLocators.CLOSE_BUTTON_DETAIL_INGREDIENT)

    @allure.step('Получаем значение счетчика инградиента')
    def get_value_ingredient_counter(self):
        return int(self.get_text_on_element(MainPageLocators.INGREDIENT_COUNTER))

    @allure.step('Добавляем булочку в заказ')
    def drag_and_drop_ingredient(self):
        ingredient_locator = MainPageLocators.BUN_R2_D3
        target_locator = MainPageLocators.CONSTRUCTOR_ELEMENT
        self.drag_and_drop(ingredient_locator, target_locator)
