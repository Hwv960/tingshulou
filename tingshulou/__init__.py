from bs4 import BeautifulSoup
import os
import sys
import datetime
import time
from tingshulou.utils import httptools

# 最大重试次数
retry_download_time = 5
# 当前重试次数
count_retry_download_time = 0


def download_file(f_url, f_path):

    r = httptools.get_file(f_url)

    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(title + file_name.__str__().zfill(4) + "   开始下载" + "时间 " + now_time)

    if os.path.exists(file_path):
        print("文件已经存在!")
    else:
        print("文件正在下载中!")
        with open(f_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
        time.sleep(10)

    if os.path.getsize(f_path) == 0:

        os.remove(f_path)

        global retry_download_time
        retry_download_time -= 1
        if retry_download_time != 0:
            global count_retry_download_time
            count_retry_download_time += 1
            print("文件下载失败，正在重试, 第 " + count_retry_download_time.__str__() + " 次！")
            download_file(f_url, f_path)

    retry_download_time = 5
    count_retry_download_time = 1

    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(title + file_name.__str__().zfill(4) + "   下载完毕" + "时间 " + now_time + "\n")


if __name__ == "__main__":

    index = input("请输入听书楼编码：")

    host = "http://www.tingshulou.com"

    url = host + "/book/" + index.__str__() + ".html"

    html = httptools.get(url)

    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('h1').get_text()

    start = input("将要下载的小说是：" + title + "?(Y/N)")

    if start != 'Y':
        print("下载结束！！！")
        sys.exit()

    all_a = soup.find_all('a')

    array = []

    for item in all_a:
        if item:
            if "down" in item.attrs.get('href', ""):
                array.append(item.attrs.get('href', ""))

    file_name = 0
    first = True

    for href in array:
        url = host + href
        html = httptools.get(url)
        soup = BeautifulSoup(html, 'html.parser')
        all_a = soup.find_all('a')

        if not os.path.exists(title):
            os.mkdir(title)

        for item in all_a:
            if item:
                file_type = ''
                if ".m4a" in item.attrs.get('href', ""):
                    file_type = "m4a"
                elif ".mp3" in item.attrs.get('href', ""):
                    file_type = "mp3"
                if file_type != '':
                    file_url = item.attrs.get('href', "")
                    if first:
                        file_name = file_name + 1
                        file_path = title + "/" + title + file_name.__str__().zfill(4) + "." + file_type
                        download_file(file_url, file_path)
                        first = False
                    else:
                        first = True

    end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(end_time + "  下载" + title + "完毕，感谢使用！")

