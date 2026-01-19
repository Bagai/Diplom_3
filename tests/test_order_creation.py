# import pytest
from data import (
    url_login_page,
    url_forgot_password_page,
    url_reset_password_page,
    url_main_page,
    url_personal_account_page,
    url_order_history_page,
    url_order_feed_page,
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

import time


class TestResetPassword:

    # def test_open_constructor(self, driver):
    #     LoginPage(driver).go_to_url(url_login_page)
    #     HeaderPage(driver).click_on_button_constructor()
    #     assert driver.current_url == url_main_page

    # def test_open_order_feed(self, driver):
    #     LoginPage(driver).go_to_url(url_login_page)
    #     HeaderPage(driver).click_on_button_order_feed()
    #     assert driver.current_url == url_order_feed_page

    # def test_open_ingredients_details(self, driver):
    #     main_page = MainPage(driver)
    #     main_page.go_to_url(url_main_page)
    #     main_page.click_on_ingridient_bun()
    #     assert main_page.check_modal_window_is_displayed()

    # def test_close_ingredients_details(self, driver):
    #     main_page = MainPage(driver)
    #     main_page.go_to_url(url_main_page)
    #     main_page.click_on_ingridient_bun()
    #     main_page.click_close_modal_window_button()
    #     assert main_page.check_modal_window_is_displayed() == False

    # def test_counter_increase(self, driver):
    #     main_page = MainPage(driver)
    #     main_page.go_to_url(url_main_page)
    #     main_page.click_and_drag_ingridient_bun()
    #     assert main_page.check_counter_inreasing() == "2"

    # def test_auth_user_is_able_to_order(self, driver):
    #     login_page = LoginPage(driver)
    #     login_page.go_to_url(url_login_page)
    #     login_page.fill_in_email_field(email)
    #     login_page.fill_in_password_field(password)
    #     login_page.click_on_button_login()
    #     main_page = MainPage(driver)
    #     main_page.check_placing_order_button_is_displayed()
    #     main_page.click_and_drag_ingridient_bun()
    #     main_page.click_and_drag_ingridient_souce()
    #     main_page.click_and_drag_ingridient_filling()
    #     main_page.click_placing_order_button()
    #     assert main_page.check_modal_window_of_order_is_displayed()
    pass