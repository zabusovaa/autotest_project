from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn-default")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    REGISTER_EMAIL = (By.CSS_SELECTOR, "[name=registration-email]")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "[name=registration-password1]")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "[name=registration-password2]")
    REGISTER_BTN = (By.CSS_SELECTOR, "[name=registration_submit]")

class BasketPageLocators():
    INFO_BASKET = (By.CSS_SELECTOR, ".content #content_inner p")
    ITEM_BASKET = (By.CSS_SELECTOR, ".basket-items")

class ProductPageLocators():
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")

    INFO_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    INFO_COST = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")

    ALERT_INFO_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
    ALERT_INFO_COST = (By.CSS_SELECTOR, ".alert-info .alertinner")

    ALERT_INFO_NAME_VALUE = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    ALERT_INFO_COST_VALUE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

