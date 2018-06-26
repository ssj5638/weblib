from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

PORT = 9999


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # req_url = self.path[:self.path.index('?')]
        # print(req_url)
        qindex = self.path.find('?')    # .find()찾으려는 값이 없으면 -1을 리턴

        # if qindex == -1:
        #     req_url =self.path[:len(self.path)]
        # else:
        #     req_url = self.path[:qindex]
        req_url = self.path[:len(self.path)] if qindex == -1 else self.path[:qindex]

        if req_url != '/graph':
            self.send_error(404, 'FileNot Found')
            return

        # print(req_url)
        ex = self.get_parameter('ex')
        print(ex)

    def get_parameter(self, name):
        qindex = self.path.find('?')

        # if qindex == -1:
        #     qs = 'NaN'
        # else:
        #     qs = self.path[qindex+1:]
        qs = '' if qindex == -1 else self.path[qindex+1:]
        # qs = self.path[self.path.find('?')+1:]
        # print(qs)



        params = parse_qs(qs)
        valuse = params.get(name)
        # print(params)

        return None if valuse is None else valuse.pop()

# 서버구동
httpd = HTTPServer(('', PORT), MyHTTPRequestHandler)
print('HTTP Server Starts Runs On Port(%d)'% (PORT))
httpd.serve_forever()