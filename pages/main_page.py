from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as ex

# import allure


class MainPage(BasePage):

    def click_close_modal_window_button(self):
        self.click_element(MainPageLocators.BUTTON_CLOSE_MODAL_XPATH)

    def click_on_ingridient_bun(self):
        self.click_element(MainPageLocators.INGRIDIENTS_BUN_XPATH)

    def click_on_ingridient_sauce(self):
        self.click_element(MainPageLocators.INGRIDIENTS_SOUCE_XPATH)

    def click_on_ingridient_filling(self):
        self.click_element(MainPageLocators.INGRIDIENTS_FILLING_XPATH)

    def click_and_drag_ingridient_bun(self):
        self.drag_and_drop(
            MainPageLocators.INGRIDIENTS_BUN_XPATH,
            MainPageLocators.BURGER_INGRIDIENTS_TO_ORDER_SECTION_XPATH,
        )

    def click_and_drag_ingridient_souce(self):
        self.drag_and_drop(
            MainPageLocators.INGRIDIENTS_SOUCE_XPATH,
            MainPageLocators.BURGER_INGRIDIENTS_TO_ORDER_SECTION_XPATH,
        )

    def click_and_drag_ingridient_filling(self):
        self.drag_and_drop(
            MainPageLocators.INGRIDIENTS_FILLING_XPATH,
            MainPageLocators.BURGER_INGRIDIENTS_TO_ORDER_SECTION_XPATH,
        )

    def check_counter_inreasing(self):
        return self.get_element_text(MainPageLocators.INGRIDIENT_COUNTER_XPATH)

    def check_placing_order_button_is_displayed(self):
        return self.check_element_is_displayed(
            MainPageLocators.BUTTON_PLACE_ORDER_XPATH
        )

    def click_placing_order_button(self):
        return self.click_element(MainPageLocators.BUTTON_PLACE_ORDER_XPATH)

    def check_modal_window_is_displayed(self):
        return self.check_element_is_not_displayed(
            MainPageLocators.SECTION_IS_OPENNED_XPATH
        )

    def check_modal_window_of_order_is_displayed(self):
        return self.check_element_is_not_displayed(
            MainPageLocators.SECTION_ORDER_IS_OPENNED_XPATH
        )

    def click_on_close_modal_window_of_order_with_wait(self):
        self.click_on_element_after_layout_hide(
            MainPageLocators.OVERLAY_XPATH, MainPageLocators.BUTTON_CLOSE_MODAL_XPATH
        )

    def click_on_close_modal_window_of_order(self):
        self.click_element(MainPageLocators.BUTTON_CLOSE_MODAL_XPATH)
