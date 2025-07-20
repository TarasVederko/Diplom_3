import allure
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from url import *

class PersonalAccountPage(BasePage):

    @allure.step('переходим на страницу входа в личный кабинет')
    def open_login_page(self):
        self.navigate_to(login_url)

    @allure.step('Логинимся в системе')
    def entrance_in_personal_account(self, email, password):

        with allure.step('Открываем страницу входа в личный кабинет'):
            self.open_login_page()

        with allure.step('Заполняем поле email'):
            self.send_keys_to_input(PersonalAccountPageLocators.EMAIL_INPUT_FIELD, email)

        with allure.step('Заполняем поле пароль'):
            self.send_keys_to_input(PersonalAccountPageLocators.PASSWORD_INPUT_FIELD, password)

        with allure.step('Кликаем на кнопку Войти'):
            self.click_on_element(PersonalAccountPageLocators.ENTRANCE_BUTTON)

        with allure.step('Ждем пока загрузится меню с булками/соусами/начинками'):
            self.wait_for_element(MainPageLocators.INGREDIENTS_MENU)
