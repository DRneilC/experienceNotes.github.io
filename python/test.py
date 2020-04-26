#!/usr/bin/python
#coding=utf-8

# raw_input("按下 enter 键退出，其他任意键显示...\n");

import sys, getopt;
# print '参数个数', len(sys.argv), '参数列表', str(sys.argv);

# def main(argv):
#     inputfile = ''
#     outputfile = ''
#     try:
#         opts, args = getopt.getopt(argv, ["ifile=","ofile="])
#     except getopt.GetoptError:
#         print 'test.py -i <inputfile> -o <outputfile> get error'
#         sys.exit(2)

#     print opts, args;

#     for opt, arg in opts:
#         if opt == '-h':
#             print 'test.py -i <inputfile> -o <outputfile> get h'
#             sys.exit()
#         elif opt in ("-i", "--ifile"):
#             inputfile = arg
#         elif opt in ("-o", "--ofile"):
#             outputfile = arg

#     print '输入的文件为：', inputfile
#     print '输出的文件为：', outputfile

# if __name__ == "__main__":
#     main(sys.argv[1:])

'''
numbers = [1, 2, 3, 4, 4, 5, 8, 9, 11];
even = []
odd = []
while len(numbers) > 0:
    num = numbers.pop()
    if num % 2 == 0 :
        even.append(num)
    else:
        odd.append(num)

print even, odd
'''


'''
i = 1
while i < 10:
    i += 1;
    if i % 2 == 1:
        continue;
    print i;
else:
    print i;
'''

'''
for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num): # 根据因子迭代
        if num % i == 0:      # 确定第一个因子
            j = num / i          # 计算第二个因子
            # print '%d 等于 %d * %d' % (num,i,j)
            print(num, '等于', i, '*', j);
            break;          # 跳出当前循环
    else:
        print(num, '是一个质数');
'''

import math, random;
# print(math.modf(10.45))
# print(math.radians(60));
# print(math.degrees(math.pi / 6));
# print(math.sin(math.pi / 6));

# print(random.random())
# print(random.uniform(187, 34))


# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a+b

import time, calendar;
# print (time.time())

# from tem import pack
# pack.testFun('你是是饿')

# import importPac
# importPac.func('嘿嘿巴蒂')

# print range(2,10,2);
# print [x*5 for x in range(2,10,2)];

# fo = open('text.rtf', 'r')
# print "文件名: ", fo.name
# print "是否已关闭 : ", fo.closed
# print "访问模式 : ", fo.mode
# print "末尾是否强制加空格 : ", fo.softspace

# 打开一个文件
fo = open("foo.txt", "w")
# fo.write( "www.runoob.com!\nVery good site!\n")
 

# fo = open("foo.txt")
# str = fo.read(4)
# print str

# # 查找当前位置
# position = fo.tell()
# print "当前文件位置 : ", position
 
# # 把指针再次重新定位到文件开头
# position = fo.seek(4, 1)
# str = fo.read(10)
# print "重新读取字符串 : ", str
# # 关闭打开的文件
# fo.close()

import os;

os.rename('foo.txt', 'foo1.txt')
os.remove('foo1.txt')


class people:
    name = "";
    age = "";
    __weight = 0;

    def __init__ (self, n, a, w):
        self.name = n;
        self.age = a;
        self.__weight = w;

    def speak (self):
        # print("%s 说：我今年 %d岁, 我%d斤，"%(self.name, self.age, self.__weight))
        pass;

class student (people):
    def __init__ (self, n, a, w, g):
        people.__init__(self, n, a, w);
        self.grade = g
    def speak (self):
        # print("%s 说：我今年 %d岁，我在读%d年级"%(self.name, self.age, self.grade))
        pass;

class speaker ():
    topic = "";
    name = "";

    def __init__ (self, n, t):
        self.topic = t;
        self.name = n;

    def speak (self):
        # print("我叫%s, 我今天演讲的题目是%s"%(self.name, self.topic))
        pass;

class sample (speaker, student): 
    a = '';
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g);
        speaker.__init__(self, n, t);

lilei = sample("lilei", 9, 45, 3, 'Python')
lilei.speak()

