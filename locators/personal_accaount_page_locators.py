from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    BUTTON_ORDER_HISTORY_XPATH = (
        By.XPATH,
        ".//a[text()='История заказов']",
    )
    BUTTON_LOGOUT_XPATH = (
        By.XPATH,
        ".//button[text()='Выход']",
    )
