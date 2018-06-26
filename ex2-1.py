# urlparse 테스트

from urllib.parse import urlparse, urlsplit, urljoin, parse_qs

url = "http://www.python.org:80/python.html;philosophy?a=10&b=20#here" # #here태그

result = urlparse(url)
print(result)