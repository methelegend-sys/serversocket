import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print ('Starting Up On %s Port %s' % server_address)
sock.bind(server_address)

sock.listen(1)

print ('Waiting For A Connection')
connection, client_address = sock.accept()
print('Connection From', client_address)
name=input('Username:')
connection.sendall(name.encode())
name = connection.recv(20)
name=name.decode()

while True:
    data = connection.recv(20)
    data=data.decode()

    if data=='0':
        print('Connection Closed By Client')
        connection.close()
        break

    print(name,': "%s"' % data)
    message=input('Message(Input 0 To Abort):')
    connection.sendall(message.encode())

    if message=='0':
        print("Closing Connection")
        connection.close()
        break
