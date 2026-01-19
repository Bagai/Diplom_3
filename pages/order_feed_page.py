from .base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
import allure


class OrderFeedPage(BasePage):
    
    def click_on_order(self):
        self.click_element(OrderFeedPageLocators.ORDER_FEED_ELEMENT_XPATH)

    def check_modal_is_opened(self):
        return self.check_element_is_displayed(OrderFeedPageLocators.ORDER_MODAL_IS_OPENED_XPATH)
    
    def get_order_number(self):
        return self.get_element_text(OrderFeedPageLocators.ORDER_FEED_ORDER_NUMBER_ELEMENT_XPATH)

    def get_total_number_rders(self):
        return self.get_element_text(OrderFeedPageLocators.TOTAL_NUMBER_ALL_TIME_ELEMENT_XPATH)
    
    def get_total_number_today_orders(self):
        return self.get_element_text(OrderFeedPageLocators.TOTAL_NUMBER_TODAY_ELEMENT_XPATH)
    
    def check_isorder_in_progress(self, order_number):
        return self.get_element_text(OrderFeedPageLocators.ORDER_FEED_ORDER_NUMBER_ELEMENT_XPATH) == order_number