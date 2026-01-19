from .base_page import BasePage
from locators.personal_accaount_page_locators import PersonalAccountPageLocators
import allure


class PersonalAccountPage(BasePage):
    
    def check_history_button_is_diesplayed(self):
        return self.check_element_is_displayed(PersonalAccountPageLocators.BUTTON_ORDER_HISTORY_XPATH)
    
    def click_history_button(self):
        self.click_element(PersonalAccountPageLocators.BUTTON_ORDER_HISTORY_XPATH)

    def click_logout_button(self):
        self.click_element(PersonalAccountPageLocators.BUTTON_LOGOUT_XPATH)
