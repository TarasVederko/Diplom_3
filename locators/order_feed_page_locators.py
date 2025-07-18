from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    # заголовок лента заказов
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")

    # счетчик заказов за все время
    COUNTER_ORDERS_FULL_TIME = (By.XPATH, "//div[@class='undefined mb-15']//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")

    # счетчик заказов за сегодгя
    COUNTER_ORDERS_TODAY = (By.XPATH, "//div[not(@*)]//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")

    # непосредственно лента с заказами
    ORDER_FEED = (By.CLASS_NAME, "OrderFeed_orderFeed__2RO_j")

    # список заказов В работе
    ORDER_FEED_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[1]")

    # номер заказа в окне подтверждения заказа
    ORDER_NUMBER_IN_CONFORMATION_WINDOW = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
