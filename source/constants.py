# 窗口大小常量配置
SCREEN_W, SCREEN_H = 800, 600
SCREEN_SIZE = (SCREEN_W, SCREEN_H)

# 背景图片放大倍数
BG_MULTI = SCREEN_H / 224
# 背景角色放大倍数
PLAYER_MULTI = 2.9
# 砖块放大倍数
BRICK_MULTI = SCREEN_H / 224 + 0.01
# 敌人放大倍数
ENEMY_MULTI = 2.5

# 字体设置
FONT = 'FixedSys.ttf'

GRAVITY = 1.0
ANTI_GRAVITY = 0.3

# 临时变量落地高度
GROUND_HEIGHT= SCREEN_H - 62
