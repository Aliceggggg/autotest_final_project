from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    # --- геттеры: вытаскивают данные со страницы ---

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    # --- методы-проверки: принимают ожидаемые значения аргументами ---

    def should_be_product_added_message(self, expected_name):
        actual_name = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME
        ).text
        assert actual_name == expected_name, (
            f"Product name mismatch: expected '{expected_name}', got '{actual_name}'"
        )

    def should_be_basket_total_equal_product_price(self, expected_price):
        actual_price = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL
        ).text
        assert actual_price == expected_price, (
            f"Price mismatch: expected '{expected_price}', got '{actual_price}'"
        )