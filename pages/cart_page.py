from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def get_all_item_names(self) -> list:
        items = self.find_elements(self.CART_ITEMS)
        return [item.find_element(*self.ITEM_NAME).text for item in items]

    def get_all_item_prices(self) -> list:
        items = self.find_elements(self.CART_ITEMS)
        return [item.find_element(*self.ITEM_PRICE).text for item in items]

    def is_item_in_cart(self, item_name: str) -> bool:
        return item_name in self.get_all_item_names()

    def get_cart_item_count(self) -> int:
        return len(self.find_elements(self.CART_ITEMS))