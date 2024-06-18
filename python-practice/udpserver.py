from socket import socket, AF_INET, SOCK_DGRAM


def main():
    # 1. 创建一个udp套接字
    server = socket(AF_INET, SOCK_DGRAM)
    # 2. 绑定ip和port
    server.bind(("192.168.68.98", 6789))
    print("服务器开始监听...on 192.168.68.98 port 6789")
    # 3. 接收数据
    while True:
        # 接受upd客户端发送过来的数据
        data, addr = server.recvfrom(1024)
        print(f"Received message: {data.decode()} from {addr}")
        # 发送响应给客户端
        response = f"Echo: {data.decode()}"
        server.sendto(response.encode(), addr)
        # 服务器可以选择性地结束循环以退出
        if data.decode().strip().lower() == "exit":
            print("Server is shutting down.")
            break

    server.close()
