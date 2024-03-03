from socket import *

if __name__ == '__main__':
    # 服务器端口号
    serverPort = 11111
    # 创建服务器套接字，使用IPv4协议，TCP协议
    serverIP = '127.0.0.1'
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 绑定端口号和套接字
    serverSocket.bind((serverIP, serverPort))
    # 开启监听
    serverSocket.listen(1)
    print('The server is ready to receive')
    while True:
        # 等待接受客户端的连接
        connectionSocket, addr = serverSocket.accept()
        # 接受客户端的数据
        sentence = connectionSocket.recv(1024).decode()
        # 数据处理
        capitalizedSentence = sentence.lower()
        # 把结果发送回客户端
        connectionSocket.send(capitalizedSentence.encode())
        print(f"客户端{addr}发送的消息为{capitalizedSentence.encode()}")
        # 连接关闭
        connectionSocket.close()
