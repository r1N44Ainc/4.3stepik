from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators
from .main_page import MainPage

link = MainPageLocators.LINK


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        page = MainPage(self.browser, link)
        page.open()
        page.go_to_login_page()
        current_url = str(self.browser.current_url)
        assert "login" in current_url,\
            "There isn't 'login' in current url"

    def should_be_login_form(self):
        page = MainPage(self.browser, link)
        page.is_element_present(*LoginPageLocators.LOGIN_FORM)
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not presented"

    def should_be_register_form(self):
        page = MainPage(self.browser, link)
        page.is_element_present(*LoginPageLocators.REGISTER_FORM)
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form is not presented"

