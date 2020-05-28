import random

import pygame

# 设置游戏屏幕大小
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 600
# 初始化 pygame
pygame.init()
# 设置游戏界面大小
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
# 游戏界面标题
pygame.display.set_caption('超级马里奥')
mario_image = pygame.image.load('2.png')

while True:
    # 更新部分
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
        elif event.type == pygame.KEYUP:
            key = pygame.key.get_pressed()

        screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        screen.blit(mario_image, (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))
        pygame.display.update()
        clock.tick(3)
