#!/usr/bin/env python
# -*-coding:utf-8-*-
import  urllib.request
from lxml import etree
from os import system
import os
import random
import ssl
import mysql.connector

ssl._create_default_https_context = ssl._create_unverified_context

pciturelist = []

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36", "Connection": "keep-alive"}

mydb = mysql.connector.connect(
    host="47.96.177.168",       # 数据库主机地址
    user="root",    # 数据库用户名
    passwd="123456",   # 数据库密码
    database="testData" # 表名
)

mycursor = mydb.cursor()

# sql = "CREATE TABLE IF NOT EXISTS imgs (img_id INT UNSIGNED AUTO_INCREMENT, img_desc VARCHAR(100) NOT NULL, img_url VARCHAR(40) NOT NULL, PRIMARY KEY ( img_id ))ENGINE=InnoDB DEFAULT CHARSET=utf8;"

# mycursor.execute(sql)
# mydb.commit()

def mmRankSum():
    if not os.path.exists('pic'):
        os.makedirs('pic')

    req = urllib.request.Request("https://www.meitulu.com/t/youwu/", headers=header)
    html = urllib.request.urlopen(req)
    htmldata = html.read()
    htmlpath = etree.HTML(htmldata)

    #首先获取页码数,然后用循环的方式挨个解析每一个页面
    pages = htmlpath.xpath('//ul[@class="img"]/li/a/@href')
    # print(pages)

    for i in range( len(pages)):
        mmRankitem(pages[i])

"""
参数 url : 分页中每一页的具体url地址
通过穿过来的参数，使用  lxml和xpath 解析 html，获取每一个MM写真专辑页面的url
"""
def mmRankitem(url):
    req = urllib.request.Request(url, headers=header)
    html = urllib.request.urlopen(req)
    htmldata = html.read()
    htmlpath = etree.HTML(htmldata)
    pages = htmlpath.xpath('//div[@id="pages"]/a/@href')
    print(pages);

    for i in range(len(pages)):
       getAlbums("https://www.meitulu.com" + pages[i])


"""
参数 url : 每一个MM专辑的页面地址
通过穿过来的参数，获取每一个MM写真专辑图片集合的地址

"""
def getAlbums(girlUrl):
    req = urllib.request.Request(girlUrl, headers=header)
    html = urllib.request.urlopen(req)
    htmldata = html.read()
    htmlpath = etree.HTML(htmldata)

    # print(girlUrl)

    pages = htmlpath.xpath('//img[@class="content_img"]/@src')
    names = htmlpath.xpath('//img[@class="content_img"]/@alt')
    
    # print(pages);

    for i in range(len(pages)):
        res = urllib.request.urlretrieve(pages[i],'pic/%s.jpg' % names[i])

        sql = "INSERT INTO imgs (img_desc, img_url) VALUES (%s, %s)"
        val = (str(names[i]), str(pages[i]))

        mycursor.execute(sql, val)
        mydb.commit()

        if res:
            print('下载%s' % (names[i]))

mmRankSum()

print('finish')
system('shutdown -s')