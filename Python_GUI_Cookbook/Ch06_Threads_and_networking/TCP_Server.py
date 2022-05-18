from socketserver import BaseRequestHandler, TCPServer

class RequestHandler(BaseRequestHandler):
    #override base class handle method
    def handle(self):
        print('Server connected to:', self.client_address)
        while True:
            rsp = self.request.recv(512)
            if not rsp: break
            self.request.send(b'Server received: '+rsp)

def start_server():
    # print('Server started')
    server = TCPServer(('',24000),RequestHandler)
    server.serve_forever()