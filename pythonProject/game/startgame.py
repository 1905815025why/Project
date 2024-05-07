import sys
import random
import pygame
from pygame.locals import *

import register


class FlyBird(object):
    def __init__(self):
        self.birdrect = pygame.Rect(65,50,50,50)               #鸟的矩形
        self.startBird = [pygame.image.load(r"D:\PC\Pictures\bird.png"),                     #使鼠标能够控制鸟的飞行
                        pygame.image.load(r"D:\PC\Pictures\bird.png"),
                        pygame.image.load(r"D:\PC\Pictures\bird.png")]
        self.start = 0                                     #默认飞行状态
        self.x = 120                                       #鸟所在x轴坐标
        self.y = 350                                       #鸟所在y轴坐标，即上下飞行高度
        self.jump = False                                  #默认情况小鸟自动降落
        self.jumpHeight = 10                               #跳跃高度
        self.gravity = 5                                   #重力
        self.dead = False                                  #默认小鸟生命状态是活的

    def upgradeBird(self):
        if self.jump:                                       #小鸟跳跃
            self.jumpHeight -= 1                           #速度递减，上升速度越来越慢
            self.y -= self.jumpHeight                      #鸟y轴坐标减小，小鸟上升
        else:                                              #小鸟坠落
            self.gravity += 0.2                            #小鸟坠落，重力递增，下降越来越快
            self.y += self.gravity                         #鸟y轴坐标增加
        self.birdrect[1] = self.y                              #更改y轴坐标

class Pipe(object):
    def __init__(self):
        self.x = 400                                    #管道所在x轴坐标
        self.upPipe = pygame.image.load(r"D:\PC\Pictures\uppipe(1).png")               #加载上管道图片
        self.upPipe = pygame.transform.scale(self.upPipe,(80,500))
        self.dowmPipe = pygame.image.load(r"D:\PC\Pictures\downpipe.png")              #加载下管道图片
        self.dowmPipe = pygame.transform.scale(self.dowmPipe,(50,500))
    def updatePipe(self):
        self.x -= 5                                                                 #管道x轴坐标递减
        if self.x < -80:
            global score
            score += 1
            self.x = 400                                                            #当管道运行到一定位置，即小鸟飞跃管道，分数加1，并重置管道

def createMap():
    gameScreen.fill((255,255,255))                      #填充颜色
    gameScreen.blit(background,(0,0))              #填入到背景
                                                        #显示管道
    gameScreen.blit(pipe.upPipe,(pipe.x,-300))     #上管道坐标位置
    gameScreen.blit(pipe.dowmPipe,(pipe.x,500))    #下管道坐标位置
    pipe.updatePipe()                                   #管道移动
    if bird.dead:                                       #显示小鸟，撞管道状态
        bird.start = 2                                  #起飞状态
    elif bird.jump:
        bird.start = 1
    gameScreen.blit(bird.startBird[bird.start],(bird.x,bird.y))             #设置小鸟坐标
    bird.upgradeBird()                                  #鸟移动
    pygame.display.update()                             #更新显示

    gameScreen.blit(typeface.render(str(score),-1,(255,255,255)),(200,50))             #设置颜色及坐标位置
    pygame.display.update()                                                              #更新显示

def checkCrash():
    uprect = pygame.Rect(pipe.x,-300,                                               #上方管子的矩形位置
                         pipe.upPipe.get_width()-10,
                         pipe.upPipe.get_height())
    downrect = pygame.Rect(pipe.x,500,                                              #下方管子的矩形位置
                           pipe.dowmPipe.get_width()-10,
                           pipe.dowmPipe.get_height())
    if uprect.colliderect(bird.birdrect) or downrect.colliderect(bird.birdrect):    #检测小鸟与上下方管子是否碰撞
        bird.dead = True
    if not 0 < bird.birdrect[1] <height:                                            #检测小鸟是否飞出边界
        bird.dead = True
        return True
    else:
        return False


def resultScore():
    text1 = "Game Over"                                                #游戏失败提示
    text2 = "Your score is:"+str(score)                                #显示游戏分数
    typeface1 = pygame.font.SysFont('Arial',40)             #设置游戏结束字体
    text1Color = typeface.render(text1,1,(242,3,36))    #设置游戏结束字体颜色
    typeface2 = pygame.font.SysFont('Arial',40)            #设置分数的字体和字体大小
    text2Color = typeface.render(text2,1,(253,177,6))   #设置分数的颜色
    gameScreen.blit(text1Color,[gameScreen.get_width()/2-text1Color.get_width()/2,100])       #设置游戏结束显示位置
    gameScreen.blit(text2Color,[gameScreen.get_width()/2-text2Color.get_width()/2,200])       #设置分数显示位置
    pygame.display.flip()                                                                          #更新整个待显示的对象到屏幕上


