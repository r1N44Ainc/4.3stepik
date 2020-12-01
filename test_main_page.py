import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.locators import MainPageLocators
from .pages.main_page import MainPage

link = MainPageLocators.LINK

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
         pass

    def test_guest_should_see_login_link(self, browser):
         pass

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_login_page(browser):
    page = LoginPage(browser, link)
    page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.open_product_basket()
    page = BasketPage(browser, link)
    page.basket_is_empty()
    page.should_be_message_basket_is_empty()









