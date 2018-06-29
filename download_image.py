from http.client import HTTPConnection
from urllib.request import Request, urlopen, urlretrieve
from urllib.parse import urlencode


def download(url):
    name = 'random_graph'
    fullName = name + '.png'
    urlretrieve(url, fullName)


if __name__ == '__main__':
    url = 'localhost:9999/graph'
    data = urlencode({'ex':2})
    data = data.encode('utf-8')

    request = Request(url, data)
    f = urlopen(request)
    print(f.read())