from .base_page import BasePage
from locators.header_page_locators import HaderLocators
import allure


class HeaderPage(BasePage):
    
    def click_on_button_personal_account(self):
        self.click_element(HaderLocators.BUTTON_PERSONAL_ACCOUNT_XPATH)

    def click_on_button_constructor(self):
        self.click_element(HaderLocators.BUTTON_CONSTRUCTOR_XPATH)

    def click_on_button_order_feed(self):
        self.click_element(HaderLocators.BUTTON_ORDER_FEED_XPATH)
