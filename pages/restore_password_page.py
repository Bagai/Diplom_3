from .base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
import allure


class RestorePasswordPage(BasePage):

    @allure.step("Fill in email field")
    def fill_in_email_field(self, email):
        self.add_text_to_element(
            ForgotPasswordPageLocators.INPUT_EMAIL_ADRESS_XPATH, email
        )

    @allure.step("Click on button restore password")
    def click_on_button_restore_password(self):
        self.click_element(ForgotPasswordPageLocators.BUTTON_RESTORE_PASSWORD_XPATH)
