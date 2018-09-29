import requests
import string
from urllib.parse import quote
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'}

ip, port = ("139.198.10.210", "10800")
proxy_url = "http://{0}:{1}".format(ip, port)

proxy_dict = {
    "http": proxy_url
}


def get(url):
    res = requests.request(method='get', url=url, headers=headers, proxies=proxy_dict)
    html = res.content.decode(res.apparent_encoding, "ignore")
    res.close()
    return html


def get_file(url, path):
    url = quote(url, safe=string.printable)
    r = requests.get(url, stream=True, headers=headers, proxies=proxy_dict)

    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)
    r.close()
    if os.path.getsize(path) == 0:
        return False
    else:
        return True
