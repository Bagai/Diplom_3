from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import allure


class LoginPage(BasePage):

    @allure.step('Fill in email field')
    def fill_in_email_field(self, email):
        self.add_text_to_element(LoginPageLocators.EMAIL_FIELD_XPATH, email)

    @allure.step('Fill in password field')
    def fill_in_password_field(self, password):
        self.add_text_to_element(
            LoginPageLocators.PASSWORD_FIELD_NOT_ACTIVE_XPATH, password
        )

    @allure.step('Click on button login')
    def click_on_button_login(self):
        self.click_element(LoginPageLocators.BUTTON_ENTER_XPATH)

    @allure.step('Click on button restore password')
    def click_on_button_restore_password(self):
        self.click_element(LoginPageLocators.BUTTON_RESTORE_PASSWORD_XPATH)

    @allure.step('Click on button show/hide password')
    def click_on_button_show_hide_password(self):
        self.click_element(LoginPageLocators.BUTTON_SHOW_HIDE_PASSWORD_XPATH)

    @allure.step('Check if password field is active')
    def is_password_field_active(self):
        return self.find_element_with_wait(
            LoginPageLocators.BUTTON_SHOW_HIDE_PASSWORD_XPATH
        )
    @allure.step('Check if restore password button is displayed')
    def is_restore_password_button_displayed(self):
        return self.find_element_with_wait(LoginPageLocators.BUTTON_RESTORE_PASSWORD_XPATH)
