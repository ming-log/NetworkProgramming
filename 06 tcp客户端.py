# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/3 11:40
# tcp客户端
# tcp客户端，并不是像之前一个段子一个顾客去吃饭，这个顾客要点菜，就问服务员咱们饭店有客户端么，
# 然后这个服务器非常客气的说道:先生 我们饭店不用客户端，我们直接送到您的餐桌上
# 如果，不学习网络的知识是不是说不定也会发生那样的笑话
# 所谓的服务器端:就是提供服务的一方，而客户端，就是需要被服务的一方

# tcp客户端构建流程
# tcp 的客户端要比服务器端简单很多，如果说服务器端是需要自己买手机、插手机卡、设置铃声、等待别人
# 打电话流程的话，那么客户端就只需要我们找一个电话亭，拿起电话拨打即可，流程要少很多
from socket import *


def main():
    n = 1
    while True:
        # 创建socket
        tcp_client_socket = socket(AF_INET, SOCK_STREAM)

        # 目的信息
        # server_ip = input("请输入服务器ip:")
        server_ip = '127.0.0.1'
        # try:
        #     server_port = int(input("请输入服务器端口:"))
        # except Exception as e:
        #     print(e)
        server_port = 7788

        # 链接服务器
        tcp_client_socket.connect((server_ip, server_port))

        # 提示用户输入数据
        # send_data = input("请输入要发送的数据:")

        send_data = '数据条数:' + str(n)
        tcp_client_socket.send(send_data.encode("gbk"))

        n += 1
        # 接收对方发送过来的数据，最大接收1024个字节
        recv_data = tcp_client_socket.recv(1024)
        print("接收到的数据为:", recv_data.decode("gbk"))

    # 关闭套接字
    tcp_client_socket.close()


if __name__ == '__main__':
    main()
