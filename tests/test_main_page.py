import allure
import pytest
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from data.titles import *
from conftest import *

class TestMainPage:

    @pytest.mark.parametrize('driver', ['driver_chrom', 'driver_fox'], indirect=True)
    @allure.title('Тестируем переход в кноструктор')
    def test_switch_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_feed_button()
        main_page.click_on_constructor_button()
        main_page.wait_for_ingredients_menu()
        result = main_page.get_text_on_title_constructor()
        assert result == TEXT_TITLE_CONSTRUCTOR, 'Не открылось меню с бургерами после нажатия кнопки Конструктор  в шапке'

    @pytest.mark.parametrize('driver', ['driver_chrom', 'driver_fox'], indirect=True)
    @allure.title('Тестируем переход в ленту заказов')
    def test_switch_to_order_feed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.click_on_order_feed_button()
        order_feed_page.wait_for_order_feed()
        result = order_feed_page.get_text_title_order_feed()
        assert result == TEXT_TITLE_ORDER_FEED

    @pytest.mark.parametrize('driver', ['driver_chrom', 'driver_fox'], indirect=True)
    @allure.title('Тестируем появление окна с деталями после клика на инградиент')
    def test_details_window_of_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun_r2_d3()
        main_page.wait_for_details_window()
        result = main_page.get_text_title_details_window()
        assert result == TEXT_TITLE_DETAIL_INGREDINET

    @pytest.mark.parametrize('driver', ['driver_chrom', 'driver_fox'], indirect=True)
    @allure.title('Тестируем закрытие окна детали инградиента кликом по крестику')
    def test_close_window_of_ingredient(self,driver):
        main_page = MainPage(driver)
        main_page.click_on_bun_n_200i()
        main_page.wait_for_details_window()
        main_page.click_on_cross_details_window()
        assert main_page.wait_details_window_disappear

    @pytest.mark.parametrize('driver', ['driver_chrom', 'driver_fox'], indirect=True)
    @allure.title('Тестируем при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается.')
    def test_increase_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        current_value = main_page.get_value_ingredient_counter()
        main_page.add_bun_into_constractor()
        new_value = main_page.get_value_ingredient_counter()
        assert new_value == current_value + 2
