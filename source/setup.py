import pygame

from . import constants as C
from . import tools

# pygame模块初始化
pygame.init()
# 窗口初始化
# pygame.display.set_mode((C.SCREEN_W, C.SCREEN_H))
SCREEN = pygame.display.set_mode(C.SCREEN_SIZE)

# 加载素材文件夹下所有图片
GRAPHICS = tools.load_graphics('resources/graphics')
