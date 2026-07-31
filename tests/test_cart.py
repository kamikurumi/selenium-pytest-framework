import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.data_loader import load_test_data
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utils.logger import setup_logger

logger = setup_logger('test_cart')

@allure.feature("购物车功能")
@allure.story("批量添加商品")
class TestCart:
    @pytest.mark.parametrize("test_data", load_test_data("cart_data.json"))
    @allure.title("批量添加商品测试: {test_data[scenario]}")
    def test_add_multiple_items_to_cart(self, driver, test_data):
        items = test_data["items"]
        should_succeed = test_data["should_succeed"]
        scenario = test_data.get("scenario", "未命名场景")

        with allure.step("1. 登录系统"):
            login_page = LoginPage(driver)
            login_page.login("standard_user", "secret_sauce")
            logger.info("登录成功")

        with allure.step("2. 进入商品列表页"):
            inventory_page = InventoryPage(driver)
            assert inventory_page.is_logged_in(), "登录失败"
            logger.info("进入商品列表页")

        if should_succeed:
            with allure.step("3. 依次添加多个商品到购物车"):
                for item in items:
                    item_name = item["name"]
                    expected_price = item["expected_price"]
                    with allure.step(f"添加商品: {item_name}"):
                        actual_price = inventory_page.get_item_price_by_name(item_name)
                        assert actual_price == expected_price, f"价格不符: {item_name}"
                        inventory_page.add_item_to_cart_by_name(item_name)
                        logger.info(f"已添加商品: {item_name}")

            with allure.step("4. 进入购物车并验证"):
                cart_page = inventory_page.go_to_cart()
                expected_count = len(items)
                actual_count = cart_page.get_cart_item_count()
                assert actual_count == expected_count, f"购物车数量应为 {expected_count}，实际为 {actual_count}"
                cart_item_names = cart_page.get_all_item_names()
                cart_item_prices = cart_page.get_all_item_prices()
                for item in items:
                    assert item["name"] in cart_item_names, f"商品 {item['name']} 不在购物车"
                    assert item["expected_price"] in cart_item_prices, f"价格 {item['expected_price']} 不在购物车"
                logger.info(f"验证通过，购物车共 {actual_count} 件商品")

        else:
            with allure.step("3. 异常场景：添加不存在的商品"):
                invalid_item = items[0]["name"]
                with pytest.raises((NoSuchElementException, TimeoutException)):
                    inventory_page.add_item_to_cart_by_name(invalid_item)
                logger.info(f"预期的异常发生，商品 '{invalid_item}' 不存在")

        # 附加日志文件到 Allure 报告（可选）
        # 可在全局后置中统一附加，这里省略