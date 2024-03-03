import select
import socket


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12000))
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.listen(1024) 

    # 将服务器套接字加入等待读就绪的套接字列表
    inputs = [server_socket]   

    while True:
        # 调用select()函数，阻塞等待      
        readable, _, _ = select.select(inputs, [], [])
        # 数据抵达，循环
        for temp_socket in readable:
            # 监听到有新的连接
            if temp_socket == server_socket:
                client_socket, client_address = server_socket.accept()
                # print(f"New client connected from {client_address}")
                # 将新的客户端套接字加入待处理列表
                inputs.append(client_socket)

            # 有数据到达
            else:
                # 读取客户端连接发送的数据
                data = temp_socket.recv(1024)
                # 若有数据递达，对数据进行处理
                if data:
                    # print(f"Received {len(data)} bytes from client {temp_socket.getpeername()}: {data}")
                    temp_socket.sendall(data)
                # 若未接收到数据，断开连接
                else:
                    # 从待处理列表中删除该套接字
                    inputs.remove(temp_socket)
                    # 若未接收到数据，断开连接
                    # print(f"Client {temp_socket.getpeername()} closed the connection.")
                    temp_socket.close()
    server_socket.close()


if __name__ == '__main__':
    main()