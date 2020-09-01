"""
只能实现发送一条接收一条，一次只能执行发送和接收中的一个操作
要想实现边发送边接收需要使用多任务
"""
import socket


def send_msg(udp_socket):
    """获取键盘数据，并将其发送给对方"""
    # 1. 从键盘输入数据
    msg = input("\n请输入要发送的数据:")

    # 2. 输入对方的ip地址
    dest_ip = input("\n请输入对方的ip地址:")

    # 3. 输入对方的端口号
    try:
        dest_port = int(input("\n请输入对方的端口号:"))
    except Exception as e:
        print(e)

    # 4. 发送数据
    udp_socket.sendto(msg.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接收数据并显示"""
    # 1. 接收数据
    msg = udp_socket.recvfrom(1024)

    # 2. 解码
    recv_ip = msg[1]
    msg = msg[0].decode("gbk")

    # 3. 显示接收到的数据
    print(">>>%s:%s" % (recv_ip, msg))


def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定本地信息
    udp_socket.bind(("", 7890))
    while True:
        # 3. 选择功能
        print("=" * 30)
        print("1. 发送消息")
        print("2. 接收消息")
        print("0. 退出")
        print("=" * 30)
        op_num = input("请输入要操作的功能序号:")

        # 4. 根据选择调用相应的函数
        if op_num == "1":
            send_msg(udp_socket)
        elif op_num == "2":
            recv_msg(udp_socket)
        elif op_num == "0":
            break
        else:
            print("输入有误，请重新输入...")


if __name__ == '__main__':
    main()
