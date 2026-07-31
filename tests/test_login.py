import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_loader import load_test_data
from utils.logger import setup_logger

logger = setup_logger('test_login')

@allure.feature("登录功能")
@allure.story("参数化登录测试")
class TestLogin:
    @pytest.mark.parametrize("test_data", load_test_data("test_data.json"))
    @allure.title("登录测试: {test_data[username]} - 预期{test_data[expected_success]}")
    def test_login(self, driver, test_data):
        username = test_data["username"]
        password = test_data["password"]
        expected_success = test_data["expected_success"]
        expected_error = test_data.get("expected_error")

        # ---------- 步骤1：执行登录 ----------
        with allure.step("输入账号密码并提交登录"):
            login_page = LoginPage(driver)
            login_page.login(username, password)
            logger.info(f"使用账号 '{username}' 尝试登录")

        # ---------- 步骤2：根据预期结果断言 ----------
        if expected_success:
            with allure.step("验证登录成功，进入商品列表页"):
                inventory_page = InventoryPage(driver)
                assert inventory_page.get_page_title() == "Products", "未进入商品列表页"
                assert inventory_page.is_logged_in(), "购物车图标未显示"
                logger.info(f"✅ 登录成功: {username}")
                # 可在 Allure 报告中附加成功信息（可选）
                allure.attach(f"用户 {username} 登录成功", name="登录结果", attachment_type=allure.attachment_type.TEXT)
        else:
            with allure.step("验证登录失败，显示预期错误消息"):
                error_msg = login_page.get_error_message()
                assert error_msg == expected_error, f"预期错误 '{expected_error}'，实际 '{error_msg}'"
                logger.info(f"❌ 登录失败，错误消息: {error_msg}")
                allure.attach(f"错误消息: {error_msg}", name="错误信息", attachment_type=allure.attachment_type.TEXT)