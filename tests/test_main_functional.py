from pages.login_page import LoginPageHelper
from pages.main_page import MainPageHelper
from pages.order_feed_page import FeedOrderPageHelper




class TestMainFunctional:
    def test_go_to_on_page_feed(self, driver):
        main_page = MainPageHelper(driver)
        feed_page = FeedOrderPageHelper(driver)
        main_page.go_to_site()
        main_page.click_on_feed_batton()
        assert "Лента заказов" in feed_page.check_go_on_feed_page()

    def test_go_to_on_page_burger(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_site()
        main_page.click_on_feed_batton()
        main_page.click_on_constructor_batton()
        assert "Соберите бургер" in main_page.text_burger_title_on_main_page()

    def test_open_modal_with_details_ingredients(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_site()
        main_page.click_on_ingredient()
        assert 'Детали ингредиента' in main_page.find_text_on_detail_modal()

    def test_close_modal_with_details_ingredients(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_site()
        main_page.click_on_ingredient()
        main_page.click_on_close_btn_on_detail_inrgredient_modal()
        assert 'Соберите бургер' in main_page.text_burger_title_on_main_page()

    def test_create_order_with_login_user(self, driver, register_user):
        main_page = MainPageHelper(driver)
        login_page = LoginPageHelper(driver)
        main_page.go_to_site()
        main_page.click_on_profile_batton()
        login_page.user_authorization(register_user["login"], register_user["password"])
        main_page.click_on_create_order_btn()
        assert 'Ваш заказ начали готовить' in main_page.check_confirm_create_order()

    def test_create_order(self, driver, register_user):
        main_page = MainPageHelper(driver)
        login_page = LoginPageHelper(driver)
        main_page.go_to_site()
        main_page.click_on_profile_batton()
        login_page.user_authorization(register_user["login"], register_user["password"])
        main_page.drag_and_drop()
        main_page.click_on_create_order_btn()
        assert 'Ваш заказ начали готовить' in main_page.check_confirm_create_order()

    def test_check_counter(self, driver, register_user):
        main_page = MainPageHelper(driver)
        login_page = LoginPageHelper(driver)
        main_page.go_to_site()
        main_page.click_on_profile_batton()
        login_page.user_authorization(register_user["login"], register_user["password"])
        main_page.drag_and_drop()
        assert '2' in main_page.check_increasing_counter_when_adding_ingredient()
