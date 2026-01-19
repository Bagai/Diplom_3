from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    ORDER_HISTORY_ORDER_NUMBER_ELEMENT_XPATH = (
        By.XPATH,
        ".//a/div/p[contains(text(), '#')]",
    )
    ORDER_HISTORY_MENU_XPATH = (
        By.XPATH,
        ".//a[contains(@class, 'Account_link_active') and text()='История заказов']",
    )
