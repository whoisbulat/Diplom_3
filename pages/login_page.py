from locators.login_locators import LoginPageLocators
from pages.base_page import BasePage
import allure




class LoginPageHelper(BasePage):
    @allure.step('Кликаем на кнопку забыли пароль')
    def click_on_forgot_password_btn(self):
        self.click_to_element(LoginPageLocators.LOCATOR_FORGOT_PASSWORD_BATTON)
    @allure.step('проверяем переход на страницу восстановления пароля')
    def check_transition_to_the_forgot_password_page(self):
        forgot_page = self.find_element(LoginPageLocators.LOCATOR_TEXT_PASSWORD_RECOVERY_ON_HEADER)
        return forgot_page.text

    @allure.step('Заполняем поле email')
    def set_email_to_field(self, text):
        self.set_text_to_element(LoginPageLocators.LOCATOR_INPUT_EMAIL, text)

    @allure.step('Кликаем на кнопку восстановить')
    def click_on_recover_btn(self):
        self.click_to_element(LoginPageLocators.LOCATOR_RECOVER_BTN)

    @allure.step('находим кнопку сохранить')
    def find_btn_save(self):
        forgot_page = self.find_element(LoginPageLocators.LOCATOR_SAVE_BTN)
        return forgot_page.text

    @allure.step('Кликаем на показать/скрыть')
    def click_on_eye_icon(self):
        self.click_to_element(LoginPageLocators.LOCATOR_EYE_ICON)

    @allure.step('Проверяем активное состояние инпута email')
    def check_active_email_input(self):
        return self.find_element(LoginPageLocators.LOCATOR_ACTIVE_PASSWORD_INPUT).get_attribute("class")

    @allure.step('Логин пользователя')
    def user_authorization(self, email, password):
        self.set_text_to_element(LoginPageLocators.LOCATOR_EMAIL_INPUT_LOGIN_PAGE, email)
        self.set_text_to_element(LoginPageLocators.LOCAROR_PASSWORD_INPUT_LOGIN_PAGE, password)
        self.click_to_element(LoginPageLocators.LOCATOR_LOGIN_BUTTON)

    @allure.step('Кликаем на кнопку забыли пароль')
    def find_login_text_on_header(self):
        text_login = self.find_element(LoginPageLocators.LOCATOR_LOGIN_TEXT_ON_HEADER)
        return text_login.text
