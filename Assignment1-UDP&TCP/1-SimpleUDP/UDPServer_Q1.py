from socket import *

if __name__ == '__main__':
    # 服务器端口号
    serverPort = 12005
    # 创建服务器套接字，使用IPv4协议，UDP协议
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    # 绑定端口号和套接字
    serverSocket.bind(('', serverPort))
    # 提示信息serverSocket = socket(AF_INET, SOCK_DGRAM)
    print("The server is ready to receive")
    # 进程一直运行，等待分组到达
    while True:
        # 接收报文
        message, clientAddress = serverSocket.recvfrom(1024)
        # 处理
        modifiedMessage = message.decode().upper()
        # 发送报文
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
