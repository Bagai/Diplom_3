import pytest
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
from pages.order_feed_page import OrderFeedPage

import time


class TestResetPassword:

    # def test_open_order_details(self, driver):
    #     order_page = OrderFeedPage(driver)
    #     order_page.go_to_url(url_order_feed_page)
    #     order_page.click_on_order()
    #     assert order_page.check_modal_is_opened()

    def test_user_orders_displayes_at_order_feed(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_url(url_login_page)
        login_page.fill_in_email_field(email)
        login_page.fill_in_password_field(password)
        login_page.click_on_button_login()
        main_page = MainPage(driver)
        main_page.check_placing_order_button_is_displayed()
        main_page.click_and_drag_ingridient_bun()
        main_page.click_and_drag_ingridient_souce()
        main_page.click_and_drag_ingridient_filling()
        main_page.click_placing_order_button()
        main_page.check_modal_window_of_order_is_displayed()
        time.sleep(3)
        main_page.click_on_close_modal_window_of_order()
        header_page = HeaderPage(driver)
        header_page.click_on_button_personal_account()
        pa_page = PersonalAccountPage(driver)
        pa_page.click_history_button()
        order_history_page = OrderHistoryPage(driver)
        # order_history_page.go_to_url(url_order_history_page)
        number_of_order = order_history_page.get_order_number()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.go_to_url(url_order_feed_page)
        assert number_of_order in order_feed_page.get_order_number()
