# import socket module
from socket import *

if __name__ == '__main__':
    # 准备TCP套接字
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 将TCP套接字绑定到指定端口
    serverIP = '127.0.0.1'
    serverPort = 6789
    serverSocket.bind((serverIP, serverPort))
    # 设置最大连接数
    serverSocket.listen(1)

    while True:
        # 准备迎接客户端的连接
        print('Ready to serve...')
        # 接收到客户连接请求后，建立新的TCP连接套接字
        connectionSocket, addr = serverSocket.accept()
        try:
            # 获取客户发送的报文
            message = connectionSocket.recv(1024)
            # 获取客户端需要的文件名，根据html格式来进行切分
            filename = message.split()[1].decode()
            # 读取文件
            f = open(filename[1:], "r", encoding="utf-8")
            outputdata = f.read()
            # 发送http响应，记得要encode一下，因为网络传的是数据流，并在响应头设置好你设定的编码方式，比如utf-8
            # 200响应行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 响应头
            response_header = "Connection: close\r\nContent-Type: text/html\r\n"
            response_header += "Content-Length: %d\r\n" % len(outputdata)
            response_header += "charset: utf-8\r\n"
            # 空行
            empty = "\r\n"
            # 响应体
            response_body = outputdata
            # 拼接响应
            response = response_line + response_header + empty + response_body
            # 发送响应
            connectionSocket.send(response.encode())
            # 关闭连接
            connectionSocket.close()
        except IOError:
            # 找不到这个文件，返回404
            # 读取404页面文件
            f = open("404.html", "r", encoding="utf-8")
            outputdata = f.read()
            # 404响应行
            response_line = "HTTP/1.1 404 Not Found\r\n"
            # 响应头
            response_header = "Connection: close\r\nContent-Type: text/html\r\n"
            response_header += "Content-Length: %d\r\n" % len(outputdata)
            response_header += "charset: utf-8\r\n"
            # 空行
            empty = "\r\n"
            # 响应体
            response_body = outputdata
            # 拼接响应
            response = response_line + response_header + empty + response_body
            # 发送响应
            connectionSocket.send(response.encode())
            # 关闭连接
            connectionSocket.close()
    serverSocket.close()
