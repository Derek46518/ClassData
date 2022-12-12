import pygame
import time
from random import randint
#視窗大小
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
#常用顏色
GREEN = (73,188,11)
WHITE = (255,255,255)
#地鼠座標 / 分數 /遊戲時間 / 開始時間 / 狀態
x,y = None,None
score = 0
game_time = 20
start_time = 0
state = 0 #首頁0 遊戲中1 結束2
#建立視窗及頻率鐘
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('打地鼠')
clock = pygame.time.Clock()
#載入遊戲圖片
mallet = pygame.image.load('mallet.png') 
down_mallet = pygame.image.load('down-mallet.png')
mole = pygame.image.load('mole.png') 
grass = pygame.image.load('grass.png') 
#隱藏滑鼠座標顯示及初始化文字模組
pygame.mouse.set_visible(False)
pygame.font.init()

# FPS
FPS = 60
# 歡迎畫面
def welcome_screen():
    # 全部填滿草
    screen.blit(grass,(0,0))
    # 字體設定
    font = pygame.font.SysFont('corbel',48)
    # 文字設定
    text = font.render('Press ENTER to start',False,WHITE)
    # 畫出文字部分
    screen.blit(text,((SCREEN_WIDTH - text.get_width()) / 2, 185 ) )
    #畫出一個地鼠
    
    # 取得槌子的矩形範圍
   
    # 將槌子的中心點設在滑鼠點的位置
    
    
def play():
   # 取用遊戲狀態、分數及開始時間資訊
   global state, score, start_time
   # 設定遊戲開始時間 time.time() 會取得目前的時間
   start_time = time.time()
   # 將分數歸 0 且狀態設定為 1 遊玩中
   
   # 產生新的老鼠（這邊先立一個函式之後完成）
   
   # 產生瞬間先檢查是否有被打到（這邊先立一個函式之後完成）
  
  
def end():
   # 狀態改為 2 結束遊戲
   global state
   state = 2
 
def new_mole():
   # 隨機決定下一個老鼠產生的位置
   global x, y
   # x 從螢幕最左到右邊扣掉老鼠的寬都能取, y 則向下移 30 到底部扣掉老鼠的高都能取
   
 
# 判斷是否在方形區塊內
def isInRect(p,rect):
    # 先取得點座標
    x1, y1 = p
    # 再取得方形座標
    x2, y2, len, width = rect
    # 如果不在區域內 就 return false
    if(x1<x2 or x1 > x2+len) : return False
    elif (y1<y2 or y1>y2+width) : return False
    # else return true
    else: return True

def whack():
   global score
   # 取得滑鼠當前的位置
   
   # 取得老鼠的寬及高
   
   # 將座標計算是不是點擊在老鼠的圖片上, 如果有的話要加分和產生下一隻新的
   
   
# 遊戲畫面
def play_screen():
    # 畫出草
    screen.blit(grass,(0,0))
    # 字體設定
    font = pygame.font.SysFont('corbel',30)
    # 分數的文字
    text_score = font.render(str(score),False,WHITE)
    # 現在的時間
    current = game_time - (time.time() - start_time)
    # 如果時間結束 就跳到 end
    if current <= 0:
          end()
    # 時間的文字
    text_time = font.render(str(int(current)),False,WHITE)
    # 如果按下了滑鼠
    if pygame.mouse.get_pressed()[0]:
        # 就在鼠標位置顯示下降的槌子
        screen.blit(down_mallet, pygame.mouse.get_pos())
    # 如果不是的話
    else:
        # 就在鼠標的位置顯示一般的槌子
        screen.blit(mallet,pygame.mouse.get_pos())
    # 顯示分數
    screen.blit(text_score,(10,0))
    #顯示時間
    screen.blit(text_time,(370,0))
    # 顯示地鼠
    screen.blit(mole,(x,y))
        
# 結束話面
def end_screen():
    # 背景填滿綠色
    screen.fill(GREEN)
    # 設定字體樣板分別顯示遊戲結束、分數及重新開始按鈕
    font = pygame.font.Font(None, 30)
    game_over = font.render("GAME OVER", False, WHITE)
    font = pygame.font.Font(None, 25)
    # 分數
    points = font.render("Score: " + str(score), False, WHITE)
    font = pygame.font.Font(None, 22)
    restart = font.render("Press ENTER to play again", False, WHITE)
    # 將上述資訊顯示到螢幕上
    screen.blit(game_over, (SCREEN_WIDTH / 2 - game_over.get_width() / 2, 100))
    screen.blit(points, (SCREEN_WIDTH / 2 - points.get_width() / 2, 200))
    screen.blit(restart, (SCREEN_WIDTH / 2 - restart.get_width() / 2, 300))

#遊戲執行
running=True
while running:
    #事件處理
    for event in pygame.event.get():
        #當遊戲視窗被關閉
        if event.type==pygame.QUIT:#當遊戲視窗被關閉
            running=False
        elif state == 0:#遊戲還沒開始的事件
           if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    play()
        elif state == 1:#遊戲中的事件
            # 如果按下滑鼠 就打
           if event.type == pygame.MOUSEBUTTONDOWN:
               whack()           
        elif state == 2:#遊戲結束的事件
             if event.type == pygame.KEYDOWN and event.key ==pygame.K_RETURN:
                   play()
        # 依據state執行應該執行的畫面
        
        clock.tick(FPS)#限制畫面最高更新 60 FPS
        pygame.display.update()#更新畫面      
pygame.quit()

