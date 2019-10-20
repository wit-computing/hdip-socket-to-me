import socket
import sys

HOST, PORT = "192.168.5.2", 50200
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server and send data
sock.connect((HOST, PORT))
sock.sendall(data + "\n")
print "Sent:     {}".format(data)
while True:
        # Receive data from the server and shut down
        received = sock.recv(1024)
        if received:
            print "Received: {}".format(received)
	else:
	    break
    