from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        """Возвращает название товара со страницы"""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        """Возвращает цену товара со страницы"""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение о добавлении товара в корзину отсутствует"

    def should_be_product_name_in_message(self, expected_name):
        """Проверяет, что название товара в сообщении совпадает с ожидаемым"""
        message_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert expected_name == message_name, \
            f"Название товара не совпадает: ожидалось '{expected_name}', получено '{message_name}'"

    def should_be_basket_total_equal_product_price(self, expected_price):
        """Проверяет, что стоимость корзины совпадает с ценой товара"""
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert expected_price == basket_total, \
            f"Стоимость корзины не совпадает: ожидалось '{expected_price}', получено '{basket_total}'"
