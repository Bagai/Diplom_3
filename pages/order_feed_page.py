from .base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
import allure


class OrderFeedPage(BasePage):
    
    @allure.step('Click on order')
    def click_on_order(self):
        self.click_element(OrderFeedPageLocators.ORDER_FEED_ELEMENT_XPATH)

    @allure.step('Check modal is opened')
    def check_modal_is_opened(self):
        return self.check_element_is_displayed(OrderFeedPageLocators.ORDER_MODAL_IS_OPENED_XPATH)
    
    @allure.step('Check modal is closed')
    def check_modal_is_closed(self):
        return self.check_element_is_not_displayed(OrderFeedPageLocators.ORDER_MODAL_IS_OPENED_XPATH)
    @allure.step('Get order number')
    def get_order_number(self):
        return self.get_element_text(OrderFeedPageLocators.ORDER_FEED_ORDER_NUMBER_ELEMENT_XPATH)

    @allure.step('Get total number of orders')
    def get_total_number_rders(self):
        return self.get_element_text(OrderFeedPageLocators.TOTAL_NUMBER_ALL_TIME_ELEMENT_XPATH)
    
    @allure.step('Get total number of today orders')
    def get_total_number_today_orders(self):
        return self.get_element_text(OrderFeedPageLocators.TOTAL_NUMBER_TODAY_ELEMENT_XPATH)
    
    @allure.step('Check if order is in progress')
    def check_isorder_in_progress(self, order_number):
        return self.get_element_text(OrderFeedPageLocators.ORDER_FEED_ORDER_NUMBER_ELEMENT_XPATH) == order_number