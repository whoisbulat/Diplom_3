import allure

from pages.login_page import LoginPageHelper
from pages.main_page import MainPageHelper
from pages.order_feed_page import FeedOrderPageHelper
from pages.profile_page import ProfilePageHelper




class TestOrderFeed:
    @allure.title('Открытие дельной модалки заказа')
    @allure.description('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_check_open_ingredient_modal(self, driver):
        main_page = MainPageHelper(driver)
        feed_page = FeedOrderPageHelper(driver)
        main_page.click_on_feed_batton()
        feed_page.click_on_order_list()
        assert "Cостав" in feed_page.check_open_details_order()

    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_orders_from_the__Order_History_section_are_displayed_on_the_Order_Feed_page(self, driver, register_user):
        main_page = MainPageHelper(driver)
        login_page = LoginPageHelper(driver)
        profile_page = ProfilePageHelper(driver)
        order_feed_page = FeedOrderPageHelper(driver)
        main_page.click_on_profile_batton()
        login_page.user_authorization(register_user["login"], register_user["password"])
        main_page.drag_and_drop()
        main_page.click_on_create_order_btn()
        main_page.click_on_close_btn_on_detail_inrgredient_modal()
        main_page.click_on_profile_batton()
        profile_page.click_order_histoty_btn()
        order_number_on_profile = profile_page.get_order_number()
        main_page.click_on_feed_batton()
        assert order_number_on_profile == order_feed_page.get_order_number()

    @allure.title('после оформления заказа его номер появляется в разделе В работе')
    @allure.description('после оформления заказа его номер появляется в разделе В работе.')
    def test_order_number(self, driver, register_user):
        main_page = MainPageHelper(driver)
        login_page = LoginPageHelper(driver)
        order_feed_page = FeedOrderPageHelper(driver)
        main_page.click_on_profile_batton()
        login_page.user_authorization(register_user["login"], register_user["password"])
        main_page.drag_and_drop()
        main_page.click_on_create_order_btn()
        order_number_on_modal = main_page.check_order_number_on_modal()
        main_page.click_on_close_btn_on_detail_inrgredient_modal()
        main_page.click_on_feed_batton()
        assert order_feed_page.get_user_order_in_progress_(order_number_on_modal)

    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.description('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_order_counter_all(self, driver, register_user):
        main_page = MainPageHelper(driver)
        login_page = LoginPageHelper(driver)
        order_feed_page = FeedOrderPageHelper(driver)
        main_page.click_on_feed_batton()
        counter = order_feed_page.check_all_time_counter()
        main_page.click_on_profile_batton()
        login_page.user_authorization(register_user["login"], register_user["password"])
        main_page.drag_and_drop()
        main_page.click_on_create_order_btn()
        main_page.click_on_close_btn_on_detail_inrgredient_modal()
        main_page.click_on_feed_batton()
        actual_counter = int(counter) + 1
        assert actual_counter == int(order_feed_page.check_all_time_counter())

    @allure.title('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.description('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_order_counter_day(self, driver, register_user):
        main_page = MainPageHelper(driver)
        login_page = LoginPageHelper(driver)
        order_feed_page = FeedOrderPageHelper(driver)
        main_page.click_on_feed_batton()
        counter = order_feed_page.check_day_time_counter()
        main_page.click_on_profile_batton()
        login_page.user_authorization(register_user["login"], register_user["password"])
        main_page.drag_and_drop()
        main_page.click_on_create_order_btn()
        main_page.click_on_close_btn_on_detail_inrgredient_modal()
        main_page.click_on_feed_batton()
        actual_counter = int(counter) + 1
        assert actual_counter == int(order_feed_page.check_day_time_counter())





