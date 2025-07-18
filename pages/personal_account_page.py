import allure
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from url import *

class PersonalAccountPage(BasePage):

    def open_login_page(self):
        self.navigate_to(login_url)

    @allure.step('Логинимся в системе')
    def entrance_in_personal_account(self, email, password):
        self.open_login_page()
        self.send_keys_to_input(PersonalAccountPageLocators.EMAIL_INPUT_FIELD, email)
        self.send_keys_to_input(PersonalAccountPageLocators.PASSWORD_INPUT_FIELD, password)
        self.click_on_element(PersonalAccountPageLocators.ENTRANCE_BUTTON)
        self.wait_for_element(MainPageLocators.INGREDIENTS_MENU)
