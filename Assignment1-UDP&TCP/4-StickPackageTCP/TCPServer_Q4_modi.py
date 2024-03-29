import socket
import struct
import random
from socket import *


def get_random_buffer_size():
    return random.randint(0, 5) + 1


if __name__ == '__main__':
    # 服务器端口号
    serverPort = 12005
    # 创建服务器套接字，使用IPv4协议，TCP协议
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 设置端口重用，以便服务能迅速重启
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 绑定端口号和套接字
    serverSocket.bind(('', serverPort))
    # 开启监听
    serverSocket.listen(1)
    print('The server is ready to receive')
    while True:
        # 等待接受客户端的连接
        connectionSocket, addr = serverSocket.accept()
        # 设置mes编号
        mes_idx = 1
        # 不断处理客户端的请求
        while True:
            # 接受客户端的数据长度
            length_bytes = connectionSocket.recv(4)
            length = struct.unpack('!i', length_bytes)[0]
            # 接受客户端的数据
            sentence = ""
            while len(sentence) < length:
                if length - len(sentence) >= 5:
                    sentence += connectionSocket.recv(get_random_buffer_size()).decode('utf-8')
                else:
                    sentence += connectionSocket.recv(length - len(sentence)).decode('utf-8')
            sen = sentence[0: length]
            # 输出客户端发来的数据
            print('server get mes{}: {}'.format(mes_idx, sen.replace('\0', '')))
            # 若以\0为结束，则停止监听
            if sen.endswith('\0'):
                print('server end listening from client')
                break
            mes_idx += 1
        # 连接关闭
        connectionSocket.close()
