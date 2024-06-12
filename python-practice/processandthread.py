from time import time, sleep
from random import randint
from os import getpid
from multiprocessing import Process


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


if __name__ == "__main__":
    # main()
    main1()
