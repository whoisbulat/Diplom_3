from pages.login_page import LoginPageHelper
from pages.main_page import MainPageHelper
import time
from pages.order_feed_page import FeedOrderPageHelper
from pages.profile_page import ProfilePageHelper




class TestOrderFeed:
    def test_check_open_ingredient_modal(self, driver):
        main_page = MainPageHelper(driver)
        feed_page = FeedOrderPageHelper(driver)
        main_page.go_to_site()
        main_page.click_on_feed_batton()
        feed_page.click_on_order_list()
        time.sleep(2)
        assert "Cостав" in feed_page.check_open_details_order()

    def test_orders_from_the__Order_History_section_are_displayed_on_the_Order_Feed_page(self, driver, register_user):
        main_page = MainPageHelper(driver)
        login_page = LoginPageHelper(driver)
        profile_page = ProfilePageHelper(driver)
        order_feed_page = FeedOrderPageHelper(driver)
        main_page.go_to_site()
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

    def test_order_number(self, driver, register_user):
        main_page = MainPageHelper(driver)
        login_page = LoginPageHelper(driver)
        order_feed_page = FeedOrderPageHelper(driver)
        main_page.go_to_site()
        main_page.click_on_profile_batton()
        login_page.user_authorization(register_user["login"], register_user["password"])
        main_page.drag_and_drop()
        main_page.click_on_create_order_btn()
        time.sleep(2)
        check = main_page.check_order_number_on_modal()
        main_page.click_on_close_btn_on_detail_inrgredient_modal()
        main_page.click_on_feed_batton()
        time.sleep(5)
        order_in_working = order_feed_page.check_order_in_progress()
        assert check in order_in_working

    def test_order_counter_all(self, driver, register_user):
        main_page = MainPageHelper(driver)
        login_page = LoginPageHelper(driver)
        order_feed_page = FeedOrderPageHelper(driver)
        main_page.go_to_site()
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

    def test_order_counter_day(self, driver, register_user):
        main_page = MainPageHelper(driver)
        login_page = LoginPageHelper(driver)
        order_feed_page = FeedOrderPageHelper(driver)
        main_page.go_to_site()
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
