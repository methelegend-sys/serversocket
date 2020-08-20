import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print ('connecting to %s port %s' % server_address)
sock.connect(server_address)
name=input('Username:')
sock.sendall(name.encode())
name = sock.recv(20)
name=name.decode()
while(True):
    message = input("Message(Input 0 To Abort):")
    sock.sendall(message.encode())
    if message=='0':        
        print("Closing Connection")
        sock.close()
        break

    data = sock.recv(20)
    data=data.decode()
    if data=='0':
        print('Connection Closed By Server')
        sock.close()
        break
    
    print (name,': "%s"' % data)

