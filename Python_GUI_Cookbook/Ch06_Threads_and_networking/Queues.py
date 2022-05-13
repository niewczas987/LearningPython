#using TCP/IP
from socket import socket, AF_INET, SOCK_STREAM

def write_to_scrol(inst):
    print('Hi! from Queue ', inst)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost',24000))
    for idx in range(3):
        sock.send(b'Message from queue: ' + bytes(str(idx).encode()))
        recv = sock.recv(8192).decode()
        inst.gui_queue.put(recv)
    inst.create_thread(6)
