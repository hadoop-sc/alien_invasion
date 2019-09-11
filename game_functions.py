# -*- coding: utf-8 -*-
# 功能：定义游戏运行的方法
# 作者：邵春
# 时间：2019.09.11

import sys
import pygame

def check_events():

    '''响应按键和鼠标事件'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):

    '''更新屏幕上的图案，并刷新到新的屏幕'''

    screen.fill(ai_settings.screen_bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()