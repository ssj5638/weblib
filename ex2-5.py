# http.client.HTTPConnection 사용한 HEAD방식 요청

from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')
conn.request('HEAD', '/')

result = conn.getresponse()
print(result.status, result.reason)

data = result.read()
print(len(data))