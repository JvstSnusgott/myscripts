import http.server
import socketserver
import logging

logging.basicConfig(filename='ip_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
       
        if self.headers.get("Host") == "your-link.com":
            # Log the IP address of the client
            client_ip = self.client_address[0]
            logging.info(f"IP address {client_ip} accessed the special domain")

          
            self.send_response(302)
            self.send_header("Location")
            self.end_headers()
            return

      
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


PORT = 8000
Handler = RequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server started at port {PORT}")
    
    httpd.serve_forever()
