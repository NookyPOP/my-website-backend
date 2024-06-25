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

print(issubclass(list, object)) # True
print(issubclass(object, object))  # True
print(issubclass(type, type))  # True
print(issubclass(type, object))  # True


class MyMetaClass(type):
    pass


class MyClass(metaclass=MyMetaClass):
    pass


# print(MyClass, type(MyClass), MyMetaClass)