# print('按下回车开始计时，按下 Ctrl + C 停止计时。')
# while True:
#     try:
#         input() # 如果是 python 2.x 版本请使用 raw_input() 
#         starttime = time.time()
#         print('开始')
#         while True:
#             print('计时: ', round(time.time() - starttime, 0), '秒')
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print('结束')
#         endtime = time.time()
#         print('总共的时间为:', round(endtime - starttime, 2),'secs')
#         break;


# 链接数据库
# import mysql.connector
 
# mydb = mysql.connector.connect(
#     host="47.96.177.168",       # 数据库主机地址
#     user="root",    # 数据库用户名
#     passwd="123456",   # 数据库密码
#     database="testData" # 表名
# )

# mycursor = mydb.cursor()
 
# mycursor.execute("SHOW DATABASES")
 
# for x in mycursor:
#     print(x)

# sql = "INSERT INTO users_list (name, age, weight) VALUES (%s, %s, %s)"
# sql = "SELECT * FROM users_list where name='张文远'"

# mycursor.executemany(sql, val)

# mydb.commit()    # 数据表内容有更新，必须使用到该语句

# myresult = mycursor.fetchall()
# print(myresult)


def printFozu ():
    print("                            _ooOoo_  ")
    print("                           o8888888o  ")
    print("                           88  .  88  ")
    print("                           (| -_- |)  ")
    print("                            O\\ = /O  ")
    print("                        ____/`---'\\____  ")
    print("                      .   ' \\| |// `.  ")
    print("                       / \\||| : |||// \\  ")
    print("                     / _||||| -:- |||||- \\  ")
    print("                       | | \\\\\\ - /// | |  ")
    print("                     | \\_| ''\\---/'' | |  ")
    print("                      \\ .-\\__ `-` ___/-. /  ")
    print("                   ___`. .' /--.--\\ `. . __  ")
    print("                ."" '< `.___\\_<|>_/___.' >'"".  ")
    print("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |  ")
    print("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /  ")
    print("         ======`-.____`-.___\\_____/___.-`____.-'======  ")
    print("                            `=---='  ")
    print("  ")
    print("         .............................................  ")
    print("                  佛祖镇楼                  BUG辟易  ")
    print("          佛曰:  ")
    print("                  写字楼里写字间，写字间里程序员；  ")
    print("                  程序人员写程序，又拿程序换酒钱。  ")
    print("                  酒醒只在网上坐，酒醉还来网下眠；  ")
    print("                  酒醉酒醒日复日，网上网下年复年。  ")
    print("                  但愿老死电脑间，不愿鞠躬老板前；  ")
    print("                  奔驰宝马贵者趣，公交自行程序员。  ")
    print("                  别人笑我忒疯癫，我笑自己命太贱；  ")
    print("                  不见满街漂亮妹，哪个归得程序员？")

# printFozu()

# def test(a, b):
#     shang = a // b;
#     yushu = a % b;
#     return shang, yushu

# shang, yushu = test(5, 2)
# print(test(5, 2))

# test(1, 2)

def mathformula():
    for i in range(1, 10):
        for k in range(1, 10):
            if i <= k:
                print("%d%d得%d"%(i, k, i*k))

# mathformula()

def runnian ():
    year = int(input('请输入年份'))
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        print("%s年是闰年"%year)
    else:
        print("%s年不是闰年"%year)

# runnian()

import time;
# print(time.strptime('2019-10-01', "%Y-%m-%d"))

import socket
from socket import *

# Address Family：可以选择 AF_INET（用于 Internet 进程间通信） 或者 AF_UNIX（用于同一台机器进程间通信）,实际工作中常用AF_INET
# Type：套接字类型，可以是 SOCK_STREAM（流式套接字，主要用于 TCP 协议）或者 SOCK_DGRAM（数据报套接字，主要用于 UDP 协议）

# 创建tcp的套接字
# udp_socket = socket(AF_INET, SOCK_DGRAM)
# dest_addr = ('192.168.11.101', 8080)
# send_data = input("请输入要发送的数据:")
# udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

# 5. 关闭套接字
# udp_socket.close()
