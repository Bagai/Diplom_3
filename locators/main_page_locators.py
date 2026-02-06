from selenium.webdriver.common.by import By


class MainPageLocators:
    INGRIDIENTS_BUN_XPATH = (
        By.XPATH,
        ".//h2[text()='Булки']/following::ul[1]/a[1]",
    )
    INGRIDIENTS_SOUCE_XPATH = (
        By.XPATH,
        ".//h2[text()='Соусы']/following::ul[1]/a[1]",
    )
    INGRIDIENTS_FILLING_XPATH = (
        By.XPATH,
        ".//h2[text()='Начинки']/following::ul[1]/a[1]",
    )
    BUTTON_CLOSE_MODAL_XPATH = (
        By.XPATH,
        ".//section[contains(@class,'Modal_modal__P3_V5')]/div/button",
    )
    BURGER_INGRIDIENTS_TO_ORDER_SECTION_XPATH = (
        By.XPATH,
        ".//section[contains(@class, 'BurgerConstructor_basket')]",
    )
    INGRIDIENT_COUNTER_XPATH = (
        By.XPATH,
        ".//h2[text()='Булки']/following::ul[1]/a[1]/div/p[contains(@class, 'counter_counter__num__3nue1')]",
    )
    BUTTON_PLACE_ORDER_XPATH = (
        By.XPATH,
        ".//button[text()='Оформить заказ']",
    )
    SECTION_IS_OPENNED_XPATH = (
        By.XPATH,
        ".//section[contains(@class, 'Modal_modal_opened')]",
    )
    SECTION_ORDER_IS_OPENNED_XPATH = (
        By.XPATH,
        ".//section[contains(@class, 'Modal_modal_opened')]/div/div/p[text()='идентификатор заказа']",
    )
    BUTTON_CLOSE_MODAL_XPATH = (
        By.XPATH,
        ".//button[contains(@class, 'Modal_modal__close')]",
    )
    OVERLAY_XPATH = (
        By.XPATH,
        ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]",
    )
