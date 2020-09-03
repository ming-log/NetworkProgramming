# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/3 14:17
from socket import *


def main():
    # 创建socket
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)

    # 本地信息
    address = ('', 7788)

    # 绑定
    tcp_server_socket.bind(address)

    # 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
    tcp_server_socket.listen(128)  # 允许很多客户端连接

    n = 1
    while True:
        print('---- 空闲中 ----')
        # 监听套接字 负责 等待有新的客户端进行连接
        # accept产生的新的套接字用来 为客户端服务
        client_socket, client_addr = tcp_server_socket.accept()
        print('---- 工作中 ----')
        while True:
            # 接收对方发送过来的数据
            recv_data = client_socket.recv(1024).decode("gbk")  # 接收1024个字节
            print("recv_data：", recv_data)

            # 如果recv解堵塞，那么有2种方式:
            # 1. 客户端发送过来数据
            # 2. 客户端调用close导致，这里recv解堵塞recv_data将为空
            if not recv_data:
                break
            print('接收到的数据为:', recv_data)

            return_data = "thank you !-----" + str(n)
            # 发送一些数据到客户端
            client_socket.send(return_data.encode('gbk'))
            n += 1

        print('---- 客户%s服务完毕 ----' % str(client_addr))
        # 关闭为这个客户端服务的套接字,只要关闭了，就意味着不能再为这个客户端服务了，如果还需要服务，只能再次访问
        client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
