# 创建一个udp socket(udp套接字)
import socket


def main():
    # 1. 创建udp的套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # socket.AF_INET  使用ipv4协议
    # socket.SOCK_DGRAM  指UDP

    # 2. 绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
    local_addr = ('', 7788)  # ip地址和端口号，ip一般不用写，表示本地的任何一个ip
    udp_socket.bind(local_addr)  # 必须绑定自己电脑的ip以及port，其他的不行

    # 3. 准备接收方的地址
    # '192.168.1.103'标识目的ip地址
    # 8080表示目的的端口
    dest_addr = ('192.168.1.2', 8080)  # 注意 是元组， ip是字符串， 端口是数字
    while True:
        # 4. 从键盘获取数据
        send_data = input("请输入要发送的数据:")

        # 发送数据到指定的电脑上的指定程序中
        udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
        if send_data == '0':
            break
    # 关闭套接字
    udp_socket.close()
    print("---- run ----")


if __name__ == "__main__":
    main()