def TimeOut():
    countdown_time = 300  # 设置倒计时时间（秒）
    pygame.time.set_timer(pygame.USEREVENT + 1, 1000)  # 创建一个计时器，每秒触发一次事件
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.USEREVENT + 1:  # 检测计时器事件
                countdown_time -= 1
                if countdown_time < 0:
                    bird.dead = True  # 倒计时结束后游戏结束
                    break

        gameScreen.fill((255,255,255,0))  # 清屏
        font = pygame.font.Font(None, 36)  # 绘制倒计时文本
        text = font.render('Time left: {}'.format(countdown_time), True, (0, 0, 255))
        gameScreen.blit(text, (20, 20))
        pygame.display.flip()  # 更新屏幕显示


if __name__ == '__main__':
    while True:
        pygame.init()                                       #初始化pygame
        size = width, height = 400, 700  # 设置窗口
        gameScreen = pygame.display.set_mode(size)  # 显示窗口
        pygame.font.init()                                  #初始化字体
        typeface = pygame.font.SysFont('Arial',40)  #设置默认字体和字体大小
        clock = pygame.time.Clock()                         #设置时钟
        # TimeOut()
        game_time = 0                                       #定义时钟变量
        pipe = Pipe()                                       #实例化管道类
        bird = FlyBird()                                    #实例化鸟类
        pygame.display.update()
        score = 0                                           #游戏开始时的分数
        text3 = "重新开始"
        text4 = "退出游戏"
        text3Font = pygame.font.SysFont('Arial',(36))               #创建一个文字对象，设置字体和大小
        text3 = typeface.render(text3,1,(255,255,255))     #将文本渲染为Surface对象，设置文本颜色为白色
        text3X = ()
        while True:
            clock.tick(60)                                               #每秒执行60次
            for event in pygame.event.get():                              #轮询事件
                if event.type == pygame.QUIT:
                    sys.exit()
                if(event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not bird.dead:
                    bird.jump = True                                                    #跳跃
                    bird.gravity = 5                                                    #重力
                    bird.jumpHeight = 10                                                #跳跃速度
            background = pygame.image.load(r"D:\PC\Pictures\gamepage.png")              #加载背景图片
            background = pygame.transform.scale(background,(400,700))
            if checkCrash():                                                            #检测小鸟生命状态
                resultScore()                                                            #如果小鸟死亡显示游戏分数

                reSsize = pygame.Rect(100,300,200,50)                                        #设置按钮的尺寸和位置
                Button1 = pygame.sprite.Sprite()
                text3 = "Restart Game"
                text3Font = pygame.font.SysFont('Arial', (25))                          # 创建一个文字对象，设置字体和大小
                text3 = text3Font.render(text3, 1, (255, 255, 255))            # 将文本渲染为Surface对象，设置文本颜色为白色
                text3Rect = text3.get_rect()                                                # 获取文本的矩形区域
                pygame.draw.rect(gameScreen,(0,255,0),reSsize)                         #在屏幕上绘制按钮矩形
                gameScreen.blit(text3, (120, 310))


                exitSize = pygame.Rect(100,400,200,50)
                Button2 = pygame.sprite.Sprite()
                text4 = "Exit Game"
                text4Font = pygame.font.SysFont('Arial', (25))                   # 创建一个文字对象，设置字体和大小
                text4 = text4Font.render(text4, 1, (255, 255, 255))      # 将文本渲染为Surface对象，设置文本颜色为白色
                text4Rect = text4.get_rect()  # 获取文本的矩形区域
                pygame.draw.rect(gameScreen,(255,0,0),exitSize)                  #在屏幕上绘制按钮矩形
                gameScreen.blit(text4, (140, 410))
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == QUIT:
                        continue
                    elif event.type == MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if reSsize.collidepoint(mouse_pos):  # 检查鼠标是否点击了Restart按钮
                            print("Restart button clicked!")
                                # 在这里添加你希望在点击Restart按钮后执行的代码
                        elif exitSize.collidepoint(mouse_pos):  # 检查鼠标是否点击了Exit按钮
                            pygame.quit()

            else:
                createMap()                                                             #创建地图

