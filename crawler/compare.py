import requests
import os
import time
import json
from concurrent.futures import ThreadPoolExecutor
import aiohttp
import aiofile
import asyncio
from urllib.parse import urlparse

range_images = (1, 3)


def download_image(url: str):
    filename = url[url.rfind("/") + 1 :]
    resp = requests.get(url)
    if resp.status_code == 200:
        with open("images/" + filename, "wb") as f:
            f.write(resp.content)


def main():
    if not os.path.exists("images"):
        os.mkdir("images")
    for page in range_images:
        time_stamp = int(time.time() * 1000)
        paload = {
            "callback": "jQuery18303984010395160791_1719716137434",
            "q": "清新美女",
            "qtag": "吊带",
            "pd": "1",
            "pn": "60",
            "correct": "清新美女",
            "adstar": "0",
            "tab": "all",
            "sid": "dd0e1838e14930fad24783c19705af1a",
            "ras": "6",
            "cn": "0",
            "gn": "0",
            "kn": "0",
            "crn": "0",
            "bxn": "0",
            "cuben": "0",
            "pornn": "0",
            "manun": "0",
            "src": "resou",
            "sn": f"{page * 60}",
            "ps": f"{page * 60 - 2}",
            "pc": f"{page * 60 - 2}",
            "_": f"{time_stamp}",
        }
        resp = requests.get("https://image.so.com/j", params=paload)
        if resp.status_code == 200:
            # print(resp.text)
            content = resp.text[resp.text.find("{") : -2]
            # print(content)
            content_json = json.loads(content)
            lists = content_json["list"]
            for list in lists:
                download_image(list["thumb"])


def download_image1(url: str):
    filename = url[url.rfind("/") + 1 :]
    resp = requests.get(url)
    if resp.status_code == 200:
        with open("images/" + filename, "wb") as f:
            f.write(resp.content)


def main1():
    if not os.path.exists("images"):
        os.mkdir("images")
    with ThreadPoolExecutor(max_workers=20) as pool:
        for page in range_images:
            time_stamp = int(time.time() * 1000)
            paload = {
                "callback": "jQuery18303984010395160791_1719716137434",
                "q": "清新美女",
                "qtag": "吊带",
                "pd": "1",
                "pn": "60",
                "correct": "清新美女",
                "adstar": "0",
                "tab": "all",
                "sid": "dd0e1838e14930fad24783c19705af1a",
                "ras": "6",
                "cn": "0",
                "gn": "0",
                "kn": "0",
                "crn": "0",
                "bxn": "0",
                "cuben": "0",
                "pornn": "0",
                "manun": "0",
                "src": "resou",
                "sn": f"{page * 60}",
                "ps": f"{page * 60 - 2}",
                "pc": f"{page * 60 - 2}",
                "_": f"{time_stamp}",
            }
            resp = requests.get("https://image.so.com/j", params=paload)
            if resp.status_code == 200:
                # print(resp.text)
                content = resp.text[resp.text.find("{") : -2]
                # print(content)
                content_json = json.loads(content)
                lists = content_json["list"]
                for list in lists:
                    pool.submit(download_image1, list["thumb"])


async def download_image2(session, url: str):
    filename = url[url.rfind("/") + 1 :]
    async with session.get(url) as resp:
        if resp.status == 200:
            data = await resp.read()
            async with aiofile.async_open("images/" + filename, "wb") as f:
                await f.write(data)


async def fetch_img_url():
    async with aiohttp.ClientSession() as session:
        for page in range_images:
            time_stamp = int(time.time() * 1000)
            paload = {
                "callback": "jQuery18303984010395160791_1719716137434",
                "q": "清新美女",
                "qtag": "吊带",
                "pd": "1",
                "pn": "60",
                "correct": "清新美女",
                "adstar": "0",
                "tab": "all",
                "sid": "dd0e1838e14930fad24783c19705af1a",
                "ras": "6",
                "cn": "0",
                "gn": "0",
                "kn": "0",
                "crn": "0",
                "bxn": "0",
                "cuben": "0",
                "pornn": "0",
                "manun": "0",
                "src": "resou",
                "sn": f"{page * 60}",
                "ps": f"{page * 60 - 2}",
                "pc": f"{page * 60 - 2}",
                "_": f"{time_stamp}",
            }
            async with session.get("https://image.so.com/j", params=paload) as response:
                text = await response.text()
                content = text[text.find("{") : -2]
                content_json = json.loads(content)
                lists = content_json["list"]
                tasks = [download_image2(session, list["thumb"]) for list in lists]
                await asyncio.gather(*tasks)


async def main2():
    if not os.path.exists("images"):
        os.mkdir("images")
    await fetch_img_url()


# optimized version for aiohttp


async def download_image3(session, url: str, semophore: asyncio.Semaphore):
    async with semophore:
        filename = os.path.basename(urlparse(url).path)
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.read()
                    async with aiofile.async_open(
                        os.path.join("images", filename), "wb"
                    ) as file:
                        await file.write(data)
            return True  # success
        except asyncio.TimeoutError:
            print(f"Timeout downloading {url}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")
        return False  # failure


async def fetch_img_url3(session, page):
    time_stamp = int(time.time() * 1000)
    payload = {
        "callback": f"jQuery18303811092340553317_{time_stamp}",
        "q": "清新美女",
        "qtag": "泳装",
        "pd": "1",
        "pn": "60",
        "correct": "清新美女",
        "adstar": "0",
        "tab": "all",
        "sid": "822bcb8d30c4164da0e781467fe1b42f",
        "ras": "6",
        "cn": "0",
        "gn": "0",
        "kn": "0",
        "crn": "0",
        "bxn": "0",
        "cuben": "0",
        "pornn": "0",
        "manun": "0",
        "src": "resou",
        "sn": f"{page * 60}",
        "ps": f"{page * 60 - 2}",
        "pc": f"{page * 60 - 2}",
        "_": f"{time_stamp}",
    }
    try:
        async with session.get(
            "https://image.so.com/j", params=payload, timeout=10
        ) as response:
            text = await response.text()
            content = text[text.find("{") : -2]
            content_json = json.loads(content)
            return [list["thumb"] for list in content_json.get("list", [])]
    except asyncio.TimeoutError:
        print(f"Timeout fetching URLs for page {page}")
    except Exception as e:
        print(f"Error fetching URLs for page {page}: {e}")
    return []


async def main3():
    if not os.path.exists("images"):
        os.mkdir("images")
    connector = aiohttp.TCPConnector(ssl=False, limit=100)
    async with aiohttp.ClientSession(connector=connector) as session:
        semophore = asyncio.Semaphore(50)  # 设置最大并发数
        tasks = []
        for page in range_images:
            urls = await fetch_img_url3(session, page)
            tasks.extend([download_image3(session, url, semophore) for url in urls])

        results = await asyncio.gather(*tasks)
        print(f"Successfully downloaded {sum(results)} images.")


if __name__ == "__main__":
    start_time = time.time()
    # main()  # 用单线程 11.4s
    # main1()  # 用线程池 3.3s
    # asyncio.run(main2())
    asyncio.run(main3())  # 2.3s

    print(f"Total time: {time.time() - start_time} Seconds")
