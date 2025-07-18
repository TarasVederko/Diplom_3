import time

import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage
from conftest import *
from data.account_data import *

class TestOrderFeedPage:

    @pytest.mark.parametrize('driver', ['driver_chrom', 'driver_fox'], indirect=True)
    @allure.title('Тестируем при создании нового заказа счетчик заказов за все время обновляется ')
    def test_increasing_orders_counter_full_time(self, driver):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Логинимся в системе'):
            personal_account_page.entrance_in_personal_account(EMAIL, PASSWORD)

        with allure.step('Заходим в ленту заказов'):
            main_page.click_on_order_feed_button()

        with allure.step('Получаем значение счетчика заказов за все время и превращаем его в цифру'):
            current_value_counter = order_feed_page.get_value_full_time_orders_counter()

        with allure.step('Переходим в коструктор'):
            main_page.click_on_constructor_button()

        with allure.step('Добавляем булку'):
            main_page.add_bun_into_constractor()

        with allure.step('Кликаем по кнопке оформить заказ'):
            main_page.click_make_order()

        with allure.step('Закрываем окно подтверждения заказа'):
            main_page.close_conformation_order_window()

        with  allure.step('Заходим в ленту заказов'):
            main_page.click_on_order_feed_button()

        with allure.step('Получаме значение счетчика заказов за все время, превращаем его в цифру'):
            new_value_counter = order_feed_page.get_value_full_time_orders_counter()

        with allure.step('Проверям, что счетик заказов за все время увеличился'):
            assert new_value_counter > current_value_counter

    @pytest.mark.parametrize('driver', ['driver_chrom', 'driver_fox'], indirect=True)
    @allure.title('Тестируем при создании нового заказа счетчик заказов за все сегодня обновляется ')
    def test_increasing_orders_counter_today(self, driver):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Логинимся в системе'):
            personal_account_page.entrance_in_personal_account(EMAIL, PASSWORD)

        with allure.step('Заходим в ленту заказов'):
            main_page.click_on_order_feed_button()

        with allure.step('Получаем значение счетчика заказов за сегодня и превращаем его в цифру'):
            current_value_counter = order_feed_page.get_value_today_orders_counter()

        with allure.step('Переходим в коструктор'):
            main_page.click_on_constructor_button()

        with allure.step('Добавляем булку'):
            main_page.add_bun_into_constractor()

        with allure.step('Кликаем по кнопке оформить заказ'):
            main_page.click_make_order()

        with allure.step('Закрываем окно подтверждения заказа'):
            main_page.close_conformation_order_window()

        with  allure.step('Заходим в ленту заказов'):
            main_page.click_on_order_feed_button()

        with allure.step('Получаме значение счетчика заказов за все время, превращаем его в цифру'):
            new_value_counter = order_feed_page.get_value_today_orders_counter()

        with allure.step('Проверям, что счетик заказов за все время увеличился'):
            assert new_value_counter > current_value_counter


    @pytest.mark.parametrize('driver', ['driver_chrom', 'driver_fox'], indirect=True)
    @allure.title('Тестируем новый заказ отображается в спике В работе в окне Лента заказов')
    def test_add_orders_to_feed_in_progress(self, driver):
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Логинимся в системе'):
            personal_account_page.entrance_in_personal_account(EMAIL, PASSWORD)

        with allure.step('Добавляем булку'):
            main_page.add_bun_into_constractor()

        with allure.step('Кликаем по кнопке оформить заказ'):
            main_page.click_make_order()

        with allure.step('Получаем номер заказа'):
            order_number = order_feed_page.get_order_id_from_details()

        with allure.step('Закрываем окно подтвердения заказа'):
            main_page.close_conformation_order_window()

        with  allure.step('Заходим в ленту заказов'):
            main_page.click_on_order_feed_button()

        with allure.step('Получаем номер'):
            order_number_in_progress = order_feed_page.get_number_of_order_in_order_feed_in_progress()

        with allure.step('Проверяем что номер созданнго заказа отображается в блоке В работе'):
            assert order_number in order_number_in_progress
