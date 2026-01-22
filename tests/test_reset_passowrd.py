# import pytest
from data import (
    url_login_page,
    url_forgot_password_page,
    url_reset_password_page,
    email,
)
from pages.login_page import LoginPage
from pages.restore_password_page import RestorePasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestResetPassword:

    def test_click_restore_password_button_success(self, driver):
        loginPage = LoginPage(driver)
        loginPage.go_to_url(url_login_page)
        loginPage.click_on_button_restore_password()
        assert loginPage.get_url() == url_forgot_password_page

    def test_enter_email_and_click_restore_password_button_success(self, driver):
        restorePasswordPage = RestorePasswordPage(driver)
        restorePasswordPage.go_to_url(url_forgot_password_page)
        restorePasswordPage.fill_in_email_field(email)
        restorePasswordPage.click_on_button_restore_password()
        ResetPasswordPage(driver).is_elemnt_enter_code_is_visible()
        assert restorePasswordPage.get_url() == url_reset_password_page

    def test_click_restore_password_button_success(self, driver):
        loginPage = LoginPage(driver)
        loginPage.go_to_url(url_login_page)
        loginPage.click_on_button_show_hide_password()
        assert loginPage.is_password_field_active()
