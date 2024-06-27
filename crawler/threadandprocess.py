import time
from threading import Thread


def display(content):
    while True:
        print(content, end="", flush=True)
        time.sleep(0.1)


def main():
    Thread(target=display, args=("Ping",), daemon=True).start()
    Thread(target=display, args=("Pong",), daemon=True).start()
    # daemon=True 可以让这个线程编程保护线程，当主线程结束后，这些保护线程也会就会被销毁，不再继续运行
    time.sleep(5)


import concurrent.futures

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
] * 20


def is_prime(n):
    """判断素数"""
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n != 1


def main1():
    """主函数"""
    # with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
    #     for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
    #         print("%d is prime: %s" % (number, prime))

    with concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print("%d is prime: %s" % (number, prime))


if __name__ == "__main__":
    main1()
