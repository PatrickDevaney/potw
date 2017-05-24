import socket

connection = socket.socket()
connection.connect(("potw.quinnftw.com", 80))
connection.send(b'GET /problem/s3cret HTTP/1.1\r\n')
connection.send(b'Host: potw.quinnftw.com\r\n\r\n')
recieved = connection.recv(2048).decode("utf-8")
print(recieved)
