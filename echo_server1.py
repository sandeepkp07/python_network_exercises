import socket
host = socket.gethostname()
port = 3542
serv_sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.bind((host,port))
serv_sock.listen(1)
clnt, addr =serv_sock.accept()
print "Connected by: ", addr
while True:
data = clnt.recv(1024)
if not data:
break
clnt.sendall(data)
clnt.close()
