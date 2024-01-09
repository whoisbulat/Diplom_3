import allure
from locators.profile_locators import ProfilePageLocators
from pages.base_page import BasePage




class ProfilePageHelper(BasePage):

    @allure.step('Проверяем переход на страницу профиля')
    def find_text_profile_on_profile_page(self):
        text_profile = self.find_element(ProfilePageLocators.LOCATOR_PROFILE_TEXT)
        return text_profile.text

    @allure.step('кликаем выход из профиля')
    def click_logout_user_btn(self):
        self.click_to_element(ProfilePageLocators.LOCATOR_LOGOUT)

    @allure.step('открываем историю заказов')
    def click_order_histoty_btn(self):
        self.click_to_element(ProfilePageLocators.LOCATOR_ORDER_HISTORY_BTN)

    @allure.step('проверяем открытие истории заказа')
    def order_history_displayed(self):
        return self.find_element(ProfilePageLocators.LOCATOR_LIST_ORDER_HISTORY).get_attribute("class")

    @allure.step('провряем номер заказа')
    def get_order_number(self):
        element = self.find_element(ProfilePageLocators.LOCATOR_ORDER_NUMBER_ON_HISTORY_ORDER)
        return element.text



