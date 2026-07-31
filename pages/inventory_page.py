from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")

    @staticmethod
    def _item_add_button(name):
        return (By.XPATH, f"//div[text()='{name}']/ancestor::div[@class='inventory_item']//button[text()='Add to cart']")

    @staticmethod
    def _item_price(name):
        return (By.XPATH, f"//div[text()='{name}']/ancestor::div[@class='inventory_item']//div[@class='inventory_item_price']")

    def get_page_title(self) -> str:
        return self.find_element(self.TITLE).text

    def is_logged_in(self) -> bool:
        return self.find_element(self.SHOPPING_CART).is_displayed()

    def add_item_to_cart_by_name(self, item_name: str):
        self.click(self._item_add_button(item_name))

    def get_item_price_by_name(self, item_name: str) -> str:
        return self.find_element(self._item_price(item_name)).text

    def go_to_cart(self):
        self.click(self.SHOPPING_CART)
        from pages.cart_page import CartPage
        return CartPage(self.driver)