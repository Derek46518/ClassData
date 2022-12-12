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

'''
判斷是否在多邊形內部
原理 : 利用射線法就可以判斷一個點是否在多邊形內部
如果焦點個數為奇數就是在多邊形內 反之則在外面
參考 : https://blog.csdn.net/leviopku/article/details/111224539
'''
def isInPolygon(p,poly):
    # 先取得輸入進來的點 放進去px, py裡面
    px,py = p
    # 先假設 flag 為 False 也就代表在外面
    flag = False
    # 用 i 來當作記錄在該陣列的第幾個位置
    # corner來當作數值
    for i, corner in enumerate(poly):
        j = i + 1 # 下一個點
        if(j>=len(poly)) : 
            j = 0
        # 先取兩個相鄰的點
        x1, y1 = corner
        x2, y2 = poly[j]
        #如果在點上 就直接寫True
        if(x1 == px and y1 == py) or (x2 == px and y2 == py):
            flag = True
            break
        
        # 如果該點在兩端點的y之間
        if(min(y1,y2)<py<=max(y1,y2)):
            # 計算 X
            # X 為 x1去加上 (py - y1) 乘以斜率分之一
            x = x1 + (py-y1) * (x2-x1)/(y2-y1)
            # 如果x在點上 就代表在內部
            if(x==px):
                flag = True
                break
            # 有焦點 讓 flag 變成 flag的相反
            elif x > px:
                flag = not flag
    return flag

# 判斷是否在方形區塊內
def isInRect(p,rect):
    x1, y1 = p
    x2, y2, len, width = rect
    if(x1<x2 or x1 > x2+len) : return False
    elif (y1<y2 or y1>y2+width) : return False
    else: return True

# 定義座標位置
POLYGON = ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106))
RECT = (200, 150, 100, 50)

# 一開始設定為 True 代表每個都會顯示
DISPLAY = [True,True,True,True,True,True,True]
# 開始繪圖吧
def draw():
    DISPLAYSURF.fill(WHITE)

    if (DISPLAY[0]) : pygame.draw.polygon(DISPLAYSURF, GREEN, POLYGON)
    
    if (DISPLAY[1]) : pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
    
    if (DISPLAY[2]) : pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
    
    if (DISPLAY[3]) : pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
    
    if (DISPLAY[4]) : pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
    
    if (DISPLAY[5]) : pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
    
    if (DISPLAY[6]) : pygame.draw.rect(DISPLAYSURF, RED, RECT)

# 點擊 被點到就設定為False

def click():
    global DISPLAY
    x,y = pygame.mouse.get_pos()
    if isInPolygon((x,y),POLYGON) : DISPLAY[0] = False
    if isInRect((x,y),(300,50,20,20)): DISPLAY[4] = False
    if isInRect((x,y),(300, 250, 40, 80)) : DISPLAY[5] = False
    if isInRect((x,y),RECT): DISPLAY[6] = False
 

def show():
    global DISPLAY
    DISPLAY = [True,True,True,True,True,True,True]

# 執行 Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            click()
        if event.type == pygame.KEYDOWN:
            show()
    # 每次進來都要再重畫一遍 才能看得出特色
    draw()     
    pygame.display.update()