# import pytest
from data import (
    url_login_page,
    url_forgot_password_page,
    url_reset_password_page,
    url_main_page,
    url_personal_account_page,
    url_order_history_page,
    email,
    password,
)
from pages.login_page import LoginPage
from pages.restore_password_page import RestorePasswordPage
from pages.reset_password_page import ResetPasswordPage
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.order_history_page import OrderHistoryPage


class TestPersonalAccount:

    def test_open_personal_account(self, driver):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        main_page.go_to_url(url_main_page)
        header_page.click_on_button_personal_account()
        assert main_page.get_url() == url_login_page

    def test_open_order_history(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_url(url_login_page)
        login_page.fill_in_email_field(email)
        login_page.fill_in_password_field(password)
        login_page.click_on_button_login()
        HeaderPage(driver).click_on_button_personal_account()
        pa_page = PersonalAccountPage(driver)
        pa_page.click_history_button()
        assert pa_page.get_url() == url_order_history_page

    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_url(url_login_page)
        login_page.fill_in_email_field(email)
        login_page.fill_in_password_field(password)
        login_page.click_on_button_login()
        HeaderPage(driver).click_on_button_personal_account()
        PersonalAccountPage(driver).click_logout_button()
        LoginPage(driver).is_restore_password_button_displayed()
        assert login_page.get_url() == url_login_page
