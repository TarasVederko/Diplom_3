from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:

    # поле ввода email
    EMAIL_INPUT_FIELD = (By.XPATH, "//input[@name='name']")

    # поле ввода пароля
    PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@name='Пароль']")

    # кнопка войти
    ENTRANCE_BUTTON = (By.XPATH, "//button[text()='Войти']")
