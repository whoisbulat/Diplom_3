import allure
from selenium.webdriver import ActionChains
from locators.main_locators import MainPageLocators
from pages.base_page import BasePage



class MainPageHelper(BasePage):
    @allure.step('Переходим на страницу профиля')
    def click_on_profile_batton(self):
        self.click_to_element(MainPageLocators.LOCATOR_PROFILE_BATTON_ON_HEADER)

    @allure.step('Переходим на страницу ленты')
    def click_on_feed_batton(self):
        self.click_to_element(MainPageLocators.LOCATOR_FEED_BTN)

    @allure.step('Проверяем переход на главную страницу')
    def text_burger_title_on_main_page(self):
        burger_text = self.find_element(MainPageLocators.LOCATOR_BURGER_TITLE_ON_MAIN)
        return burger_text.text

    @allure.step('Переходим на страницу конструктора')
    def click_on_constructor_batton(self):
        self.click_to_element(MainPageLocators.LOCATOR_CONSTRUCTOR_BTN_ON_HEADER)

    @allure.step('Кликаем на ингредиент')
    def click_on_ingredient(self):
        self.click_to_element(MainPageLocators.LOCATOR_INGREDIENT_BTN)

    @allure.step('проверяем открытие модалки')
    def find_text_on_detail_modal(self):
        detail_modal_text = self.find_element(MainPageLocators.LOCATOR_TEXT_ON_DETAIL_MODAL)
        return detail_modal_text.text

    @allure.step('Закрываем модалку')
    def click_on_close_btn_on_detail_inrgredient_modal(self):
        self.click_to_element(MainPageLocators.LOCATOR_CLOSE_DETAIL_INGREDIENT_MODAL)

    @allure.step('Переходим на страницу профиля')
    def click_on_create_order_btn(self):
        self.click_to_element(MainPageLocators.LOCATOR_CREATE_ORDER)

    @allure.step('Переходим на страницу профиля')
    def check_confirm_create_order(self):
        confirm_create_order = self.find_element(MainPageLocators.LOCATOR_CONFIRM_CREATE_ORDER)
        return confirm_create_order.text

    @allure.step('Кладем элемент бургера в конструктор')
    def drag_and_drop(self):
        action_chains = ActionChains(self.driver)
        source_element = self.find_element(MainPageLocators.LOCATOR_INGREDIENT_BTN)
        target_element = self.find_element(MainPageLocators.LOCATOR_BURGER_CONSTRUCTOR)
        action_chains.drag_and_drop(source_element, target_element).perform()

    @allure.step('Проверяем, что при добавлении ингредиента в заказ счётчик  ингридиента увеличивается')
    def check_increasing_counter_when_adding_ingredient(self):
        counter_element = self.find_element(MainPageLocators.LOCATOR_ACTIVE_COUNTER_ON_BUN)
        return counter_element.text


    @allure.step('Проверяем номер заказа в модалке')
    def check_order_number_on_modal(self):
        locator = MainPageLocators.LOCATOR_ORDER_NUMBER_ON_MODAL
        current_order = self.return_element_text(locator)
        self.wait_element_(locator, current_order)
        new_order = self.return_element_text(locator)
        return new_order



