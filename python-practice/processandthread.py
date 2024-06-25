from time import time, sleep
from random import randint
from os import getpid
from multiprocessing import Process, Queue


def download_task(filename):
    print("start process, and process number is [%d]" % getpid())
    print("start downloading %s" % filename)
    time_download = randint(2, 5)
    sleep(time_download)
    print("finish downloading %s take %ds" % (filename, time_download))


def main():
    start = time()
    download_task("love.pdf")
    download_task("hate.pdf")
    end = time()
    print("total take %ds", (end - start))


def main1():
    start = time()
    p1 = Process(target=download_task, args=("python.pdf",))
    p1.start()
    p2 = Process(target=download_task, args=("js.pdf",))
    p2.start()  # 启动进程
    p1.join()
    p2.join()  # 等待进程执行结束
    end = time()
    print("total %ds" % (end - start))


# counter = 0


def sub_task1(string, queue):
    while True:
        counter = queue.get()
        if counter >= 10:
            break
        print(string, end="", flush=True)
        queue.put(counter + 1)
        sleep(0.01)


def sub_task(string, queue):
    while True:
        counter = queue.get()
        if counter is None:  # 接收到 None 消息时退出
            break
        if counter >= 10:
            queue.put(None)  # 让其他进程也能退出
            break
        print(string, end="", flush=True)
        queue.put(counter + 1)
        sleep(0.01)


def main2():
    queue = Queue()
    queue.put(0)

    p1 = Process(target=sub_task, args=("Ping", queue))
    p2 = Process(target=sub_task, args=("Pong", queue))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # queue.get()


# 多进程 密集任务类型 计算密集


def main3():
    total = 0
    start = time()
    number_list = [x for x in range(1, 100000001)]
    for i in number_list:
        total += i
    end = time()
    print(total, (end - start))


def handler_calulate(num_list, queue):
    total = 0
    for i in num_list:
        total += i
    queue.put(total)


def main4():
    number_list = [x for x in range(1, 100000001)]
    queue = Queue()
    processes = []
    index = 0
    start = time()

    for _ in range(8):
        p = Process(
            target=handler_calulate, args=(number_list[index : index + 12500000], queue)
        )
        index += 12500000
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    total = 0
    while not queue.empty():
        total += queue.get()
    end = time()
    print(total, (end - start))


import os
import glob
import threading
from PIL import Image

PREFIX = "python-practice/thumbnails"


def generate_thumbnail(infile, size):
    file, ext = os.path.splitext(infile)
    file = file[file.rfind("/") + 1 :]
    outfile = f"{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}"
    img = Image.open(infile)
    img.thumbnail(size)
    img.save(outfile, format)


def main5():
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    for infile in glob.glob("python-practice/*.png"):
        for size in (32, 64, 128, 256):
            threading.Thread(
                target=generate_thumbnail, args=(infile, (size, size))
            ).start()


"""
多个线程竞争一个资源 - 保护临界资源 - 锁（Lock/RLock）
多个线程竞争多个资源（线程数>资源数） - 信号量（Semaphore）
多个线程的调度 - 暂停线程执行/唤醒等待中的线程 - Condition
"""
from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep

import threading


class Account:
    """银行账户"""

    def __init__(self, balance=0):
        self.balance = balance  # 一个资源
        lock = threading.RLock()  # 一个锁来保护临近资源
        self.condition = threading.Condition(lock)  # 一个条件变量来暂停/唤醒线程

    def withdraw(self, money):
        """取钱"""
        with self.condition:
            while money > self.balance:
                self.condition.wait()  # 阻塞线程 直到有钱
            new_balance = self.balance - money
            sleep(0.001)
            self.balance = new_balance

    def deposit(self, money):
        """存钱"""
        with self.condition:
            new_balance = self.balance + money
            sleep(0.001)
            self.balance = new_balance
            self.condition.notify_all()  # 唤醒阻塞的线程


def add_money(account):
    while True:
        money = randint(5, 10)
        account.deposit(money)
        print(threading.current_thread().name, ":", money, "====>", account.balance)
        sleep(0.5)


def sub_money(account):
    while True:
        money = randint(10, 30)
        account.withdraw(money)
        print(threading.current_thread().name, ":", money, "<====", account.balance)
        sleep(1)


def main6():
    account = Account()
    with ThreadPoolExecutor(max_workers=15) as pool:
        for _ in range(5):
            pool.submit(add_money, account)
        for _ in range(10):
            pool.submit(sub_money, account)


if __name__ == "__main__":
    # main()
    # main1()
    # main2()
    # main3()
    # main4()
    # main5()
    main6()
