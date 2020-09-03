# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/3 13:29

# tcp服务器
# 生活中的电话机
# 如果想让别人能够打通咱们的电话获取相应服务的话，需要做以下几件事情:
# 1. 买个手机
# 2. 插上电话卡
# 3. 设计手机为正常接听状态(即能够响铃)
# 4. 静静的等着别人拨打

# 如同上面的电话机过程一样，在程序中，如果想要完成一个tcp服务器的功能
# 需要的流程如下：
# 1. socket创建一个套接字
# 2. bind绑定ip和port
# 3. listen使套接字变为可以被动链接
# 4. accept等待客户端的链接
# 5. recv/send 接收发送数据

# 一个简单的tcp服务器如下
from socket import *


def main():
    # 创建socket
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)

    # 本地信息
    address = ('', 7788)

    # 绑定
    tcp_server_socket.bind(address)

    # 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
    tcp_server_socket.listen(128)

    # 监听套接字 负责 等待有新的客户端进行连接
    # accept产生的新的套接字用来 为客户端服务
    # 如果有新的客户端链接服务器，那么就产生一个新的套接字专门为这个客户端服务
    # client_socket 用来为这个客户端服务
    # tcp_server_socket就可以省下来专门等待其他新客户端的链接
    client_socket, client_addr = tcp_server_socket.accept()

    # 接收对方发送过来的数据
    recv_data = client_socket.recv(1024)  # 接收1024个字节
    print('接收到的数据为:', recv_data.decode("gbk"))

    # 发送一些数据到客户端
    client_socket.send("thank you !".encode('gbk'))

    # 关闭为这个客户端服务的套接字,只要关闭了，就意味着不能再为这个客户端服务了，如果还需要服务，只能再次访问
    client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
