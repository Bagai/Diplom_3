from selenium.webdriver.common.by import By


class HaderLocators:
    BUTTON_PERSONAL_ACCOUNT_XPATH = (
        By.XPATH,
        ".//p[text()='Личный Кабинет']",
    )
    BUTTON_CONSTRUCTOR_XPATH = (
        By.XPATH,
        ".//p[text()='Конструктор']",
    )
    BUTTON_ORDER_FEED_XPATH = (
        By.XPATH,
        ".//p[text()='Лента Заказов']",
    )
