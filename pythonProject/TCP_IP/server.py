import socket
host = socket.gethostname()                                           #主机地址
port = 12345                                                        #端口号
s = socket.socket()                                                 #创建TCP/IP套接字
s.bind((host,port))                                                 #绑定地址
s.listen(1)                                                         #最大连接数量
sock,addr=s.accept()                                                #变动接收TCP/IP连接
print("连接已建立")
info = sock.recv(1024).decode()                                     #最多接收1024个字节
while info!='byebye':
    if info:
        print("接收到的内容:"+info)
    send_data = input("要发送的内容:")
    sock.send(send_data.encode())                                    #发送TCP数据
    if send_data == 'byebye':
        break
    info = sock.recv(1024).decode()                                  #接收客户端数据
sock.close()                                                         #关闭客户端套接字
s.close()                                                            #关闭服务器套接字
