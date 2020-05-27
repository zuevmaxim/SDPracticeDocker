from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            with open("files" + self.path, mode='rb') as file:
                fileContent = file.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(fileContent)
                return
        except:
            self.send_response(404)
            self.end_headers()
        

def run(port, server_class=HTTPServer, handler_class=Server):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    from sys import argv
    run(port=int(argv[1]))
