#!/usr/bin/python
#coding=utf-8

import pygame
from pygame.locals import *
import random

'''
    1. 搭建界面，主要完成窗口和背景图的显示
'''

class HeroPlane (object):
    def __init__ (self, screen):
        # 默认飞机位置
        self.x = 164
        self.y = 530

        # 设置显示内容的窗口
        self.screen = screen

        self.image = pygame.image.load("./feijidazhan/feiji.png").convert_alpha()

    def display (self, screen):
        self.screen.blit(self.image, (self.x, self.y))

    def turnLeft (self):
        if self.x > 10:
            self.x -= 10

    def turnRight (self):
        if self.x < 160:
            self.x += 10

    def turnUp (self):
        if self.y > 10:
            self.y -= 10

    def turnDown (self):
        if self.y < 510:
            self.y += 10

def keyCtr (heroPlane):
    #获取事件，比如按键等
    for event in pygame.event.get():
        # 判断是否点击关闭按钮
        if event.type == QUIT:
            print('exit')
            exit()
        # 判断方向键
        elif event.type == KEYDOWN:
            # 判断左键
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                heroPlane.turnLeft()

            # 判断右键
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                heroPlane.turnRight()

            elif event.key == K_UP:
                print('up')
                heroPlane.turnUp()

            elif event.key == K_DOWN:
                print('down')
                heroPlane.turnDown()

            # 判断空格键
            elif event.key == K_SPACE:
                print('空格键')

def play ():    
    # pygame.mixer.Sound，主要加载ogg和wav音频文件。
    # pygame.mixer.music，主要加载mp3音频文件。

    #检查音乐流播放，有返回True，没有返回False
    #如果没有音乐流则选择播放
    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.play()
        pygame.mixer.music.play()


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("./music/feijidazhan.mp3")

    #1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((378, 638), 0, 32)

    #2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feijidazhan/bg.jpeg").convert()

    # 创建角色
    hero = HeroPlane(screen)

    #3. 把背景图片放到窗口中显示
    while True:
        # 播放音乐
        play()
        keyCtr(hero)            

        #设定需要显示的背景图
        screen.blit(background,(0,0))

        
        hero.display(screen)

        temp = random.randrange(0, 4)  # 0-3
        if temp == 0:
            hero.turnLeft()
        elif temp == 1:
            hero.turnRight()
        elif temp == 2:
            hero.turnUp()
        elif temp == 3:
            hero.turnDown()

        
        #更新需要显示的内容
        pygame.display.update()


if __name__ == "__main__":
    main()
