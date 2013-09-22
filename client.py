import socket
import sys

class TsecClient:
    
    def __init__(self, endpoint):
        self.endpoint=Endpoint(endpoint)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect (self):
        self.sock.connect(self.endpoint)
        # Setup Secure channel
        self.setSecureChannel()
        
    def send (self, data):
        # Do all crypto stuff and send
        self.sock.sendall(bytes(data + "\n", "utf-8"))
    
    def receive (self):
            #decrypt and return
            return str(self.sock.recv(1024), "utf-8")
    
    def close(self):
        self.sock.close()
    
    def setSecureChannel(self):
        pass
class Endpoint:
    def __init__ (self, endpoint):
        self.endpoint= endpoint
        self.ID=""
    
client = TsecClient(("localhost", 9999))
data = " ".join(sys.argv[1:])
try:
    # Connect to server and send data
    client.connect()
    client.send(data)
    received = client.receive();
    # Receive data from the server and shut down
finally:
    client.close()

print("Sent:     {}".format(data))
print("Received: {}".format(received))
