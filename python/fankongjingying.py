#!/usr/bin/python
#coding=utf-8

# 反恐精英
# 1. 人类
    # 属性
        # 姓名
        # 血量
        # 持有的枪
    # 方法
        # 安子弹
        # 安弹夹
        # 拿枪（持有抢）
        # 开枪

class Person (object):
    def __init__(self, new_name):
        self.name = new_name
        self.gun = None
        self.ph = 100

    # 按子弹
    def zhuangzidan (self, danjia_temp, zidan_temp):
        danjia_temp.baocun(zidan_temp)

    # 按弹夹
    def andanjia (self, gun_temp, danjia_temp):
        gun_temp.baocun(danjia_temp)

    # 拿枪
    def naqiang (self, gun_temp):
        self.gun = gun_temp

    # 开枪
    def kaiqiang (self, diren):
        self.gun.shoot(diren)

    # 掉血
    def diaoxue (self, shangshali):
        self.ph -= shangshali
        print("%s还剩%d滴血" % (self.name, self.ph))

    def __repr__ (self):
        if self.gun:
            return "%s 的ph为:%d, 他一把%s：" % (self.name, self.ph, self.gun.name)
        else:
            return "%s 的ph为:%d, 他么有枪..." % (self.name, self.ph)


# 2. 子弹类
    # 属性
        # 杀伤力
    # 方法
        # 伤害敌人(让敌人掉血)
class Bullet (object):
    def __init__ (self, max_num):
        self.shangshali = max_num

    def shashang (self, diren):
        diren.diaoxue(self.shangshali)

# 3. 弹夹类
    # 属性
        # 容量（子弹存储的最大值）
        # 当前保存的子弹
    # 方法
        # 保存子弹（安装子弹的时候）
        # 弹出子弹（开枪的时候）
class Danjia (object):
    def __init__ (self, max_num):
        self.rongliang = 20
        self.zidan = []

    def baocun (self, zidan_temp):
        self.zidan.append(zidan_temp)

    def dachuzidan (self):
        if len(self.zidan) > 0:
            print("打出一颗子弹；弹夹里还剩下%d颗子弹" % (len(self.zidan) - 1))
            return self.zidan.pop()
        else:
            return None

# 4. 枪类
    # 属性
        # 弹夹（默认没有弹夹，需要安装）
    # 方法
        # 连接弹夹（保存弹夹）
        # 射子弹
class Gun (object):
    def __init__ (self, new_name):
        self.name = new_name
        self.danjia = None

    def baocun (self, danjia_temp):
        self.danjia = danjia_temp

    def shoot (self, diren):
        zidan = self.danjia.dachuzidan()

        if zidan:
            zidan.shashang(diren)

laowang = Person('老王')
enemy = Person('敌人')
ak47 = Gun('ak47')
danjia = Danjia(20)

for i in range(10):
    bullet = Bullet(10)
    laowang.zhuangzidan(danjia, bullet)

laowang.andanjia(ak47, danjia)
laowang.naqiang(ak47)
laowang.kaiqiang(enemy)

# a = [x for x in range(1,101)]

# b = [a[x:x+3] for x in range(0,len(a),3)]
# for x in range(0,len(a),3):
#     print(x)
#     print(a[x:x+3])
# print(b)