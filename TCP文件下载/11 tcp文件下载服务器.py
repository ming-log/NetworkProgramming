# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/3 16:44
from socket import *


def send_file_2_client(client_socket, client_addr):
    # 接收对方发送过来的,要下载的文件名
    file_name = client_socket.recv(1024).decode('utf-8')  # 接收1024个字节
    print('客户端%s需要下载的文件是:%s' % (str(client_addr), file_name))

    file_content = None
    try:
        f = open(file_name, 'rb')
        file_content = f.read()
    except Exception as e:
        print("没有要下载的文件(%s)" % file_name)

    # 发送一些数据到客户端
    # client_socket.send("thank you !".encode('gbk'))
    if file_content:
        client_socket.send(file_content)


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
    while True:
        client_socket, client_addr = tcp_server_socket.accept()
        send_file_2_client(client_socket, client_addr)

        # 关闭为这个客户端服务的套接字,只要关闭了，就意味着不能再为这个客户端服务了，如果还需要服务，只能再次访问
        client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()








