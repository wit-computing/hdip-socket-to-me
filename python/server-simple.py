import SocketServer
import random
import time

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        file = open("lots-of-data.txt","r")
        print "{} wrote:".format(self.client_address[0])
        print self.data
	# i=random.randint(100,200)
        i=200
        if  self.data:
            timeToSleep = float(self.data)
            for j in range(1,i):
               line = file.readline()
               self.request.sendall(line)
               print "{} sent:".format(line)
               time.sleep(timeToSleep)
        else:
            self.request.sendall(file.read())
            print "{} wrote:".format(self.client_address[0])



if __name__ == "__main__":
    HOST, PORT = "", 50200

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    print("Server up and running...")
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

