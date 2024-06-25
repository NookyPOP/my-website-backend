item1 = list(map(lambda x: x**2, filter(lambda x: x % 2, range(1, 10))))
# print(item1)


# 可变参数
def sum_all(*args):  # *args 设置为可变参数，把参数打包成tuple
    print(args)
    return sum(args)


# print(sum_all(1, 3, 4, 5, 6))

# 关键字参数
""" 将不定量的关键字参数打包为一个字典传递给函数 """


def print_person(**kwargs):  # name,age,location 等于 **kwargs
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)


# print_person(name="Alice", age=32, location="wonderland")

# 命名关键字参数
""" 命名关键字参数出现在*之后，用于限制关键字参数，使其必须使用关键词来传递，关键字后面不能更位置参数 """


def func(a, *, b):
    return a + b


print(func(1, b=2))


x = "global"


def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()
    print(x)


outer()
print(x)


x = "global"


def func():
    global x
    x = "modified"


func()
print(x)


def outer():
    x = "enclosing"

    def inner():
        nonlocal x
        x = "modified"

    inner()

    print(x)


# outer()

from functools import wraps
from time import time, sleep
from random import randint
from typing import Any


# def record_time(output):
def record_time(fn):
    """自定义装饰函数的装饰器"""

    @wraps(fn)
    # download_task function,using the wraps to preserve the metadata of the original function.
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        print(f"{fn.__name__}: {time() - start}秒")
        return result

    return wrapper
    # def decorator(fun):
    #     @wraps(fun)
    #     def wrapper(*args, **kwargs):
    #         start = time()
    #         result = fun(*args, **kwargs)
    #         print(f"{fun.__name__}: {time() - start}秒")
    #         # fun name is metadata of the original function
    #         return result

    #     return wrapper

    # return decorator


# @record_time(11)
@record_time
# @record_time，不使用参数花的装饰器，会自动执行装饰器函数，把被装饰的函数会作为参数传入， 在装饰器函数里执行原函数
# @record_time("11") 使用参数化的装饰器，会先执行这个装饰器函数，然后再自动执行装饰器返回的函数
def download_task(filename):
    print("start process, and process number is [%d]")
    print("start downloading %s" % filename)
    time_download = randint(2, 5)
    sleep(time_download)
    print("finish downloading %s take %ds" % (filename, time_download))

    return time_download


# download_task("love.pdf")


class Record:
    """通过定义类的方式来定义装饰器"""

    def __init__(self, output) -> None:
        self.output = output

    def __call__(self, func) -> Any:
        # self.output(func.__wrapped__)

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            self.output(f"{func.__name__}: {time() - start}秒")

            return result

        return wrapper


@Record(output=print)
# 通过类的方式来定义装饰器，等价于 record_time = Record(output=print)(download_task)
def download_task(filename):
    print("start process, and process number is [%d]")
    print("start downloading %s" % filename)
    time_download = randint(2, 5)
    sleep(time_download)
    print("finish downloading %s take %ds" % (filename, time_download))

    return time_download


# download_task("loveandhate.pdf")


def singleton(cls):
    """装饰类的装饰器"""
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


# @singleton
class Person:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __dict__(self):
        # strs= f'{'name':self.name}'
        # print id
        print(id(self.name))
        return {"name": self.name}


p1 = Person("kevin1")  # {name:kevin}
# p2 = Person("kevin2")
# print(p1 is p2)

print(p1, p1.__dict__)
