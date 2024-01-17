from selenium.webdriver.common.by import By




class FeedOrderPageLocators:
    LOCATOR_FEED_TEXT_ON_HEADER = By.XPATH, "//h1[contains(text(),'Лента заказов')]"
    LOCATOR_ORDER_LIST_BTN = By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]"
    LOCATOR_TEXT_ON_DETAILS_ORDER_MODAL = By.XPATH, "//p[contains(text(),'Cостав')]"
    LOCATOR_ORDER_NUMBER_ON_ORDER_FEED = By.XPATH, "//p[@class = 'text text_type_digits-default']"
    LOCATOR_ALL_TIME_COUNTER = By.XPATH, "//p[contains(text(),'Выполнено за все время')]/following-sibling::p[contains(@class, 'OrderFeed_number')]"
    LOCATOR_DAY_TIME_COUNTER = By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'OrderFeed_number')]"
    LOCATOR_ORDER_LIST_STATUS_IN_WORKING = By.XPATH, "//*[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']"