import allure
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage
from data.account_data import *
from locators.main_page_locators import MainPageLocators


class PersonalAccountPage(BasePage):

    @allure.step('Логинимся в системе')
    def entrance_in_personal_account(self):
        self.wait_for_element(PersonalAccountPageLocators.ENTRANCE_BUTTON)
        self.send_keys_to_input(PersonalAccountPageLocators.EMAIL_INPUT_FIELD, EMAIL)
        self.send_keys_to_input(PersonalAccountPageLocators.PASSWORD_INPUT_FIELD, PASSWORD)
        self.click_on_element(PersonalAccountPageLocators.ENTRANCE_BUTTON)
        self.wait_for_element(MainPageLocators.INGREDIENTS_MENU)
