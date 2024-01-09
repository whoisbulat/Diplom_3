import allure
from locators.order_feed_locators import FeedOrderPageLocators
from pages.base_page import BasePage




class FeedOrderPageHelper(BasePage):
    @allure.step('Переход на страницу ленты')
    def check_go_on_feed_page(self):
        feed_text = self.find_element(FeedOrderPageLocators.LOCATOR_FEED_TEXT_ON_HEADER)
        return feed_text.text

    @allure.step('открываем детальный заказ')
    def click_on_order_list(self):
        self.click_to_element(FeedOrderPageLocators.LOCATOR_ORDER_LIST_BTN)

    @allure.step('проверяем открытие модалки детализации заказа')
    def check_open_details_order(self):
        modal_text = self.find_element(FeedOrderPageLocators.LOCATOR_TEXT_ON_DETAILS_ORDER_MODAL)
        return modal_text.text

    @allure.step('проверяем счетчик  Выполнено за все время')
    def check_all_time_counter(self):
        text = self.find_element(FeedOrderPageLocators.LOCATOR_ALL_TIME_COUNTER)
        return text.text

    @allure.step('берем номер заказа')
    def get_order_number(self):
        element = self.find_element(FeedOrderPageLocators.LOCATOR_ORDER_NUMBER_ON_ORDER_FEED)
        return element.text

    @allure.step('проверяем счетчик Выполнено за сегодня')
    def check_day_time_counter(self):
        element = self.find_element(FeedOrderPageLocators.LOCATOR_DAY_TIME_COUNTER)
        return element.text

    @allure.step('проверяем что после оформления заказа его номер появляется в разделе В работе')
    def check_order_in_progress(self):
        text = self.find_element(FeedOrderPageLocators.LOCATOR_ORDER_LIST_STATUS_IN_WORKING)
        return text.text