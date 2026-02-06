from .base_page import BasePage
from locators.order_history_page_locators import OrderHistoryPageLocators
import allure


class OrderHistoryPage(BasePage):
    
    @allure.step('Get order number')
    def get_order_number(self):
        return self.get_element_text(OrderHistoryPageLocators.ORDER_HISTORY_ORDER_NUMBER_ELEMENT_XPATH)
    
    @allure.step('Check menu is displayed')
    def check_menu_is_displayed(self):
        return self.check_element_is_displayed(OrderHistoryPageLocators.ORDER_HISTORY_MENU_XPATH)
    
    @allure.step('Get history order list')
    def get_order_list(self):
        return self.get_elemnts_text_list(OrderHistoryPageLocators.ORDER_HISTORY_ORDER_NUMBER_ELEMENT_XPATH)
