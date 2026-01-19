from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    LABEL_CODE_FIELD_XPATH = (
        By.XPATH,
        ".//label[text()='Введите код из письма']",
    )
    BUTTON_RESTORE_PASSWORD_XPATH = (
        By.XPATH,
        ".//button[text()='Восстановить']",
    )
