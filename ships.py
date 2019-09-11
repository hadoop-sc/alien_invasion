# -*- coding: utf-8 -*-
# 功能：定义飞船类
# 作者：邵春
# 时间：2019.09.11

import pygame

class Ships(object):

    '''初始化飞船，并设置其初始化位置'''

    def __init__(self, screen):
        self.screen = screen
        # 加载飞船位置并获取其外接矩形
        self.image = pygame.image.load("images/ships/primary_battleship.bmp")
        self.ship_rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #将每艘飞船放在屏幕中央底部
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom

    def blitme(self):

        '''在执行位置描绘飞船'''
        self.screen.blit(self.image, self.ship_rect)