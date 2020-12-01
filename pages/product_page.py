from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators
from .main_page import MainPage

link = ProductPageLocators.PRODUCT_LINK


class ProductPage(BasePage):
    def should_be_promo_in_link(self):
        page = MainPage(self.browser, link)
        page.open()
        current_url = str(self.browser.current_url)
        assert "?promo=newYear" in current_url,\
            "There isn't '?promo=newYear' in current url"

    def add_product_to_bag(self):
        page = MainPage(self.browser, link)
        page.open()
        self.browser.find_element(
            *ProductPageLocators.ADD_TO_BAG_BUTTON
        ).click()
        page.solve_quiz_and_get_code()

    def should_be_successful_message(self):
        page = MainPage(self.browser, link)
        self.add_product_to_bag()
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(*ProductPageLocators.SUCCESSFUL_MESSAGE))
        assert page.is_element_present(
            *ProductPageLocators.SUCCESSFUL_MESSAGE),\
            "There is not a message about successful editing a product"

    def cost_should_be_match(self):
        pass
