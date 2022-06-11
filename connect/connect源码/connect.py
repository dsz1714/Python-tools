# 本软件仅供学习使用, 切勿随意使用或对外发布源码!
# Connect v1.0
# 一套小工具
from urllib import request as rq
from bs4 import BeautifulSoup as bs
import random
import socket as s
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/55.0.2883.87 Sarafi/537.36'}
def nr(url):
    urlx=url
    page=rq.Request(urlx, headers=headers)
    page_info=rq.urlopen(page).read().decode('utf-8')
    soup=bs(page_info, 'html.parser')
    titles=soup.find_all('a', 'title')
    for title in titles:
        print(title.string+'\n')
        print(urlx+title.get('href')+'\n \n')
def get(url, port):
    server = s.create_connection((url, port))
    return server
urls = ['baidu.com', 'bing.com', 'microsoft.com', 'apple.com', 'google.cn', 'unc0ver.dev', 'helloworldbook3.com', 'sogou.com', 'sougou.com', 'apple.com', 'goggle.com']
while True:
    res = int(input("(1)随机抓包 (2)检查网络状态 (3)查看hosts (4)查询网站内容 (5)关闭\n"))
    if res == 1:
        for x in range(10):
            try:
                exurl = random.randint(0, len(urls)-1)
                url = urls[exurl]
                print('正在连接 %s......' % url)
                print('获取到的信息:')
                print(get(url, 80))
            except:
                print('啊，触发了一个小错误！')
    elif res == 2:
        try:
            connect = s.create_connection(('baidu.com', 80))
        except:
            print('您的网络出了什么问题？连百度都连接不上？')
        else:
            print('恭喜，网络正常！')
    elif res == 3:
        with open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'r', encoding = 'utf-8') as f:
            print(f.read())
    elif res == 4:
        try:
            url = input("输入网址:")
            print('正在连接 %s......' % url)
            print('获取到的信息:')
            print(nr(url))
        except:
            print('啊，触发了一个小错误！')
    elif res == 5:
        break
