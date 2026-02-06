from selenium.webdriver.common.by import By


class LoginPageLocators:
    BUTTON_RESTORE_PASSWORD_XPATH = (
        By.XPATH,
        ".//a[text()='Восстановить пароль']",
    )
    BUTTON_SHOW_HIDE_PASSWORD_XPATH = (
        By.XPATH,
        ".//div[contains(@class, 'input__icon')]",
    )
    BUTTON_ENTER_XPATH = (
        By.XPATH,
        ".//button[text()='Войти']",
    )
    EMAIL_FIELD_XPATH = (
        By.XPATH,
        ".//div[contains(@class, 'input_type_text')]/input[contains(@class, 'text_type_main-default')]",
    )
    PASSWORD_FIELD_NOT_ACTIVE_XPATH = (
        By.XPATH,
        ".//div[contains(@class, 'input_type_password')]/input[contains(@type, 'password')]",
    )
    PASSWORD_FIELD_ACTIVE_FIELD_XPATH = (
        By.XPATH,
        ".//div[contains(@class, 'input_type_password', 'input_status_active')]/input[contains(@type, 'text')]",
    )
