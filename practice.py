import pygame as pyg
#初始化
pyg.init()
#建立並設定視窗大小
width,height = 800,600
screen=pyg.display.set_mode((width,height))
#設定視窗標題
pyg.display.set_caption('Pygame Test')
#建立背景
bg=pyg.Surface(screen.get_size())
#背景轉換成pixel
bg=bg.convert()
#填入背景色(R,G,B)
bg.fill((177,229,237))

#建立字型模板
#系統內建文字可以用pyg.font.SysFont('微軟正黑體'48)
#可用字體可以使用pyg.font.get_fonts()找
font=pyg.font.SysFont('microsoftjhengheimicrosoftjhengheiuilight',48)
#設定文字(內容,抗鋸齒T/F,文字顏色,背景顏色)
text=font.render('中文字',True,(255,123,154),(152,164,152))
#將文字合併至背景bg
bg.blit(text,(300,200))
#在背景bg上繪製矩形(畫在哪個背景,顏色,[x1,y1,x2,y2],粗細/0是填滿)
pyg.draw.rect(bg,(0,255,0),[0,0,300,200],6)
#在背景bg上繪製線(畫在哪個背景,(x1,y1),(x2,y2),粗細)
pyg.draw.line(bg,(0,0,255),(0,0),(300,200),6)

#載入外部圖片
cat_img=pyg.image.load('cat.png')
#將圖片轉換成pixel 格式(alpha 包含)轉換透明度
cat_img=pyg.img.convert_alpha()
#將圖片合成至背景bg
bg.blit(cat_img,(0,0))

#初始化聲音模組
pyg.mixer.init()
#載入外部聲音
cat_meow=pyg.mixer.Sound('cat.wav')
#設定音量
cat_meow.set_volume(0.7)
#播放聲音
cat_meow.play()

#將背景bg圖層合併至視窗screen
screen.blit(bg,(0, 0))
#更新視窗畫面
pyg.display.update()



#遊戲執行
running=True
while running:
    #事件處理
    for event in pyg.event.get():
        #當遊戲視窗被關閉
        if event.type==pyg.QUIT:
            running=False
pyg.quit()
            

