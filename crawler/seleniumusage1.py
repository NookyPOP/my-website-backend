from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
import requests
import os
import shutil

DOWNLOAD_PATH = "images_baidu"
# 指定 ChromeDriver 路径
service = Service("/Users/kevin/Documents/chromedriver-mac-arm64/chromedriver")
# 设置 Chrome 选项
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument(
    "User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
)
# chrome_options.add_experimental_option("detach", True)  # 让浏览器一直运行，直到关闭

# chrome_options.add_argument("--headless=new")
# 打开浏览器
browser = webdriver.Chrome(service=service, options=chrome_options)
# browser.set_window_size(1400, 850)
browser.maximize_window()
# 打开网页
browser.get("https://www.baidu.com/")
# 设置隐式的等待时间
# browser.implicitly_wait(2)
total_window_handles = []
# 获取当前页面的句柄
original_window = browser.current_window_handle
total_window_handles.append(original_window)


top_left = browser.find_elements(By.CSS_SELECTOR, "#s-top-left a")
# print(top_left[5].text)
top_left[5].click()


# 切换新的窗口
def switch_to_new_window(browser, total_window_handles, window_num):
    # 等待新窗口或标签页
    WebDriverWait(browser, 10).until(EC.number_of_windows_to_be(window_num))

    # 循环所有窗口句柄
    print(total_window_handles)
    for window_handle in browser.window_handles:
        if window_handle not in total_window_handles:
            # 切换到新窗口
            browser.switch_to.window(window_handle)
            break


switch_to_new_window(browser, original_window, 2)

second_window = browser.current_window_handle
total_window_handles.append(second_window)
# 现在我们在B页面上，可以操作其元素
try:
    # 例如，找到并点击B页面上的一个按钮
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "高清美图"))
    )
    button.click()
    print(browser.window_handles)
    switch_to_new_window(browser, total_window_handles, 3)
    thrird_window = browser.current_window_handle
    total_window_handles.append(thrird_window)
    print("Successfully clicked the button on page B")
except Exception as e:
    print(f"An error occurred: {e}")


def download_image():
    for _ in range(6):
        browser.execute_script(
            "document.documentElement.scrollTop = document.documentElement.scrollHeight"
        )
        time.sleep(2)
    imgs = browser.find_elements(By.CLASS_NAME, "albumsdetail-item-img")
    # print(imgs)
    with ThreadPoolExecutor(max_workers=10) as pool:
        for img in imgs:
            img_url = img.get_attribute("src")
            # print(img_url)
            pool.submit(download_img, img_url)


def download_img(url: str):
    u_index = url.rfind("u") + 2
    filename = url[u_index : u_index + 10]
    print(filename)
    os.makedirs(DOWNLOAD_PATH, exist_ok=True)
    resp = requests.get(url, stream=True)
    with open(os.path.join(DOWNLOAD_PATH, filename + ".jpg"), "wb") as file:
        shutil.copyfileobj(resp.raw, file)
    # with open(os.path.join(DOWNLOAD_PATH, filename + ".jpg"), "wb") as file:
    #     for chunk in resp.iter_content(chunk_size=8192):
    #         file.write(chunk)
    # with open(os.path.join(DOWNLOAD_PATH, filename + ".jpg"), "wb") as file:
    #     file.write(resp.content)


try:
    # 例如，找到并点击c页面上的
    a_tag = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "美女图片"))
    )
    a_tag.click()
    switch_to_new_window(browser, total_window_handles, 4)
    print("Successfully clicked the button on page C")
    download_image()
except Exception as e:
    print(f"An error occurred: {e}")


# browser.implicitly_wait(2)
print(browser.current_url)
time.sleep(600)
