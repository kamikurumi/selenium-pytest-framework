# Selenium + Pytest 自动化测试框架（Edge 浏览器）

基于 Python + Selenium + Pytest + Page Object Model 的 Web 自动化测试项目，针对 SauceDemo 网站实现登录、购物车等核心业务流程，并集成了数据驱动、日志、失败截图和 Allure 报告。

## 技术栈

- Python 3.9+
- Selenium 4.x
- Pytest 7.x
- Allure Pytest
- Microsoft Edge 浏览器（需安装对应版本 WebDriver）
- Page Object Model（POM）
- JSON 数据驱动
- 日志记录（logging）
- 失败自动截图（Allure 集成）

## 环境准备

### 1. 安装 Python 依赖

```bash
pip install -r requirements.txt