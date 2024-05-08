from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

'''
TCP服务端的代码
'''
# def main():
#     '''创建套接字对象并指定使用哪种传输服务
#     family=AF_INET - IPv4地址
#     family=AF_INET6 - IPv6地址
#     type=SOCK_STREAM - TCP套接字
#     type=SOCK_DGRAM - UDP套接字
#     type=SOCK_RAW - 原始套接字'''
#     server = socket(family=AF_INET, type=SOCK_STREAM)
#     # 绑定IP地址和端口，用去区分不同的服务
#     # 同一时间一个端口只可以绑定一个服务，否则会报错port already used
#     server.bind(('172.31.29.35', 6789))
#     # 监听客户端连接到服务器，参数512可以理解为连接队列的大小
#     server.listen(512)
#     print('服务器启动开始监听...')
#     while True:
#         '''
#         循环接收客户端的连接并进行相应的处理
#         accept 方法是一个阻塞方法，如果没有客户端连接到服务器 代码不会向下执行
#         accept方法返回一个元组其中第一个元素是客户端对象，第二个元素是连接到服务器的客户端的地址，IP和PORT组成
#         '''
#         client, addr = server.accept()
#         print(str(addr) + '连接了服务器.')
#         client.send(str(datetime.now()).encode('utf-8'))
#         client.close()

'''
TCP客户端的代码
'''
def client():
    client = socket()
    client.connect(('172.32.29.35', 6789))
    print(client.recv(1024).decode('utf-8'))
    client.close()
'''
多线程技术处理多个用户请求的服务器代码
'''

from socket import socket,SOCK_STREAM,AF_INET
from base64 import b64decode
from json import dumps
from threading import Thread

def main():

    # 自定义线程类
    class FileTransferHandler(Thread):
        def __init__(self,cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'majiang01.jpg'
            my_dict['filedata'] = data
            json_str = dumps(my_dict)
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    server = socket()
    server.bind(('172.31.29.35',6789))
    server.listen(512)
    print('server start listening...')
    with open('majiang.jpg', 'rb') as f:
        data = b64decode(f.read()).decode('utf-8',errors='ignore')
    while True:
        client, addr = server.accept()
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()
