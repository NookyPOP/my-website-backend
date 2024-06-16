from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime
from threading import Thread
from json import dumps
from base64 import b64encode


def main():
    # 1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址, family is optional and defaults to AF_INET
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字

    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.绑定IP地址和端口(端口用于区分不同的服务)
    # 同一时间在同一个端口上只能绑定一个服务器, 多次绑定会报错
    server.bind(("192.168.68.98", 6789))
    # 3. 开始进行服务器的监听， 监听客户端连接到服务器
    server.listen(512)  # 512: 每个连接的客户端最大的数据包数量
    print("服务器启动开始监听...")
    while True:
        # 4 通过循环的方式接受客户端的连接并作出相应的处理， accept()会等待并返回一个客户端的连接
        # accept 方法是一个阻塞方法， 如果没有客户端连接将一直卡住，不执行后面的代码
        # accept 返回一个元组, 第一个元素是客户端的socket对象, 第二个元素是连接客户端的地址(由IP和端口两部分组成)
        client, address = server.accept()
        print("连接到客户端:", address)
        # 5, 发送数据到客户端
        client.send(str(datetime.now()).encode("utf-8"))
        # 6, 关闭客户端
        client.close()


# creating a server with threading


def main1():
    # 自定义线程类
    class FileTransferHandler(Thread):
        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):  # 重写父类run方法, 实现子线程要运行的代码, 子线程要执行的代码
            file_dict = {}
            file_dict["filename"] = "code.png"
            file_dict["filedata"] = data  # data是通过base64编码后，再经过decode后的字符串
            # print(1, data[0:100], type(data))
            # 1 iVBORw0KGgoAAAANSUhEUgAAA0sAAAG9CAIAAABLcnoMAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAEXRFWHRTb2Z0d2FyZQBTbmlw <class 'str'>
            # JSON 是纯文本，所以不能携带二进制数据，需要使用Base64编码
            file_str = dumps(file_dict)
            # print(2, file_str[0:100], type(file_str))
            # 2 {"filename": "code.png", "filedata": "iVBORw0KGgoAAAANSUhEUgAAA0sAAAG9CAIAAABLcnoMAAAACXBIWXMAAAsTAA <class 'str'>
            # 使用encode将字符串转换为二进制数据
            str_encode = file_str.encode("utf-8")
            # 将字符串转换为二进制数据 # The encoding in which to encode the string.
            print(3, str_encode[0:100], type(str_encode))
            # 3 b'{"filename": "code.png", "filedata": "iVBORw0KGgoAAAANSUhEUgAAA0sAAAG9CAIAAABLcnoMAAAACXBIWXMAAAsTAA' <class 'bytes'>
            self.cclient.send(str_encode)  # 使用encode将字符串转换为二进制数据，再发送
            self.cclient.close()

    # 1. 创建一个socket对象
    server = socket()
    # 2. 绑定IP地址和端口
    server.bind(("192.168.68.98", 6789))
    # 3. 开始监听
    server.listen(512)
    print("服务器启动开始监听...")
    try:
        with open("python-practice/code.png", "rb") as f:
            read_data = f.read()  # data是二进制数据
            # print(4, data[0:100], type(data), end="\n\n")
            # 4 b'\x89PNG\r\n\x1a\n\x00\x00' <class 'bytes'>
            # 将二进制数据处理成base64编码的字符串
            # Base64是一种用于将二进制数据编码为ASCII字符串的编码方法, 编码后的二进制数据通常用于存储或传输
            base64_data = b64encode(read_data)  # b64encode将二进制数据转换为base64编码
            # print(5, base64_data[:100], type(base64_data), end="\n\n")
            # 5 b'iVBORw0KGgoAAAANSUhEUgAAA0sAAAG9CAIAAABLcnoMAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAEXRFWHRTb2Z0d2FyZQBTbmlw' <class 'bytes'>
            # 将base64编码的二进制数据转换为字符串, 方便发送, 使用decode的原因是将二进制数据转换为字符串
            base64_str = base64_data.decode("utf-8")
            # 将base64编码的二进制数据转换为字符串 # The encoding with which to decode the bytes.
            # print(6, base64_str[:100], type(base64_str), end="\n\n")
            # 6 iVBORw0KGgoAAAANSUhEUgAAA0sAAAG9CAIAAABLcnoMAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAEXRFWHRTb2Z0d2FyZQBTbmlw <class 'str'>
            data = base64_str

            # 总结：服务器和客户端的发送和接受的数据是二进制数据，如果需要是字典，需要先将字典转换为json格式的字符串，再转换为二进制数据
            # 如果字典的某个value是二进制数据， 那么需要先将二进制数据转换为base64编码的二进制数据，再使用decode转成字符串
    except Exception as e:
        print(11, e)
    while True:
        # 4. 等待客户端连接
        client, address = server.accept()
        print("连接到客户端:", address)
        # 5. 与客户端通信
        t = FileTransferHandler(client)
        t.start()


if __name__ == "__main__":
    # main()
    main1()
