from selenium.webdriver.common.by import By


class MainPageLocators:
    LINK = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    PRODUCT_BASKET_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-default")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BAG_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    SUCCESSFUL_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")