import requests
import string


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}


def get(url):
    res = requests.request(method='get', url=url, headers=headers)
    html = res.content.decode(res.apparent_encoding, "ignore")
    return html


def get_file(url):
    from urllib.parse import quote
    url = quote(url, safe=string.printable)
    r = requests.get(url, stream=True, headers=headers)
    return r
