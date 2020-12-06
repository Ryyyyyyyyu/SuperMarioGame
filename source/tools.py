# 工具和游戏主控
import os
import pygame

from source import constants as C


class Game:
    def __init__(self, state_dict, start_state):
        # 获取当前窗口对象
        self.screen = pygame.display.get_surface()
        # 设置窗口标题
        pygame.display.set_caption('超级马里奥')
        # 创建时钟对象 (可以控制游戏循环频率)
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        self.state_dict = state_dict
        self.state = self.state_dict[start_state]

    def update(self):
        if self.state.finished:
            next_state = self.state.next
            # 各种的类中初始化时已经将finished改为False了，这行目前在P11的进度里看看来可以不要
            self.state.finished = False
            self.state = self.state_dict[next_state]
        self.state.update(self.screen, self.keys)

    def run(self):
        """
        游戏启动函数
        :param GRAPHICS: 传入获取到的所有图片对象
        :return:
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()

            self.update()
            # 更新屏幕
            pygame.display.update()
            # 设置游戏帧数
            self.clock.tick(60)


def load_graphics(path, accept=('.jpg', '.png', '.gif', '.bmp')):
    """
    处理素材图片
    :param path: 素材图片路径
    :param accept: 图片后缀类型
    :return:  返回处理后的图片
    """
    # 定义一个空字典存放处理后的图片
    graphics = {}
    # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    # 循环获取目录下的文件名
    for pic in os.listdir(path):
        # 将文件名和扩展名拆分存放
        name, ext = os.path.splitext(pic)
        # ext.lower()将扩展后缀名转换成小写，判断后缀名是否在指定后缀名内
        if ext.lower() in accept:
            # 加载文件图片
            img = pygame.image.load(os.path.join(path, pic))
            # 判断图片是否透明
            if img.get_alpha():
                # 对透明图片进行像素格式转换
                img = img.convert_alpha()
            else:
                # 对不透明图片进行像素格式转换
                img = img.convert()
            # 将处理完成的图片存放到字典中，用图片名作为KEY值
            graphics[name] = img
    return graphics


def get_image(sheet, x=0, y=0, width=C.SCREEN_W, height=C.SCREEN_H, colorkey=(0, 0, 0), scale=1):
    """
    从已经加载的图片里获取某部分图片的方法
    :param sheet:传入加载的图片
    :param x:传入的sheet中需要获取的部分图片的左上角的X坐标
    :param y:传入的sheet中需要获取的部分图片的左上角的Y坐标
    :param width:需要获取的部分图片的宽
    :param height:需要获取的部分图片的高
    :param colorkey:传入的图片的底色
    :param scale:图片放大的倍数
    :return:返回获取的部分图片
    """
    # 创建一个和所需部分图片大小一样的空图层
    image = pygame.Surface((width, height))
    # 获取的sheet图片中左上部分坐标为下x,y，width, height为宽高的部分画在image的(0, 0)
    image.blit(sheet, (0, 0), (x, y, width, height))
    # 设置背景色为透明
    image.set_colorkey(colorkey)
    # 将iamge的宽高放大scale倍数
    iamge = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
    return iamge

