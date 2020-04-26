#!/usr/bin/python
#coding=utf-8

import urllib.request;
import os;
from os import system;
from lxml import etree;
import ssl;
import re;
import json;
import time;

ssl._create_default_https_context = ssl._create_unverified_context
cookie = "__cfduid=d5c34a3ec5bdc7cc6687d72d71a40a7e11566261067; Hm_lvt_14b14198b6e26157b7eba06b390ab763=1567135414,1568171264,1568612233,1568791456; zkhanecookieclassrecord=%2C66%2C; PHPSESSID=fca56d373381a81c3e6433169844789d; zkhanmlusername=qq081339156818; zkhanmluserid=2000742; zkhanmlgroupid=1; zkhanmlrnd=9qTma7cLuF4SXtjoKSFs; zkhanmlauth=987332badb5ab2c17f25898507034a9c; Hm_lpvt_14b14198b6e26157b7eba06b390ab763=1568799227; Hm_lvt_526caf4e20c21f06a4e9209712d6a20e=1568791501,1568791555,1568791685,1568799246; zkhandownid24805=1; Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e=1568799405; security_session_verify=40996c6367bb47a73b2dcf51327fdffa"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36", "Connection": "keep-alive", "Cookie": cookie}

fetchUrl = 'http://pic.netbian.com'

def getTotalNum ():
    if not os.path.exists('4kimgs'):
        os.mkdir('4kimgs')

    for i in range(19):
        url = fetchUrl + '/e/search/result/index.php?page=' + str(i) + '&searchid=2453'
            
        getRankNum(url)

def getRankNum (url):
    req = urllib.request.Request(url, headers=header);
    html = urllib.request.urlopen(req);
    htmldata = html.read();
    htmlPath = etree.HTML(htmldata);

    # print(url);

    pages = htmlPath.xpath('//div[@id="main"]/div[@class="slist"]/ul/li/a/@href');
    print(pages);

    for i in range(len(pages)):
        sleep(1)
        getImgsItem(fetchUrl + pages[i])


def getImgsItem(url):
    urlIdMatch = re.search("\d+", url)
    urlId = urlIdMatch.group()
    # print(urlId)

    download_url = "http://pic.netbian.com/e/extend/downpic.php?id={}&t=0.3456148298180828".format(urlId)

    req = urllib.request.Request(download_url, headers=header);
    html = urllib.request.urlopen(req);
    htmldata = html.read().decode();
    data = json.loads(htmldata)
    print(data)

    img_url = fetchUrl + data['pic']

    # print(img_url)
    file_path = os.path.join("4kimgs", urlId + '.jpg')
    try:
        if data['pic']:
            with open(file_path, "wb") as fp:
                reqimg = urllib.request.Request(img_url, headers=header);
                fp.write(urllib.request.urlopen(reqimg).read())
            print("图片%s已下载完成！" % (img_url))
        else:
            print("无此链接")
            pass;
    except Exception as e:
        if os.path.exists(file_path):
            os.remove(file_path)
        print(e)

if __name__ == '__main__':
    getTotalNum();

    print('finish');
    system('shutdown -s');