import time
import socket
serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1356
serv_sock.bind((host,port))
serv_sock.listen(1) #que upto 10 requests
while True:
clnt_sock, addr = serv_sock.accept()
print 'connected from', addr
time = time.ctime(time.time()) + "\r\n"
clnt_sock.send(time.encode('ascii'))
clnt_sock.close()
