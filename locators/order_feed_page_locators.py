from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_FEED_ELEMENT_XPATH = (
        By.XPATH,
        ".//ul[contains(@class, 'OrderFeed_list')]/li[1]",
    )
    ORDER_MODAL_IS_OPENED_XPATH = (
        By.XPATH,
        ".//section[contains(@class, 'Modal_modal_opened')]/div/div/p[text()='Cостав']",
    )
    ORDER_FEED_ORDER_NUMBER_ELEMENT_XPATH = (
        By.XPATH,
        ".//ul[contains(@class, 'OrderFeed_list')]/li/a/div/p[1]",
    )
    TOTAL_NUMBER_ALL_TIME_ELEMENT_XPATH = (
        By.XPATH,
        ".//div/p[text()='Выполнено за все время:']/following-sibling::p",
    )
    TOTAL_NUMBER_TODAY_ELEMENT_XPATH = (
        By.XPATH,
        ".//div/p[text()='Выполнено за сегодня:']/following-sibling::p",
    )
    ORDER_FEED_IN_PROGRESS_XPATH = (
        By.XPATH,
        ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li",
    )
