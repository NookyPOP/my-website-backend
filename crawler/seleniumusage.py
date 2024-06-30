from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# 指定 ChromeDriver 路径
service = Service("/Users/kevin/Documents/chromedriver-mac-arm64/chromedriver")
# 打开浏览器

# 设置 Chrome 选项
# chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--headless=chrome")
# 添加试验性参数
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# excludeswitches 告诉Chrome 排除某些默认启用的开关（switches）
# enable-automation 这是 Chrome 的一个特殊开关，当启用时，它会：
# a. 在浏览器窗口上显示一个 "Chrome 正在被自动化软件控制" 的提示条。
# b. 修改某些浏览器行为，使其更适合自动化测试。
chrome_options.add_experimental_option("useAutomationExtension", False)
# useAutomationExtension 自动化扩展是一个内置的Chrome扩展，主要用于支持自动化测试。它提供了一些额外的功能，一般真是的用户不安装
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)
"""
使用这两个实验的option的原因：
为什么要排除这个开关？

隐藏自动化特征：
移除浏览器顶部的自动化提示条，使浏览器外观更接近普通用户使用的状态。
绕过某些检测：
一些网站可能会检测自动化工具，并改变其行为或阻止访问。排除这个开关可以帮助绕过这些检测。
更真实的用户体验模拟：
在进行网页抓取或自动化测试时，可能希望浏览器行为尽可能接近真实用户。

"""
# chrome_options.add_argument("--headless=new")
# 如果不想看到浏览器窗口，我们可以通过下面的方式设置使用无头浏览器。


# 创建 Chrome WebDriver 实例
browser = webdriver.Chrome(service=service, options=chrome_options)
browser.set_window_size(1200, 800)
browser.set_window_position(400, 150)
# 打开网页
browser.get("https://www.baidu.com/")
# 设置隐式的等待时间
browser.implicitly_wait(4)

# 执行Chrome开发者协议命令（在加载页面时执行指定的JavaScript代码）
# browser.execute_cdp_cmd(
#     "Page.addScriptToEvaluateOnNewDocument",
#     {"source": 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'},
# )


# 通过 ID 查找input元素
element = browser.find_element(By.ID, "kw")
# 输入内容
element.send_keys("Python")
# 点击搜索按钮
button_element = browser.find_element(By.CSS_SELECTOR, "#su")
# 点击按钮
button_element.click()

# 创建显示等待对象
obj_wait = WebDriverWait(browser, 5)
# 设置等待条件
obj_wait.until(
    expected_conditions.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "#content_left")
    )
)
# 执行JavaScript代码
browser.execute_script(
    "document.documentElement.scrollTop = document.documentElement.scrollHeight"
)
# 截图
browser.get_screenshot_as_file("screenshot.png")
# 执行其他操作...
time.sleep(100)
# 完成后关闭浏览器
browser.quit()
