from http.server import BaseHTTPRequestHandler, HTTPServer

port = 9999


class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):       # 서버가 GET방식으로 받은 경우 실행
        # print('receive result')
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()

        self.wfile.write('<h1> Hello World</h1>'.encode('utf-8'))

# 서버구동
httpd = HTTPServer(('', port), MyHTTPRequestHandler)
print('HTTP Server Starts....')
httpd.serve_forever()