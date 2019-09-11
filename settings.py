# -*- coding: utf-8 -*-
# 功能：游戏的设置定义类
# 作者：邵春
# 时间：2019.9.11

class Settings(object):
    '''存储游戏所有设置的类'''

    def __init__(self):
        '''初始化游戏的设置'''

        #屏幕设置
        self.screen_caption = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg_color = (0, 0, 0)