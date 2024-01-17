from selenium.webdriver.common.by import By





class ProfilePageLocators:
    LOCATOR_PROFILE_TEXT = By.XPATH, "//a[contains(text(),'Профиль')]"
    LOCATOR_LOGOUT = By.XPATH, "//button[contains(text(),'Выход')]"
    LOCATOR_ORDER_HISTORY_BTN = By.XPATH, "//a[contains(text(),'История заказов')]"
    LOCATOR_LIST_ORDER_HISTORY = By.XPATH, "//div[@class ='OrderHistory_orderHistory__qy1VB']"
    LOCATOR_ORDER_NUMBER_ON_HISTORY_ORDER = By.XPATH, "//p[@class = 'text text_type_digits-default']"