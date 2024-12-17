from selenium.webdriver.support.expected_conditions import alert_is_present

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_basket_btn(self):
        # проверка на наличие кнопки
        basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        basket_btn.click()

    def should_be_alert_name(self):
        # проверка на наличие сообщения с именем книги
        assert self.is_element_present(*ProductPageLocators.ALERT_INFO_NAME), "Нет сообщения с именем книги"

    def should_be_alert_cost(self):
        # проверка на наличие сообщения с ценой книги
        assert self.is_element_present(*ProductPageLocators.ALERT_INFO_COST), "Нет сообщения с ценой книги"

    def should_be_correct_product_name(self):
        # проверка корректности отображаемого сообщения о названии добавленной в корзину книги
        assert self.browser.find_element(
            *ProductPageLocators.ALERT_INFO_NAME_VALUE).text == self.browser.find_element(
            *ProductPageLocators.INFO_NAME).text, \
            "Имя книги некорректно"


    def should_be_correct_product_cost(self):
        # проверка корректности отображаемого сообщения о цене добавленной в корзину книги
        assert self.browser.find_element(
            *ProductPageLocators.ALERT_INFO_COST_VALUE).text == self.browser.find_element(
            *ProductPageLocators.INFO_COST).text, \
            "Имя книги некорректно"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_INFO_NAME), \
            "Сообщение присутствует, но не должно"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_INFO_NAME), \
            "Сообщение не исчезло, но должно"

