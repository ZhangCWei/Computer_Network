from socket import *
import time
if __name__ == '__main__':
    # Set the server's IP address and port
    serverName = '127.0.0.1'
    serverPort = 12000
    # Create a UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    # Set a timeout value of 1 second
    clientSocket.settimeout(5)
    # Ping 4 times
    print('正在 Ping ' + serverName + ' 具有32字节的数据:')
    # 统计信息
    num_timeout = 0
    num_normal = 0
    max_time = 0
    min_time = 5000
    total_time = 0

    for i in range(4):
        # Format the message with the current time
        message = 'Ping ' + str(i+1) + ' ' + str(time.time())
        # Send the message to the server
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        send_time = time.time()
        try:
            # Receive the response from the server
            modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
            recv_time = time.time()
            dtime = (recv_time - send_time)*1000
            if dtime > max_time:
                max_time = dtime
            if dtime < min_time:
                min_time = dtime
            total_time += dtime
            # Print the response
            print('来自 ' + serverName + '的回复：', end=' ')
            print('字节=32', end=' ')
            print(f"时间={dtime:.0f}ms")
            num_normal += 1
        except timeout:
            # Print a timeout message
            print('Request timed out')
            num_timeout += 1

    print(serverName + '的 Ping 统计信息：')
    print('\t数据包：已发送 = 4,' + '已接收 = ' + str(num_normal) + ', 丢失 = ' + str(num_timeout) + f'({num_timeout/4*100}%丢失）')
    print('往返行程的估计时间(以毫秒为单位)：')
    print(end='\t')
    print(f"最短={min_time:.0f}ms，最长={max_time:.0f}ms，平均={total_time/num_normal:.0f}ms")
    # Close the socket
    clientSocket.close()

