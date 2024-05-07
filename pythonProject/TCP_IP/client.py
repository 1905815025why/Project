import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host,port))                         #初始化TCP/IP服务器
print("已连接")
info = ''
while info != 'byebye':
    send_data = input("请输入要发送的内容：")
    s.send(send_data.encode())               #发送TCP数据
    if send_data == 'byebye':
        break
    info =s.recv(1024).decode()                #接收服务器数据
    print('接收到的内容：'+info)
s.close()                                      #关闭套接字
