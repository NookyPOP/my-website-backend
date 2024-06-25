class LoggingMixin:
    def log(self, msg):
        print(f"[LOG] {msg}")


class OrderProcessor:
    def process_order(self, order_id):
        print(f"Processing order {order_id}")


# extend functionality through mixin


class LoggedOrderProcessor(OrderProcessor, LoggingMixin):
    def process_order(self, order_id):
        self.log(f"starting order {order_id}")
        super().process_order(order_id)  # 可以通过继承的方式调用父类的方法，而不用初始化父类
        super().log(f"1111")
        self.log(f"finishing order {order_id}")


# use mixin
processor = LoggedOrderProcessor()
# processor.process_order(123)


# 自定义字典限制，只有在指定的key不存在的时候才允许添加


class SetOnceMappingMixin:
    # 定义混入类
    def __setitem__(self, key, value):  # 通过magic method 来定义mixin的类
        if key in self:
            raise KeyError(str(key) + " already exit")
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    pass


my_dict = SetOnceDict()

# print(my_dict)

try:
    my_dict["username"] = "jack"
    my_dict["username"] = "rose"
except KeyError:
    pass
# print(my_dict)

# print(type(OrderProcessor))
# # print(isinstance(OrderProcessor, object))
# # print(issubclass(OrderProcessor, object))

# print(isinstance(processor, LoggedOrderProcessor))  # true
# print(isinstance(LoggedOrderProcessor, object))  # true
# print(isinstance(str, object))  # true
# print(isinstance(object, type))  # true
# print(issubclass(LoggedOrderProcessor, object))  # true
# print(issubclass(str, object))  # true
# print(issubclass(object, type))  # false
# print(issubclass(type, object))  # true
# print(issubclass(LoggedOrderProcessor, OrderProcessor))  # true
# print(issubclass(OrderProcessor, LoggedOrderProcessor))  # false
import sys

print(isinstance([1], list), type([1]), type(list))
# True <class 'list'> <class 'type'>
print(isinstance(list, type))
# True
print(isinstance(sys, object), type(sys))
# True <class 'module'>
print(isinstance(object(), object), type(object()))

print(isinstance(object, type))
print(isinstance(object, object))
print(isinstance(type, object))
print(isinstance(type, type))

print(issubclass(list, object))  # True
print(issubclass(object, object))  # True
print(issubclass(type, type))  # True
print(issubclass(type, object))  # True


class MyMetaClass(type):
    pass


class MyClass(metaclass=MyMetaClass):
    pass


# print(MyClass, type(MyClass), MyMetaClass)


class MyIterator:
    def __init__(self, limit) -> None:
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return self.count

        else:
            raise StopIteration


# use the iterator

my_iter = MyIterator(5)
print(my_iter, type(my_iter))
print(next(my_iter))  # 1
print(next(my_iter))  # 2

for num in my_iter:
    print(num)


def fib(num):
    # 定义斐波那契数列,生成器来实现
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


#
gen = fib(5)
print(gen)  # <generator object fib at 0x102ad66c0>
next(gen)  # 1
next(gen)  # 1
print(next(gen))  # 2
print(next(gen))  # 3
for num in gen:
    print(num)  # 1 1 2 3 4


def calc_avg():
    """流式计算平均值"""
    total, counter = 0, 0
    avg_value = None
    while True:
        value = yield avg_value
        total, counter = total + value, counter + 1
        avg_value = total / counter


gen = calc_avg()
next(gen)
print(gen.send(11))
print(gen.send(20))
print(gen.send(30))
