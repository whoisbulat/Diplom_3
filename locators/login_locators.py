from selenium.webdriver.common.by import By



class LoginPageLocators:
    LOCATOR_EMAIL_INPUT_LOGIN_PAGE = (By.XPATH, "//input[@name='name']")  # поле для ввода емайла на странице авторизации
    LOCAROR_PASSWORD_INPUT_LOGIN_PAGE = (By.XPATH, "//input[@name='Пароль']")  # поле для ввода пароля на странице авторизации
    LOCATOR_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")  # кнопка входа на странице авторизации
    LOCATOR_TEXT_PASSWORD_RECOVERY_ON_HEADER = By.XPATH, "//h2[contains(text(),'Восстановление пароля')]"
    LOCATOR_FORGOT_PASSWORD_BATTON = By.XPATH, "//a[contains(text(),'Восстановить пароль')]"
    LOCATOR_RECOVER_BTN = By.XPATH, "//button[contains(text(),'Восстановить')]"
    LOCATOR_INPUT_EMAIL = By.XPATH, "//input[@name='name']"
    LOCATOR_INPUT_PASSWORD = By.XPATH, "//input[@name='//input[@name='Введите новый пароль']']"
    LOCATOR_INPUT_CODE = By.XPATH, "//input[@name='//input[@name='name']']"
    LOCATOR_SAVE_BTN = By.XPATH, "//button[contains(text(),'Сохранить')]"
    LOCATOR_EYE_ICON = By.XPATH, "//div[contains(@class,'input__icon-action')]"
    LOCATOR_LOGIN_TEXT_ON_HEADER = By.XPATH, "//h2[contains(text(),'Вход')]"
    LOCATOR_ACTIVE_PASSWORD_INPUT = By.XPATH, "//label[contains(@class,'input__placeholder text noselect')][1]"