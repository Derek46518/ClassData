import pygame, sys
from pygame.locals import *

# 初始化
pygame.init()
FPS = 60 # 設定每秒幾禎
fpsClock = pygame.time.Clock() # Clock

# 設定視窗
DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)
pygame.display.set_caption('Cat Animation')

# 設定一些基本的數值
WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
# 設定貓的x y 軸
catx = 10
caty = 10
direction = 'right' # 一開始的方向

while True: # the main game loop
     DISPLAYSURF.fill(WHITE)
    
     if direction == 'right': # 往右跑
         catx = catx + 5 
         
         if catx > DISPLAYSURF.get_width()-catImg.get_width(): # 如果跑到邊界 就讓貓往下跑
             direction = 'down'

     elif direction == 'down': # 往下跑
         caty = caty + 5
         if caty > DISPLAYSURF.get_height()-catImg.get_height(): # 如果讓貓跑到邊界 就讓貓往左跑
             direction = 'left'

     elif direction == 'left': # 往左跑
         catx = catx - 5
         if catx < 10: 
             direction = 'up'
     elif direction == 'up': # 往上跑
         caty = caty - 5
         if caty < 10:
             direction = 'right'
                
                
     DISPLAYSURF.blit(catImg, (catx, caty)) #繪製覆蓋整個視窗

     # 偵測事件
     for event in pygame.event.get():
         # 按叉叉就退出
         if event.type == QUIT:
             pygame.quit()
             sys.exit()
     #記得更新畫面
     pygame.display.update()
     #並且讓clock tick 一下
     fpsClock.tick(FPS)