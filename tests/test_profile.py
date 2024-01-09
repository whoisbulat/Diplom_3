from pages.profile_page import ProfilePageHelper
from pages.login_page import LoginPageHelper
from pages.main_page import MainPageHelper




class TestProfile:
    def test_user_authorization(self, driver, register_user):
        main_page = MainPageHelper(driver)
        login_page = LoginPageHelper(driver)
        profile_page = ProfilePageHelper(driver)
        main_page.go_to_site()
        main_page.click_on_profile_batton()
        login_page.user_authorization(register_user["login"], register_user["password"])
        main_page.click_on_profile_batton()
        assert 'Профиль' in profile_page.find_text_profile_on_profile_page()

    def test_logout_user(self, driver, register_user):
        main_page = MainPageHelper(driver)
        login_page = LoginPageHelper(driver)
        profile_page = ProfilePageHelper(driver)
        main_page.go_to_site()
        main_page.click_on_profile_batton()
        login_page.user_authorization(register_user["login"], register_user["password"])
        main_page.click_on_profile_batton()
        profile_page.click_logout_user_btn()
        assert "Вход" in login_page.find_login_text_on_header()

    def test_order_history(self, driver, register_user):
        main_page = MainPageHelper(driver)
        login_page = LoginPageHelper(driver)
        profile_page = ProfilePageHelper(driver)
        main_page.go_to_site()
        main_page.click_on_profile_batton()
        login_page.user_authorization(register_user["login"], register_user["password"])
        main_page.drag_and_drop()
        main_page.click_on_create_order_btn()
        main_page.click_on_close_btn_on_detail_inrgredient_modal()
        main_page.click_on_profile_batton()
        profile_page.click_order_histoty_btn()
        assert 'OrderHistory_orderHistory__qy1VB' == profile_page.order_history_displayed()



