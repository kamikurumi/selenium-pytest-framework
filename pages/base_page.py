from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import setup_logger
import logging

logger = setup_logger('BasePage')   # 每个类使用独立logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)

    def find_element(self, locator):
        logger.info(f"查找元素: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        logger.info(f"查找多个元素: {locator}")
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        logger.info(f"点击元素: {locator}")

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        logger.info(f"输入文本 '{text}' 到元素: {locator}")

    def wait_for_visible(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"元素 {locator} 在 {timeout}s 内不可见")
            raise

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        logger.info(f"滚动到元素: {locator}")
        return element