import allure
import pytest
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from data.titles import *
from conftest import *

@allure.feature('Основной функционал')
@allure.story('Тесты функционала главной страницы')
class TestMainPage:

    @pytest.mark.parametrize('driver', ['driver_chrom', 'driver_fox'], indirect=True)
    @allure.title('Тестируем переход в кноструктор')
    def test_switch_to_constructor(self, driver):
        main_page = MainPage(driver)

        with allure.step('Кликаем по кнопке Лента заказов'):
            main_page.click_on_order_feed_button()

        with allure.step('Кликаем по кнопке конструктор'):
            main_page.click_on_constructor_button()

        with allure.step('Ждем появление меню с инградиентами'):
            main_page.wait_for_ingredients_menu()

        with allure.step('Проверям что по клику на кнопку конструктор происходит переход на главную страницу'):
            assert main_page.get_current_url() == main_site


    @pytest.mark.parametrize('driver', ['driver_chrom', 'driver_fox'], indirect=True)
    @allure.title('Тестируем переход в ленту заказов')
    def test_switch_to_order_feed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Кликаем на кнопку Лента заказов'):
            main_page.click_on_order_feed_button()

        with allure.step('Ждем загрузку заголова Лента заказа'):
            order_feed_page.wait_for_order_feed()

        with allure.step('Проверям что по клику на кнопку Лента заказов происходит переход на ленту заказов'):
            assert main_page.get_current_url() == orders_feed_url


    @pytest.mark.parametrize('driver', ['driver_chrom', 'driver_fox'], indirect=True)
    @allure.title('Тестируем появление окна с деталями после клика на инградиент')
    def test_details_window_of_ingredient(self, driver):
        main_page = MainPage(driver)

        with allure.step('Кликаеи на булочу Флюоресцентная булка R2-D3'):
            main_page.click_on_bun_r2_d3()

        with allure.step('Жде появление окна Детали инградиента'):
            main_page.wait_for_details_window()

        with allure.step('Проверяем что появилось окно с заголовком Детали инградиента'):
            assert main_page.get_text_title_details_window() == TEXT_TITLE_DETAIL_INGREDINET


    @pytest.mark.parametrize('driver', ['driver_chrom', 'driver_fox'], indirect=True)
    @allure.title('Тестируем закрытие окна детали инградиента кликом по крестику')
    def test_close_window_of_ingredient(self,driver):
        main_page = MainPage(driver)

        with allure.step('Кликаем на булку Краторная булка N-200i'):
            main_page.click_on_bun_n_200i()

        with allure.step('Жде пока загрузится окно Детали инградиента'):
            main_page.wait_for_details_window()

        with allure.step('Кликаем по крестику'):
            main_page.click_on_cross_details_window()

        with allure.step('Проверяем что окно закрылось'):
            assert main_page.wait_details_window_disappear() is True


    @pytest.mark.parametrize('driver', ['driver_chrom', 'driver_fox'], indirect=True)
    @allure.title('Тестируем при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается.')
    def test_increase_ingredient_counter(self, driver):
        main_page = MainPage(driver)

        with allure.step('Получаем текущее значение счетчика Флюоресцентной булки R2-D3'):
            current_value = main_page.get_value_ingredient_1_counter()

        with allure.step('Добавляем булку Флюоресцентная булка R2-D3'):
            main_page.add_bun_into_constractor()

        with allure.step('Получаем новое значение счетчика Флюоресцентной булки R2-D3'):
            new_value = main_page.get_value_ingredient_1_counter()

        with allure.step('Проверяем что счетчик Флюоресцентной булки R2-D3 увеличился на 2'):
            assert new_value == current_value + 2
