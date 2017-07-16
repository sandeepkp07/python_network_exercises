import socket
host = socket.gethostname()
port = 17685
clnt_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clnt_sock.connect((host,port))
data = raw_input()
while data == 'quit':
clnt_sock.send(data)
resp = (clnt_sock.recv(4096)).strip()
print resp
print 'press "quit" if u want to exit'
clnt_sock.close()

