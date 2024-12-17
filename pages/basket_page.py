from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty_info(self):
        # проверка наличия сообщения о том, что корзина пуста
        assert self.is_element_present(*BasketPageLocators.INFO_BASKET), "Нет сообщения о том, что корзина пуста"

    def should_be_basket_empty(self):
        # проверка, что корзина пуста
        assert self.is_not_element_present(*BasketPageLocators.ITEM_BASKET), "Корзина не пуста"

