from selenium.webdriver.common.by import By

class MainPageLocators:

    # кнопка "Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")

    # блок с инградиентами для бургеров
    INGREDIENTS_MENU = (By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")

    # кнопка Булки в меню инградиентов
    BUN_BUTTON_IN_INGREDIENTS_MENU = (By.XPATH, "//span[text()='Булки']")

    # кнопка Соусы в меню инградиентов
    SAUCE_BUTTON_IN_INGREDIENTS_MENU = (By.XPATH, "//span[text()='Соусы']")

    # кнопка Начинки в меню инградиентов
    FILLING_BUTTON_IN_INGREDIENTS_MENU = (By.XPATH, "//span[text()='Начинки']")

    # Флюоресцентная булка R2-D3
    BUN_R2_D3 = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")

    # Краторная булка N-200i
    BUN_N_200I = (By.XPATH, "//img[@alt='Краторная булка N-200i']")

    # Соус Spicy-X
    SAUCE_SPICY_X = (By.XPATH, "//img[@alt='Соус Spicy-X']")

    # Соус фирменный Space Sauce
    SAUCE_SPACE_SAUCE = (By.XPATH, "//img[@alt='Соус фирменный Space Sauce']")

    # Мясо бессмертных моллюсков Protostomia
    FILLING_PROSTOMIA = (By.XPATH, "//img[@alt='Мясо бессмертных моллюсков Protostomia']")

    # Филе Люминесцентного тетраодонтимформа
    FILLING_CHOP = (By.XPATH, "//img[@alt='Филе Люминесцентного тетраодонтимформа']")

    # Окно Детали инградиента
    WINDOW_DETAIL_INGREDIENT = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")

    # Загловок Детали инградиента
    TITLE_DETAIL_INGREDIENT = (By.XPATH, "//h2[text()='Детали ингредиента']")

    # Кресик в окне детали инградиента и подтверждения оформления заказа
    CLOSE_BUTTON_DETAIL_INGREDIENT = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")

    # кнопка "Лента заказов"
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")

    # кнопка Офорить заказ
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Перетяните булочку сюда (верх)
    CONSTRUCTOR_ELEMENT = (By.XPATH, "//img[@alt='Перетяните булочку сюда (верх)']")

    # кнопка личный кабинет
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

    # текст иденитфикатор заказа в окне после оформления заказа
    ORDER_ID_IN_CONFORMATION_WINDOW = (By.XPATH, "//p[text()='идентификатор заказа']")

    # загловок Соберите бургер у кноструктора
    TITLE_CONSTRUCT_BURGER = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")

    # счетик инградиента
    INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")

    # крестик в окне подтверждения оформления заказа
    CLOSE_BUTTON_CONFORMATION_ORDER = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")

    # невидимое окно
    OVERLAY = (By.XPATH, "//*[contains(@class, 'Modal_modal_overlay')]")

    #номер заказа
    TITLE_CONFORMATION_ORDER = (By.CLASS_NAME, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')

