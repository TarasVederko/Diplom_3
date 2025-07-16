import allure
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step('Ждем загрузку ленты с заказми')
    def wait_for_order_feed(self):
        self.wait_for_element(OrderFeedPageLocators.ORDER_FEED)

    @allure.step('Получаем текстзагловка Лента заказов')
    def get_text_title_order_feed(self):
        return self.get_text_on_element(OrderFeedPageLocators.ORDER_FEED_TITLE)