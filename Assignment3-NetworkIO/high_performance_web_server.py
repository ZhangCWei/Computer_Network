from socket import *
import threading


def thread_func(conn):
    # 接收客户端数据
    data = conn.recv(1024).decode()
    # 服务器发送响应，代表本次的数据结束
    conn.sendall('over'.encode())
    # 关闭客户端连接
    conn.close()


def multithreading_server_BIO(ip: str, port: int):
    # 创建服务器套接字，使用IPv4协议，TCP协议
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 绑定端口号和套接字
    serverSocket.bind((ip, port))
    # 开启监听，设置1024个连接缓冲，暂时将连接挂起
    serverSocket.listen(1024)
    print('The server is ready to receive')
    while True:
        # 等待接受客户端的连接
        conn, addr = serverSocket.accept()
        # print(addr)
        # 创建线程
        t = threading.Thread(target=thread_func, args=(conn,))
        t.start()

    serverSocket.close()


if __name__ == '__main__':
    # 服务器端口号
    serverPort = 12000
    multithreading_server_BIO('', serverPort)
