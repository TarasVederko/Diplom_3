import allure
import pytest
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage
from data.titles import *
from conftest import *

class TestOrderFeedPage:

    @pytest.mark.parametrize('driver', ['driver_chrom', 'driver_fox'], indirect=True)
    @allure.title('Тестируем при создании нового заказа счетчик заказов за все время обновляется ')
    def test_increasing_orders_counter_full_time(self, driver):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Открываем окно входа в личный кабинет'):
            main_page.click_on_personal_account_button()

        with allure.step('Входим в личный кабинет'):
            personal_account_page.entrance_in_personal_account()

        with allure.step('Заходим в ленту заказов'):
            main_page.click_on_order_feed_button()

        with allure.step('Получаем значение счетчика заказов за все время и превращаем его в цифру'):
            current_value_counter = order_feed_page.get_value_full_time_orders_counter()

        with allure.step('Переходим в коструктор'):
            main_page.click_on_constructor_button()

        with allure.step('Создаем новый заказ'):
            main_page.drag_and_drop_ingredient()
            main_page.click_make_order()





