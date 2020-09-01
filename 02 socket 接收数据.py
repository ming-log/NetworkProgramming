# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author: Ming Luo
# time: 2020/9/1 10:59

from socket import *

# 1. 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 2. 绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
# 绑定端口
local_addr = ('', 7789)   # ip地址和端口号，ip一般不用写，表示本地的任何一个ip
udp_socket.bind(local_addr)  # 必须绑定自己电脑的ip以及port，其他的不行

# 3. 等待接收对方发送的数据
while True:
    recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
    # recv_data 这个变量中存储的是一个元组(接收到的数据、(发送方的ip、端口port))

    # 4. 显示接收到的数据
    print(recv_data[0].decode('gbk'))  # windows 默认中文编码方式为gbk
    print("发送方ip:", recv_data[1][0])
    print("发送方端口:", recv_data[1][1])
    print("-" * 30)

# 5. 关闭程序
udp_socket.close()
