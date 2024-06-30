import requests
import time

# import re
import bs4
import lxml
import asyncio
import aiohttp

"""

使用 with 和 async with 的原因:

上下文管理：
with 语句背后的概念是上下文管理（context management）。上下文管理器可以分配和释放资源，确保在使用期间和使用完毕后资源得到正确处理。
对于同步代码，可以使用 with，对于异步代码，则使用 async with。

清理资源：
常见的使用场景包括文件操作、网络连接和锁。在你提供的代码中，涉及的是网络连接。
async with aiohttp.ClientSession() as session: 确保在会话完成后自动关闭网络连接，防止资源泄漏。

确保异常安全：
如果在使用资源的过程中抛出异常，with 和 async with 都可以确保进入和退出资源管理器时的代码能够被执行，从而帮助正确清理资源。
这有助于避免因为异常而导致的资源泄漏和其他不可预见的问题。

"""


# using aiohttp and bs4 to fetch page title by asynchronously
# 使整个 HTTP 请求过程完全异步化，无需依赖线程池实现
async def fetch_page_title2(session, url):
    async with session.get(url, headers={"User-Agent": "BaiduSpider"}) as response:
        text = await response.text()
        soup = bs4.BeautifulSoup(text, "lxml")
        title = soup.select("html > head > title")
        print(title[0].text if title else "No title found")


async def main2():
    print("start")
    start_time = time.time()
    urls = [
        "https://www.python.org/",
        "https://www.jd.com/",
        "https://www.baidu.com/",
        "https://www.taobao.com/",
        "https://git-scm.com/",
        "https://www.sohu.com/",
        "https://gitee.com/",
        "https://www.amazon.com/",
        "https://www.usa.gov/",
        "https://www.nasa.gov/",
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page_title2(session, url) for url in urls]
        await asyncio.gather(*tasks)  # gather 同时执行 tasks, 并发运行所有任务，并等待它们全部完成。

    print("done")
    end_time = time.time()
    print(end_time - start_time)


# using requests and bs4 to fetch page title by asynchronously
# requests + asyncio.to_thread：需要将同步 I/O 包装成异步调用，导致增加额外的线程管理开销。
async def fetch_page_title(session, url):
    # 使用 to_thread 将阻塞的请求放到线程池中执行
    response = await asyncio.to_thread(
        session.get, url, headers={"User-Agent": "BaiduSpider"}
    )
    # 线程池：使用 asyncio.to_thread 将阻塞操作放到线程池中执行，避免阻塞事件循环。
    text = response.text
    soup = bs4.BeautifulSoup(text, "lxml")
    title = soup.select("html > head > title")
    print(title[0].text)


async def main():
    print("start")
    start_time = time.time()
    urls = [
        "https://www.python.org/",
        "https://www.jd.com/",
        "https://www.baidu.com/",
        "https://www.taobao.com/",
        "https://git-scm.com/",
        "https://www.sohu.com/",
        "https://gitee.com/",
        "https://www.amazon.com/",
        "https://www.usa.gov/",
        "https://www.nasa.gov/",
    ]

    session = requests.Session()  # 创建会话 这个是同步的
    tasks = [fetch_page_title(session, url) for url in urls]
    await asyncio.gather(*tasks)  # 并发运行所有任务，并等待它们全部完成。
    print("done")
    end_time = time.time()
    print(end_time - start_time)


# using requests and bs4 to fetch page title by synchronously
def fetch_page_title1(url):
    response = requests.get(url, headers={"User-Agent": "BaiduSpider"})
    text = response.text
    soup = bs4.BeautifulSoup(text, "lxml")
    title = soup.select("html > head > title")
    print(title[0].text)


def main1():
    start = time.time()

    urls = [
        "https://www.python.org/",
        "https://www.jd.com/",
        "https://www.baidu.com/",
        "https://www.taobao.com/",
        "https://git-scm.com/",
        "https://www.sohu.com/",
        "https://gitee.com/",
        "https://www.amazon.com/",
        "https://www.usa.gov/",
        "https://www.nasa.gov/",
    ]

    for url in urls:
        fetch_page_title1(url)
    time.sleep(1)
    end = time.time()
    print("total %ds" % (end - start))
    # total 6s


if __name__ == "__main__":
    # asyncio.run(main())
    # main1()
    asyncio.run(main2())  # asyncio.run(main()) 启动异步事件循环并运行主协程 main()
