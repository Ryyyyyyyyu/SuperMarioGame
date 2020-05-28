import os
import sys

import pygame


class Game:
    def __init__(self, state_dict, start_state):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.get_surface()
        self.keys = pygame.key.get_pressed()
        self.state_dict = state_dict
        self.state = self.state_dict[start_state]

    def update(self):
        if self.state.finished:
            next_state = self.state.next
            self.state.finished = False
            self.state = self.state_dict[next_state]
        self.state.update(self.screen, self.keys)



    def run(self):
        while True:
            # 更新部分
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()

            # state.update(self.screen, self.keys)
            self.update()
            pygame.display.update()
            self.clock.tick(60)


def load_graphics(path, accept=('.jpg', '.png', '.bmp', '.gif')):
    graphics = {}
    for pic in os.listdir(path):  # os.listdir(path)返回path目录下面的所有文件
        name, ext = os.path.splitext(pic)  # os.path.splitext(pic)分离文件名称和扩展名
        # print(name, r'/n', ext)
        # name1, ext1 = os.path.split(pic)
        # print(name1, r'/n',ext1)
        if ext.lower() in accept:  # ext.lower()转化为小写字母
            img = pygame.image.load(os.path.join(path, pic))  # 图片不在同一路径，需传入绝对路径
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img
    return graphics


def get_image(sheet, x, y, width, height, colorkey, scale):  # sheet图片x,y方框左上角坐标width, height方框宽高colorkey图片底色 scale放大倍数参数
    image = pygame.Surface((width, height))
    image.blit(sheet, (0, 0), (x, y, width, height))  # pygame.Surface.blit()将一个图像（Surface 对象）绘制到另一个图像上方 0, 0 代表要画到哪个位置，x, y, width, height 代表sheet即图片哪个区域要取出来
    image.set_colorkey(colorkey)  # 设置 colorkeys
    image = pygame.transform.scale(image, (int(width * scale), int(
        height * scale)))  # 对图像进行缩放 pygame.transform.smoothscale()平滑缩放  pygame.transform.scale() 快速缩放
    return image
