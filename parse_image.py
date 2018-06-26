from urllib.request import urlopen
from html.parser import HTMLParser


class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return

        if not hasattr(self, 'result'):
            self.result = []

        for name, value in attrs:
            if name == 'src':
                self.result.append(value)


def main():
    url = 'http://www.google.co.kr'
    response = urlopen(url)

    charset = response.headers.get_content_charset()
    data = response.read().decode(charset)
    response.close()

    print('\n>>>> Fetch Image From ', url)


# def parseImage(data):
    parser = ImageParser()
    parser.feed(data)

    dataset = set(x for x in parser.result)
    print('\n'.join(sorted(dataset)))


if __name__ == '__main__':
    main()