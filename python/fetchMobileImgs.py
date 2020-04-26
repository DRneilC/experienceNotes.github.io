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

fetchUrl = 'https://www.3gbizhi.com/wall'
urlList = ['MV', 'MX', 'YS', 'DM', 'KT', 'QC', 'AQ', 'YX', 'CM', 'QFJ', 'KA', 'JZ', 'ZW', 'DW', 'CY', 'QT']

def totalUrl ():
    if not os.path.exists('mobileImgs'):
        os.makedirs('mobileImgs')

    for i in range(len(urlList)):
        getTotalNum(fetchUrl + urlList[i] + '/')

def getTotalNum (url):
    req = urllib.request.Request(url, headers=header);
    html = urllib.request.urlopen(req);
    htmldata = html.read();
    htmlPath = etree.HTML(htmldata);

    # print(url);

    pages = htmlPath.xpath('//div[@id="pageNum"]/span/a/@href');

    match = re.compile(r'\d+')
    result = match.findall(pages[len(pages) - 2])
    totalNum = int(result[0])
    print(totalNum)

    for i in range(totalNum):
        if (i == 0):
            tourl = url
        else:
            tourl = url + 'index_' + str(i + 1) + '.html'

        getRankNum(tourl)

def getRankNum (url):
    req = urllib.request.Request(url, headers=header);
    html = urllib.request.urlopen(req);
    htmldata = html.read();
    htmlPath = etree.HTML(htmldata);

    print(url);

    pages = htmlPath.xpath('//div[@class="contlistw mtw"]/ul[@class="cl"]/li/a/@href');
    # print(pages)

    for i in range(len(pages)):
        time.sleep(0.1)

        try:
            getImg(pages[i])
        except Exception:
            pass;

def getImg(url):
    req = urllib.request.Request(url, headers=header);
    html = urllib.request.urlopen(req);
    htmldata = html.read();
    htmlPath = etree.HTML(htmldata);

    # print(url)

    pages = htmlPath.xpath('//div[@id="showimg"]/a/img/@src');
    names = htmlPath.xpath('//div[@id="showimg"]/a/img/@alt');

    # print(pages)
    print('real img')

    for i in range(len(pages)):
        matchObj = re.search(r'日历|月历', names[0])
        if matchObj:
            print('有日历或月历,不下载')
        else: 
            try:
                res = urllib.request.urlretrieve(pages[i], 'mobileImgs/%s.jpg' % names[0])
                print('下载%s' % names[0])
            except Exception:
                pass;

if __name__ == '__main__':
    totalUrl();

    print('finish');
    system('shutdown -s');