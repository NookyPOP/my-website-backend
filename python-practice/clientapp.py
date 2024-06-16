from socket import socket
from json import loads
from base64 import b64decode


def main():
    # 1. 创建一个socket对象， 默认，family=AF_INET, type=SOCK_STREAM
    client = socket()

    # 2. 连接服务器
    client.connect(("192.168.68.98", 6789))

    # 3. 从服务器接收数据
    text = client.recv(1024).decode("utf-8")

    # 4. 打印接收到的数据
    print(text)
    print("客户端退出...")

    # 5. 关闭套接字
    client.close()


def main1():
    # 1. 创建一个socket对象
    client = socket()
    # 2. 连接服务器
    client.connect(("192.168.68.98", 6789))
    # 定义一个保存二进制数据的对象
    in_data = bytes()
    # print(1, in_data[0:100], type(in_data))
    # 1 b'' <class 'bytes'>
    # 由于不知道文件的大小， 所以一次性将传输的二进制数据拼接起来， 直到传输完毕
    data = client.recv(1024)
    # print(2, data[:100], type(data))
    # 2 b'{"filename": "code.png", "filedata": "iVBORw0KGgoAAAANSUhEUgAAA0sAAAG9CAIAAABLcnoMAAAACXBIWXMAAAsTAA' <class 'bytes'>
    while data:
        # 3. 从服务器接收数据， 1024代表每次接收的最大数据量
        in_data += data
        data = client.recv(1024)

    # 将接收到的二进制数据解码为字符串
    # print(3, in_data[:200], type(in_data))
    # b'{"filename": "code.png", "filedata": "iVBORw0KGgoAAAANSUhEUgAAA0sAAAG9CAIAAABLcnoMAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAEXRFWHRTb2Z0d2Fy
    # ZQBTbmlwYXN0ZV0Xzt0AACAASURBVHhe7N13VBRXFwDwO7N9F1g6KCJVwN5ABLEiVrB31M' <class 'bytes'>
    text = in_data.decode("utf-8")  # 将二进制数据解码为字符串
    # print(4, text[:100], type(text))
    # 4 {"filename": "code.png", "filedata": "iVBORw0KGgoAAAANSUhEUgAAA0sAAAG9CAIAAABLcnoMAAAACXBIWXMAAAsTAA <class 'str'>
    # 使用loads函数将JSON格式的字符串转换为python对象
    obj = loads(text)
    # print(5, obj, type(obj))
    # 5 {'filename': 'code.png', 'filedata': 'iVBORw0KGgoAAAANSUhEUgAAA0sAAAG9CAIAAABLcnoMAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAEXRFWHRTb2Z0d2FyZQBTbml
    # wYXN0ZV0Xzt0AACAASURBVHhe7N13VBRXFwDwO7N9F1g6KCJVwN5ABLEiVrB31M'} <class 'dict'>
    filename = obj["filename"]
    # print(6, filename, type(filename))
    # 6 code.png <class 'str'>
    filedata_str = obj["filedata"]
    # print(7, filedata_str[:100], type(filedata_str))
    # 7 iVBORw0KGgoAAAANSUhEUgAAA0sAAAG9CAIAAABLcnoMAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAEXRFWHRTb2Z0d2FyZQBTbmlw <class 'str'>
    filedata_bytes = filedata_str.encode("utf-8")
    # print(8, filedata[:100], type(filedata))
    # 8 b'iVBORw0KGgoAAAANSUhEUgAAA0sAAAG9CAIAAABLcnoMAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAEXRFWHRTb2Z0d2FyZQBTbmlw' <class 'bytes'>
    with open("/Users/kevin/Desktop/my-website/python-practice/" + filename, "wb") as f:
        # 将base64格式的数据解码成二进制数据并写入文件
        base64 = b64decode(filedata_bytes)
        # print(9, base64[0:100], type(base64))
        # 9 b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x03K\x00\x00\x01\xbd\x08\x02\x00\x00\x00Krz\x0c\x00\x00\x00\tpHYs\x00\x00\x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\x11tEXtSoftw
        # are\x00Snipaste]\x17\xce\xdd\x00\x00 \x00IDATx^\xec\xddwT\x14W\x17' <class 'bytes'>
        f.write(base64)
    print("接收文件成功")


if __name__ == "__main__":
    # main()
    main1()
