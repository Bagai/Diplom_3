from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ex
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        self.wait.until(ex.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()

    def find_element_with_wait(self, locator):
        self.wait.until(ex.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    # def format_locator(self, locator, num_of_qa):
    #     method, unpack_locator = locator
    #     return (method, unpack_locator.format(num_of_qa))

    def get_element_text(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", self.find_element_with_wait(locator)
        )

    def check_element_is_displayed(self, locator):
        return self.find_element_with_wait(locator).is_displayed()

    def check_element_is_not_displayed(self, locator):
        try:
            self.find_element_with_wait(locator)
            return True
        except TimeoutException:
            return False

    # def open_last_tab(self):
    #     self.driver.switch_to("-1")

    def drag_and_drop(self, locator_of_elemnt_to_drag, locaor_of_elemnt_to_drop):
        drag_element = self.driver.find_element(*locator_of_elemnt_to_drag)
        drop_element = self.driver.find_element(*locaor_of_elemnt_to_drop)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(drag_element, drop_element).perform()

    def click_on_element_after_layout_hide(self, locator, locator_click):
        self.wait.until_not(ex.visibility_of_element_located(locator))
        self.click_element(locator_click)
