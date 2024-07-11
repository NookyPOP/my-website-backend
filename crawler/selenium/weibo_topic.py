from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import openpyxl

import time

# 指定chromedriver的路径
service = Service("/Users/kevin/Documents/chromedriver-mac-arm64/chromedriver")

# 设置chrome的options

options = Options()

options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

browser = webdriver.Chrome(options=options, service=service)

browser.get("https://weibo.com/newlogin?tabtype=search&gid=&openLoginLayer=0&url=")
# browser.(30)
# time.sleep(10)
browser.implicitly_wait(10)
browser.maximize_window()
# browser.set_script_timeout(10)
titles = []
for num in range(2):
    browser.execute_script(f"document.documentElement.scrollTop = {270 + num * 891}")
    time.sleep(2)
    titles_num = browser.find_elements(
        By.CSS_SELECTOR, "#app .Main_full_1dfQX .woo-box-flex.woo-box-alignCenter > a"
    )
    titles.append(titles_num)
    print(len(titles))


# for title in titles:
#     url = title.get_attribute("href")
#     text = title.text
#     print(url, text)
time.sleep(1010)
