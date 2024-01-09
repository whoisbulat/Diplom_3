from selenium.webdriver.common.by import By




class MainPageLocators:
    LOCATOR_PROFILE_BATTON_ON_HEADER = By.XPATH, "//p[contains(text(),'Личный Кабинет')]"
    LOCATOR_CONSTRUCTOR_BTN_ON_HEADER = By.XPATH, "//p[contains(text(),'Конструктор')]"
    LOCATOR_FEED_BTN = By.XPATH, "//p[contains(text(),'Лента Заказов')]"
    LOCATOR_BURGER_TITLE_ON_MAIN = By.XPATH, "//h1[text()='Соберите бургер']"
    LOCATOR_INGREDIENT_BTN = By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]"
    LOCATOR_TEXT_ON_DETAIL_MODAL = By.XPATH, "//h2[contains(text(),'Детали ингредиента')]"
    LOCATOR_CLOSE_DETAIL_INGREDIENT_MODAL = By.XPATH, "//button[contains(@class, 'Modal_modal__close')]"
    LOCATOR_CREATE_ORDER = By.XPATH, "//button[contains(text(),'Оформить заказ')]"
    LOCATOR_CONFIRM_CREATE_ORDER = By.XPATH, "//p[contains(text(),'Ваш заказ начали готовить')]"
    LOCATOR_INGREDIENT_BUN = By.XPATH, "//a[contains(@class, 'BurgerIngredient')]"
    LOCATOR_BURGER_CONSTRUCTOR = By.XPATH, "//ul[@class = 'BurgerConstructor_basket__list__l9dp_']"
    LOCATOR_ACTIVE_COUNTER_ON_BUN = By.XPATH, "//div[@class='counter_counter__ZNLkj counter_default__28sqi']/p[text()='2'][1]"
    LOCATOR_ORDER_NUMBER_ON_MODAL = By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]"