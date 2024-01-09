from pages.main_page import MainPageHelper
from pages.login_page import LoginPageHelper




class TestPasswordRecovery:
    def test_transition_to_password_reset_page(self, driver):
        main_page = MainPageHelper(driver)
        login_page = LoginPageHelper(driver)
        main_page.go_to_site()
        main_page.click_on_profile_batton()
        login_page.click_on_forgot_password_btn()
        assert "Восстановление пароля" in login_page.check_transition_to_the_forgot_password_page()

    def test_enter_email_and_click_on_restore_button(self, driver):
        main_page = MainPageHelper(driver)
        login_page = LoginPageHelper(driver)
        main_page.go_to_site()
        main_page.click_on_profile_batton()
        login_page.click_on_forgot_password_btn()
        login_page.set_email_to_field('random@mail.ru')
        login_page.click_on_recover_btn()
        assert "Сохранить" in login_page.find_btn_save()

    def test_show_password_button_makes_the_field_active(self, driver):
        main_page = MainPageHelper(driver)
        login_page = LoginPageHelper(driver)
        main_page.go_to_site()
        main_page.click_on_profile_batton()
        login_page.click_on_forgot_password_btn()
        login_page.set_email_to_field('random@mail.ru')
        login_page.click_on_recover_btn()
        login_page.click_on_eye_icon()
        assert 'input__placeholder-focused' in login_page.check_active_email_input()









