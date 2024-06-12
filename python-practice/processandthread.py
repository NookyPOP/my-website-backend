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


if __name__ == "__main__":
    # main()
    # main1()
    main2()
