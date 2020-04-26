#!/usr/bin/python
#coding=utf-8ƒ

import re
import json
import time
import urllib.request
import urllib.parse
import os
import ssl
from os import system

ssl._create_default_https_context = ssl._create_unverified_context

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36", "Connection": "keep-alive", "Cookie": "ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; HMACCOUNT=AEDCEB3CBEC95051; HMVT=aedee6983d4cfc62f509129360d6bb3d|1568767741|; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1568022565,1568690148,1568704021,1568710787; _WCMID=1644a3e15d817efd687ff214; fp3_id1=1100B651EACAB091F83AE68D760A46FFD7176998D7193C6CC7F7E014F179DCAFE31B203EF1A85AF12D96D1A871ADC78AA4D6; kg_mid=14846bbadba56e02344cf800eedb6bfe;"}

def search(song_name):
    """搜索歌曲"""
    search_url = "https://songsearch.kugou.com/song_search_v2?callback=jQuery112407471259277043021_{}&keyword={}&page=1&pagesize=300&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_={}".format(str(int(time.time()*1000)), urllib.parse.quote(song_name), str(int(time.time()*1000)))
    print(search_url)
    req = urllib.request.Request(search_url, headers=header)
    html = urllib.request.urlopen(req)
    res = html.read().decode()
    start = re.search("jQuery\\d+_\\d+\\(?", res)

    data = json.loads(res.strip().lstrip(start.group()).rstrip(")"))
    # print(data)
    return data['data']['lists']

def download(song_list, dir):
    """下载歌曲"""
    # print(len(song_list))
    if len(song_list) > 20:
        song_len = 20
    else:
        song_len = len(song_list)

    for num in range(song_len):
        print(str(num) + " >>> " + str(song_list[num]['FileName']).replace('<em>', '').replace('</em>', ''))
    i = int(input("\n请输入您想要下载的歌曲序号："))

    # for i in range(len(song_list)):
    print("请稍等，下载歌曲中...")
    time.sleep(2)
    file_hash = song_list[i]['FileHash']
    album_id = song_list[i]['AlbumID']
    url = "https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery19108347826284861242_{}&hash={}&album_id={}&dfid=&mid=14846bbadba56e02344cf800eedb6bfe&platid=4&_={}".format(str(int(time.time()*1000)), file_hash, album_id, str(int(time.time()*1000)))
    print(url)
    obj = urllib.request.Request(url, headers=header)
    html = urllib.request.urlopen(obj)
    res = html.read().decode()  # json格式

    start = re.search("jQuery\d+_\d+\(?", res)
    data = json.loads(res.strip().lstrip(start.group()).rstrip(");"))
    # print(data)
    download_url = data['data']['play_url']

    file_path = ''
    try:
        if download_url:
            file_name = str(song_list[i]['FileName']).replace('<em>', '').replace('</em>', '')
            file_path = os.path.join(dir, ' - '.join(file_name.split(' - ')[::-1]) + ".mp3")
            with open(file_path, "wb") as fp:
                fp.write(urllib.request.urlopen(download_url).read())
            print("歌曲%s已下载完成！" % (file_name))
        else:
            print("无此歌曲链接")
            pass;
    except Exception as e:
        if os.path.exists(file_path):
            os.remove(file_path)
        print(e)

if __name__ == '__main__':
    # 下载歌曲存放目录
    if not os.path.exists('music'):
        os.makedirs('music')

    dir = "music"

    try:
        # 搜索歌曲
        song_list = search(input("请输入您想要搜索的歌曲名称："))
        # 下载歌曲
        download(song_list, dir)
    except Exception as e:
        print(e)
        pass

    print('finish')
    system('shutdown -s')
    