import socket as s
import random as r
from urllib import request as rq
from bs4 import BeautifulSoup as bs
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/55.0.2883.87 Sarafi/537.36'}
class ConnectionError(Exception):
    pass
class OtherExceptions(Exception):
    pass
def catch_IP(url, port=80):
    data = s.create_connection((url, port))
    return data
def catch_data(url):
    page=rq.Request(url, headers=headers)
    page_info=rq.urlopen(page).read().decode('utf-8')
    soup=bs(page_info, 'html.parser')
    titles=soup.find_all('a', 'title')
    for title in titles:
        print(title.string)
        print(url+title.get('href'))
def check_connection():
    try:
        data = s.create_connection(("baidu.com", 80))
    except:
        raise ConnectionError("No internet connection or maybe your default connection checker site's server was down.")
    else:
        print(data)
        print("Good job! Perfect internet connection!")
def read_hosts():
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts", "r") as f:
        return f.read()
urls = ['baidu.com', 'bing.com', 'microsoft.com', 'apple.com', 'google.cn', 'unc0ver.dev', 'helloworldbook3.com', 'sogou.com', 'sougou.com', 'apple.com', 'goggle.com', 'sogou.com', 'hao123.com', 'betaprofiles.com', 'minecraft.net']
while True:
    res = int(input("(1)Get webiste's Ip (2)Get website's data (3)Check connection (4)Read hosts file (5)Exit"))
    if res == 1:
        for x in range(5):
            try:
                exurl = r.randint(0, len(urls)-1)
                url = urls[exurl]
                print('Connecting %s......' % url)
                print('Data:')
                print(catch_IP(url))
            except:
                print('Error occured.')
    elif res == 2:
        try:
            url = input("Enter the website:")
            if ("https://" in url) or ("http://" in url):
                print('Connecting %s......' % url)
                print('Data:')
                print(catch_data(url))
            else:
                fixed1 = "http://" + url
                fixed2 = "https://" + url
                print('Connecting %s and %s......' % (fixed1, fixed2))
                print('Data:')
                catch_data(fixed1)
                catch_data(fixed2)
        except:
            print('Error occured.')
    elif res == 3:
        check_connection()
    elif res == 4:
        print(read_hosts())
    elif res == 5:
        break
