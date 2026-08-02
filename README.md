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
```
### 2. 安装 Microsoft Edge WebDriver
确保 Edge 浏览器已安装（推荐最新稳定版）。\
下载与 Edge 版本匹配的 Edge WebDriver。\
将 msedgedriver.exe 放入系统 PATH。

### 3. 安装 Allure 命令行（用于生成报告）
下载 Allure 2.x 并解压。\
将 bin 目录添加到系统 PATH。\
验证：allure --version

## 项目结构
├── data/                   # JSON 测试数据\
│   ├── test_data.json      # 登录数据\
│   └── cart_data.json      # 购物车数据\
├── pages/                  # Page Object 类\
│   ├── base_page.py        # 封装 Selenium 基础操作\
│   ├── login_page.py\
│   ├── inventory_page.py\
│   └── cart_page.py\
├── tests/                  # 测试用例\
│   ├── test_login.py       # 登录参数化测试\
│   └── test_cart.py        # 购物车业务流程测试\
├── utils/                  # 工具模块\
│   ├── logger.py           # 日志配置\
│   └── data_loader.py      # JSON 数据加载\
├── conftest.py             # Pytest 配置及 fixture\
├── pytest.ini              # Pytest 参数配置\
├── requirements.txt        # 项目依赖 \
└── README.md

## 运行测试
### 运行全部测试
```bash
pytest -v -s --alluredir=./reports/allure_results
```


### 生成 HTML 报告
```bash
allure generate ./reports/allure_results -o ./reports/allure_report --clean
```

### 打开报告（自动启动本地服务器）
```bash
allure open ./reports/allure_report
```
### 日志与截图
日志文件保存在 reports/logs/，按时间命名。\
失败时自动截图，保存于 reports/screenshots/，并嵌入 Allure 报告。

### 数据驱动说明
登录数据：data/test_data.json，包含用户名、密码、预期结果。\
购物车数据：data/cart_data.json，支持批量添加多商品或异常场景。

### 扩展建议
可添加更多 Page Object 支持结算流程。\
可集成 CI/CD（如 GitHub Actions）自动运行。\
可改用 Chrome/Firefox 等其他浏览器（修改 conftest.py 中的 driver 初始化）。