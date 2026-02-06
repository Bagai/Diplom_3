from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as ex
import allure

# import allure


class MainPage(BasePage):

    @allure.step('Click on close modal window button')
    def click_close_modal_window_button(self):
        self.click_element(MainPageLocators.BUTTON_CLOSE_MODAL_XPATH)

    @allure.step('Click on ingridient bun')
    def click_on_ingridient_bun(self):
        self.click_element(MainPageLocators.INGRIDIENTS_BUN_XPATH)

    @allure.step('Click on ingridient sauce')
    def click_on_ingridient_sauce(self):
        self.click_element(MainPageLocators.INGRIDIENTS_SOUCE_XPATH)

    @allure.step('Click on ingridient filling')
    def click_on_ingridient_filling(self):
        self.click_element(MainPageLocators.INGRIDIENTS_FILLING_XPATH)

    @allure.step('Click and drag ingridient bun')
    def click_and_drag_ingridient_bun(self):
        self.drag_and_drop(
            MainPageLocators.INGRIDIENTS_BUN_XPATH,
            MainPageLocators.BURGER_INGRIDIENTS_TO_ORDER_SECTION_XPATH,
        )

    @allure.step('Click and drag ingridient sauce')
    def click_and_drag_ingridient_souce(self):
        self.drag_and_drop(
            MainPageLocators.INGRIDIENTS_SOUCE_XPATH,
            MainPageLocators.BURGER_INGRIDIENTS_TO_ORDER_SECTION_XPATH,
        )

    @allure.step('Click and drag ingridient filling')
    def click_and_drag_ingridient_filling(self):
        self.drag_and_drop(
            MainPageLocators.INGRIDIENTS_FILLING_XPATH,
            MainPageLocators.BURGER_INGRIDIENTS_TO_ORDER_SECTION_XPATH,
        )

    @allure.step('Check counter increasing')
    def check_counter_inreasing(self):
        return self.get_element_text(MainPageLocators.INGRIDIENT_COUNTER_XPATH)

    @allure.step('Check placing order button is displayed')
    def check_placing_order_button_is_displayed(self):
        return self.check_element_is_displayed(
            MainPageLocators.BUTTON_PLACE_ORDER_XPATH
        )

    @allure.step('Click placing order button')
    def click_placing_order_button(self):
        return self.click_element(MainPageLocators.BUTTON_PLACE_ORDER_XPATH)

    @allure.step('Check modal window is displayed')
    def check_modal_window_is_displayed(self):
        return self.check_element_is_not_displayed(
            MainPageLocators.SECTION_IS_OPENNED_XPATH
        )

    @allure.step('Check modal window of order is displayed')
    def check_modal_window_of_order_is_displayed(self):
        return self.check_element_is_not_displayed(
            MainPageLocators.SECTION_ORDER_IS_OPENNED_XPATH
        )

    @allure.step('Click on close modal window of order with wait')
    def click_on_close_modal_window_of_order_with_wait(self):
        self.click_on_element_after_layout_hide(
            MainPageLocators.OVERLAY_XPATH, MainPageLocators.BUTTON_CLOSE_MODAL_XPATH
        )

    @allure.step('Click on close modal window of order')
    def click_on_close_modal_window_of_order(self):
        self.click_element(MainPageLocators.BUTTON_CLOSE_MODAL_XPATH)
