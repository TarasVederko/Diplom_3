from selenium.webdriver.common.by import By

class PersonalAccountPage:

    # поле ввода email
    EMAIL_INPUT_FIELD = (By.XPATH, "//input[@name='name']")

    # поле ввода пароля
    PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@name='Пароль']")

    # кнопка войти
    ENTRANCE_BUTTON = (By.CLASS_NAME, "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa")
