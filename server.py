import socketserver


class TsecServer (socketserver.TCPServer):
    class MyTsecHandler(socketserver.BaseRequestHandler):
        def handle(self):
            print("Tsec Handler")
            #if(status=FINISHED):
            
            if(True):
                server.appHandler(self.request)
                

    
    def __init__(self, endpoint, handler):
        super().__init__(endpoint, self.MyTsecHandler)
        self.appHandler = handler
        
        
        
def appHandler(request):
        print("appHandler")
        # self.request is the TCP socket connected to the client
        data = request.recv(1024).strip()
        print (data)
        # just send back the same data, but upper-cased
        request.sendall(data.upper())

server= TsecServer(("", 9999), appHandler)
server.serve_forever()
