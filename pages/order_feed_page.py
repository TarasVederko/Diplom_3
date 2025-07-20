import allure
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage

class OrderFeedPage(BasePage):

    @allure.step('Ждем загрузку ленты с заказами')
    def wait_for_order_feed(self):
        self.wait_for_element(OrderFeedPageLocators.ORDER_FEED)

    @allure.step('Получаем текст загловка Лента заказов')
    def get_text_title_order_feed(self):
        return self.get_text_on_element(OrderFeedPageLocators.ORDER_FEED_TITLE)

    @allure.step('Получем значение счетчика заказов за все время')
    def get_value_full_time_orders_counter(self):
        return int(self.get_text_on_element(OrderFeedPageLocators.COUNTER_ORDERS_FULL_TIME))

    @allure.step('Получем значение счетчика заказов за сегодня')
    def get_value_today_orders_counter(self):
        return int(self.get_text_on_element(OrderFeedPageLocators.COUNTER_ORDERS_TODAY))

    @allure.step('Получаем номер заказа в списке В работе на странице Лента заказов')
    def get_number_of_order_in_order_feed_in_progress(self):
        return self.get_text_on_element(OrderFeedPageLocators.ORDER_FEED_IN_PROGRESS)

    @allure.step('Получаем номер заказа в окне подтверждения')
    def get_order_id_from_details(self):
        self.find_and_wait_until_text_changes(OrderFeedPageLocators.ORDER_NUMBER_IN_CONFORMATION_WINDOW, "9999")
        return self.get_text_on_element(OrderFeedPageLocators.ORDER_NUMBER_IN_CONFORMATION_WINDOW)
