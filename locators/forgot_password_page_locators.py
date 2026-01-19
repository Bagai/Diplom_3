from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    INPUT_EMAIL_ADRESS_XPATH = (
        By.XPATH,
        ".//div[contains(@class, 'input_type_text')]/input[contains(@class, 'text_type_main-default')]",
    )
    BUTTON_RESTORE_PASSWORD_XPATH = (
        By.XPATH,
        ".//button[text()='Восстановить']",
    )
