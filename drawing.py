import pygame, sys
from pygame.locals import *
pygame.init()

# 設定螢幕大小
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')

# 設定顏色
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

# 定義座標位置
POLYGON = ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106))
RECT = (200, 150, 100, 50)


# 開始繪圖吧
def draw():
    DISPLAYSURF.fill(WHITE)

    pygame.draw.polygon(DISPLAYSURF, GREEN, POLYGON)
    
    pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
    
    pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
    
    pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
    
    pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
    
    pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
    
    pygame.draw.rect(DISPLAYSURF, RED, RECT)



# 執行 Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # 每次進來都要再重畫一遍 才能看得出特色
    draw()     
    pygame.display.update()