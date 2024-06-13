from time import time, sleep
from random import randint
from os import getpid
from multiprocessing import Process
from threading import Thread, Lock


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


class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposite(self, money):
        # 给资源账户加个锁，然后每次存钱的时候需要加锁
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 加完锁后，执行完代码，开是释放锁的操作，保证正常和异常的锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        # 当任何一个进程访问资源时候，需要得到一个资源的锁，才可以访问资源，否则会被阻塞
        self._account.deposite(self._money)


def main2():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("账户余额：¥ %d 元" % account.balance)


# thread
if __name__ == "__main__":
    # main()
    # main1()
    main2()
