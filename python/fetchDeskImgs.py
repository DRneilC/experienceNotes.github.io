#!/usr/bin/python
#coding=utf-8

import urllib.request;
import os;
from os import system;
from lxml import etree;
import ssl;
import re;
import time;

ssl._create_default_https_context = ssl._create_unverified_context

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36", "Connection": "keep-alive"}

fetchUrl = 'http://www.netbian.com'

def getTotalNum ():
    if not os.path.exists('deskimgs'):
        os.makedirs('deskimgs')

    for i in range(906, 946):
        if (i == 0):
            url = fetchUrl + '/1920x1080/index.htm'
        else:
            url = fetchUrl + '/1920x1080/index_' + str(i + 1) + '.htm'

        getRankNum(url)

def getRankNum (url):
    req = urllib.request.Request(url, headers=header);
    html = urllib.request.urlopen(req);
    htmldata = html.read();
    htmlPath = etree.HTML(htmldata);

    print(url);

    pages = htmlPath.xpath('//div[@id="main"]/div[@class="list"]/ul/li/a/@href');

    for i in range(len(pages)):
        time.sleep(0.1)

        try:
            getImgsItem(fetchUrl + pages[i])
        except Exception:
            pass;

def getImgsItem(url):
    req = urllib.request.Request(url, headers=header);
    html = urllib.request.urlopen(req);
    htmldata = html.read();
    htmlPath = etree.HTML(htmldata);
    # print(url)
    print('big pic href')
    pages = htmlPath.xpath('//div[@class="pic"]/p/a/@href');

    for i in range(len(pages)):
        try:
            getImgs(fetchUrl + pages[i])
        except Exception:
            pass;

def getImgs(url):
    req = urllib.request.Request(url, headers=header);
    html = urllib.request.urlopen(req);
    htmldata = html.read();
    htmlPath = etree.HTML(htmldata);

    pages = htmlPath.xpath('//div[@id="main"]/table/tr/td/a/img/@src');
    names = htmlPath.xpath('//div[@id="main"]/table/tr/td/a/img/@alt');

    # print(pages)
    print('real img')

    for i in range(len(pages)):
        matchObj = re.search(r'日历|月历', names[0])
        if matchObj:
            print('有日历或月历,不下载')
        else: 
            try:
                res = urllib.request.urlretrieve(pages[i], 'deskimgs/%s.jpg' % names[0])
                print('下载%s' % names[0])
            except Exception:
                pass;

if __name__ == '__main__':
    getTotalNum();

    print('finish');
    system('shutdown -s');