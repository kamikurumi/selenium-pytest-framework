import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from utils.logger import setup_logger
import allure
import os

logger = setup_logger('conftest')

@pytest.fixture(scope="session")
def driver():
    logger.info("启动 Edge 浏览器（Session 级别）")
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=options)
    base_url = "https://www.saucedemo.com/"
    driver.get(base_url)
    logger.info(f"访问首页: {base_url}")
    yield driver
    logger.info("关闭浏览器")
    driver.quit()


@pytest.fixture(autouse=True)
def reset_session_state(driver):
    """每个用例后清理状态"""
    yield
    driver.delete_all_cookies()
    driver.refresh()
    logger.info("清理 Session 状态（Cookies 清除，页面刷新）")


# ------------------ 失败自动截图（集成 Allure） ------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """在测试失败时自动截图并附加到 Allure 报告"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # 获取 driver 实例（如果 fixture 存在）
        driver = item.funcargs.get('driver', None)
        if driver:
            # 截图并保存到 reports/screenshots 目录
            screenshot_dir = os.path.join(os.path.dirname(__file__), "reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}_{call.time}.png")
            driver.save_screenshot(screenshot_path)
            logger.error(f"测试失败，截图保存至: {screenshot_path}")

            # 附加到 Allure 报告
            with open(screenshot_path, 'rb') as f:
                allure.attach(f.read(), name="失败截图", attachment_type=allure.attachment_type.PNG)
        else:
            logger.warning("无法获取 driver 实例，跳过截图")