from socket import *
import time


if __name__ == '__main__':
    # 服务器的IP地址或主机名
    serverName = '127.0.0.1'
    # 服务器端口号
    serverPort = 12000
    # 创建客户套接字，使用IPv4协议，UDP协议
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    # 设置超时时间
    clientSocket.settimeout(5)
    for i in range(10):
        clientSocket.sendto(b"ping", (serverName, serverPort))
        send_time = time.time()

        try:
            message = clientSocket.recvfrom(1024)
            recv_time = time.time()
            print(f"Ping {i} RTT: {(recv_time-send_time):.2f}s")
        except timeout as e:
            print(f"Ping {i} RTT: lost")
    # 关闭客户套接字
    clientSocket.close()
