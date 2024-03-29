# 游戏主要入口
import pygame
from source import tools, setup
from source.states import main_menu, level, load_screen


def main():
    state_dict = {
        'main_menu': main_menu.MainMeun(),
        'load_screen': load_screen.LoadScreen(),
        'level': level.Level(),
        'game_over': load_screen.GameOver()
    }

    game = tools.Game(state_dict, 'main_menu')
    game.run()


if __name__ == '__main__':
    main()
