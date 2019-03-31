import requests
from lxml import etree

class SpiderHelper(object):
    def __init__(self, headers=None, timeout=5):
        self.headers = headers
        self.timeout = timeout
        self.html = None

    def get_url(self, url):
        try:
            self.html = requests.get(url, timeout=self.timeout)
        except:
            keep_request = requests.session()
            keep_request.keep_alive = False
            try:
                self.html = requests.get(url, timeout=self.timeout)
            except:
                self.html = None
        return self

    def html_encoding(self, encoding='utf-8'):
        if self.html:
            self.html.encoding = encoding
            return self
        else:
            return None

if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    spider = SpiderHelper()
    html = spider.get_url(url).html_encoding().html
    print(html.text)
