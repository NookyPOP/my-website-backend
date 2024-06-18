import socket


def clientupd():
    # 1. 创建一个udp套接字
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("192.168.68.98", 6789)

    # 2.发送数据
    try:
        while True:
            # 2.1 发送数据给服务器
            text = input("请输入要发送的数据:")
            client.sendto(text.encode(), server_address)
            # 如果用户输入'exit'，结束循环
            if text.strip().lower() == "exit":
                print("Client is exiting.")
                break
            # 3. 接受数据
            data, _ = client.recvfrom(1024)
            print(data.decode())
    finally:
        # 4. 关闭套接字
        client.close()


if __name__ == "__main__":
    clientupd()
