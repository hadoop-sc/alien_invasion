# -*- coding:utf-8 -*-
# 功能：python游戏开发第一课
# 作者：邵春
# 时间：2019.09.11

import pygame

from settings import Settings
from ships import Ships
import game_functions as gf

# 游戏入口
def run_game():

    # 初始化游戏外观并创建一个屏幕对象
    pygame.init()
    alien_settings = Settings()

    game_screen = pygame.display.set_mode((alien_settings.screen_width, alien_settings.screen_height))
    pygame.display.set_caption(alien_settings.screen_caption)

    #创建一艘飞船
    ship = Ships(game_screen)
    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events()

        #每次循环重绘屏幕
        gf.update_screen(alien_settings,game_screen,ship)




run_game()
