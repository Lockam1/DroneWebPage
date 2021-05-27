# import socket
# import struct

# def send( text, s):
#     msgbody = bytes(text.encode('utf-8'))
#     msglen = len(msgbody)
#     header = struct.pack('>H', msglen)
#     message = header + msgbody
#     s.sendall(message)

# def recieve(sock):
#     data = b''
#     while len(data) < 2:
#         data = sock.recv(1024)
#     body_length = struct.unpack('>H', data[:2])[0]
#     print(body_length)
#     data = data[2:]
#     while len(data) < body_length:
#         data += sock.recv(1024)
#     return data.decode('utf-8')

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('10.118.2.111', 65536))
# message = input('Message to send: ')
# send(message, s)
# print(recieve(s))
#---------------------------------------
# import socket
# import os

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('127.0.0.1', 12345)) #if the clients/server are on different network you shall bind to ('', port)

# s.listen(10)
# c, addr = s.accept()
# print('{} connected.'.format(addr))
# console.log('test')

# l = "test"
# c.send_all(l)

# print("Done sending...")
#------------------------------------------

import socket

HOST = ''  # Standard loopback interface address (localhost)
PORT = 80        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            conn.send_all('test')
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)