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
        page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        page.click_on_order_feed_button()
        order_feed_page.wait_for_order_feed()
        result = order_feed_page.get_text_title_order_feed()
        assert result == TEXT_TITLE_ORDER_FEED





