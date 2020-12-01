import pytest

from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

link = ProductPageLocators.PRODUCT_LINK


@pytest.mark.login
class TestLoginFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title="Best book created by robot")
        # создаем по апи
        self.link = self.product.link
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали
        self.product.delete()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация теста

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация теста


def test_promo_in_link(browser):
    page = ProductPage(browser, link)
    page.should_be_promo_in_link()


def test_add_product_to_bag(browser):
    page = ProductPage(browser, link)
    page.add_product_to_bag()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.should_be_successful_message()


def test_guest_cant_see_success_message(browser):
    pass


def test_message_disappeared_after_adding_product_to_basket(browser):
    pass


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.open_product_basket()
    page = BasketPage(browser, link)
    page.basket_is_empty()
    page.should_be_message_basket_is_empty()
