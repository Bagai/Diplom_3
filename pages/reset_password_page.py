from .base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators
import allure


class ResetPasswordPage(BasePage):

    @allure.step('Check if element enter code is visible')
    def is_elemnt_enter_code_is_visible(self):
        self.check_element_is_displayed(
            ResetPasswordPageLocators.LABEL_CODE_FIELD_XPATH
        )
