from .base_page import BasePage
from locators.personal_accaount_page_locators import PersonalAccountPageLocators
import allure


class PersonalAccountPage(BasePage):
    
    @allure.step('Check history button is displayed')
    def check_history_button_is_diesplayed(self):
        return self.check_element_is_displayed(PersonalAccountPageLocators.BUTTON_ORDER_HISTORY_XPATH)
    
    @allure.step('Click history button')
    def click_history_button(self):
        self.click_element(PersonalAccountPageLocators.BUTTON_ORDER_HISTORY_XPATH)

    @allure.step('Click logout button')
    def click_logout_button(self):
        self.click_element(PersonalAccountPageLocators.BUTTON_LOGOUT_XPATH)
