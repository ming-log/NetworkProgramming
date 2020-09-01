# 创建一个udp socket(udp套接字)
import socket


def main():
    # 1. 创建udp的套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # socket.AF_INET  使用ipv4协议
    # socket.SOCK_DGRAM  指UDP

    dest_ip = input("请输入对方的IP:")
    try:
        dest_port = int(input("请输入对方的port:"))
    except Exception as e:
        print(e)

    # ... 这里是使用套接字的功能...
    # 2. 准备接收方的地址
    # '192.168.1.103'标识目的ip地址
    # 8080表示目的的端口
    dest_addr = (dest_ip, dest_port)  # 注意 是元组， ip是字符串， 端口是数字
    while True:
        # 3. 从键盘获取数据
        send_data = input("请输入要发送的数据:")
        if send_data == '0':
            break
        # 发送数据到指定的电脑上的指定程序中
        udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

        # 接收回送过来的数据
        recv_data = udp_socket.recvfrom(1024)
        # 套接字可以同时收发数据 、
        print("recv_data:", recv_data[0].decode("gbk"))
    # 关闭套接字
    udp_socket.close()
    print("---- Exit ----")


if __name__ == "__main__":
    main()

# 单工   半双工   全双工
# 1. 单工
# 数据只在一个方向上传输，不能实现双方通信
# 例子:电视、广播
# 2. 半双工
# 允许数据在两个方向传播，但是同一时间数据只能在一个方向传输，其实际上是可以切换的单工
# 例子:对讲机
# 3. 全双工
# 允许数据在两个方向上同时传输
# 例子:手机通话
