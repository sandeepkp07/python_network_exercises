import socket
host =socket.gethostname()
port = 17685
serv_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv_sock.bind((host,port))
serv_sock.listen(5)
while True:
clnt, addr = serv_sock.accept()
rec = (clnt.recv(1024)).strip()
print rec
print "Enter data to send:"
data = raw_input()
clnt.send(data)
clnt.close()
