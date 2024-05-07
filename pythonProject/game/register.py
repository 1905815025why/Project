import sqlite3
import wx
import startgame
import pygame
class FirstFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title="注册和登录",size=(400,700))
        panel = wx.Panel(self)                                                                                  # 创建画布
        panel.Center()                                                                                          #中心显示
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)                                                   #背景被擦除时调用此方法
        self.title = wx.StaticText(panel, label="请输入用户名和密码", pos=(130, 20))
        self.label_user = wx.StaticText(panel, label="用户名:", pos=(50, 50))                             # 用户名文本
        self.text_user = wx.TextCtrl(panel, pos=(100, 50), size=(235, 25), style=wx.TE_LEFT)              # 用户名文本，用户在此输入
        self.label_password = wx.StaticText(panel, pos=(50, 90), label="密 码:")                          # 密码文本
        self.text_password = wx.TextCtrl(panel, pos=(100, 90), size=(235, 25), style=wx.TE_PASSWORD)      # 密码文本，用户在此输入
        self.registerButton = wx.Button(panel,label='注册',pos=(300,125))                                  #创建注册按钮
        self.registerButton.Bind(wx.EVT_BUTTON,self.OnclickRegisterButton)
        self.sureButton=wx.Button(panel, label='确定', pos=(100, 175))                                    # 创建确定按钮
        self.sureButton.Bind(wx.EVT_BUTTON, self.OnclickSure)                                                  # 确定按钮的绑定事件
        self.cancelButton=wx.Button(panel, label='取消', pos=(200, 175))                                  # 创建取消按钮
        self.cancelButton.Bind(wx.EVT_BUTTON, self.OnclickCancel)                                              # 取消按钮的绑定事件
        self.Center()

    def OnEraseBack(self, event):
        get = event.GetDC()  # 获取上下文
        if not get:
            get = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            get.SetClippingRect(rect)
        get.Clear()
        background = wx.Bitmap("D:\\PC\\Pictures\\pading.jpg")
        get.DrawBitmap(background, 0, 0)

    
    def OnclickSure(self,event):
        """点击确定按钮执行方法"""
        information = ""
        username = self.text_user.GetValue()                                                                 # 获取输入的用户名
        password = self.text_password.GetValue()                                                             # 获取输入的密码
        if username == "" or password == "":
            information = "登录名和密码不能为空"
        else:
            conn=sqlite3.connect('user.db')
            cursor=conn.cursor()
            data=cursor.execute('select * from user where username=? and password=?',(username,password)).fetchone()
            if data:
                information="登录成功"
                wx.MessageBox(information)
                self.ClickSureButton(event)
            else:
                information = "用户名和密码不匹配"
                wx.MessageBox(information)                                                                               #弹出提示框
            cursor.close()
            conn.close()
    def OnclickCancel(self,event):
        """点击取消按钮执行方法"""
        self.text_user.SetValue("")
        self.text_password.SetValue("")
    def ClickSureButton(self,event):                   #实现跳转页面
        secondFrame = SecondFrame(self)
        secondFrame.Show()                            #显示主页面
        secondFrame.Center()                          #第二个页面中心显示
       # self.Disable()                               #用于禁止某个对象或控件，使其不在相应用户的交互


    def OnclickRegisterButton(self,event):
        information = ""
        registerFrame=RegisterFrame(self)
        registerFrame.Show()
        registerFrame.Center()

class RegisterFrame(wx.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        panel = wx.Panel(self)  # 创建画布
        panel.Center()  # 中心显示
        self.SetSize((400, 700))
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack6)
        self.title = wx.StaticText(panel, label="注册", pos=(190, 20))
        self.label_user = wx.StaticText(panel, label="用户名:", pos=(50, 50))  # 用户名文本
        self.text_user = wx.TextCtrl(panel, pos=(100, 50), size=(235, 25), style=wx.TE_LEFT)  # 用户名文本，用户在此输入
        self.label_password = wx.StaticText(panel, pos=(50, 90), label="密 码:")  # 密码文本
        self.text_password = wx.TextCtrl(panel, pos=(100, 90), size=(235, 25), style=wx.TE_PASSWORD)  # 密码文本，用户在此输入
        self.label_password1 = wx.StaticText(panel, pos=(50, 130), label="确认密码:")  # 密码文本
        self.text_password1 = wx.TextCtrl(panel, pos=(100, 130), size=(235, 25), style=wx.TE_PASSWORD)  # 密码文本，用户在此输入
        self.sureButton = wx.Button(panel, label='确定', pos=(100, 175))  # 创建确定按钮
        self.sureButton.Bind(wx.EVT_BUTTON, self.OnclickSure1)  # 确定按钮的绑定事件
        self.cancelButton = wx.Button(panel, label='取消', pos=(200, 175))  # 创建取消按钮
        self.cancelButton.Bind(wx.EVT_BUTTON, self.OnclickCancel1)  # 取消按钮的绑定事件
        self.Center()

    def OnEraseBack6(self, event):
        get = event.GetDC()  # 获取上下文
        if not get:
            get = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            get.SetClippingRect(rect)
        get.Clear()
        background = wx.Bitmap("D:\\PC\\Pictures\\pading.jpg")
        get.DrawBitmap(background, 0, 0)

    def OnclickSure1(self,event):
        information=""
        username = self.text_user.GetValue()                    # 获取输入的用户名
        password = self.text_password.GetValue()                # 获取输入的密码
        surePassword=self.text_password1.GetValue()             #获取确认密码
        if username=='' or password=='' or surePassword=='':
            information="用户名、密码和确认密码都不能为空！"
            wx.MessageBox(information)
        elif password!=surePassword:
            information="密码和确认密码不匹配！"
            wx.MessageBox(information)
        else:
            conn=sqlite3.connect('user.db')
            cursor=conn.cursor()
            data = cursor.execute('select * from user where username=? and password=?', (username, password)).fetchone()
            if data:
                information="用户已存在！"
                wx.MessageBox(information)
            else:
                cursor.execute("insert into user (username,password) values (?,?)",(username,password))
                conn.commit()                           #提交事务
                conn.close()                            #关闭数据库连接
                information="注册成功!"
                wx.MessageBox(information)

    def OnclickCancel1(self,event):
        information=""
        self.Close()



class SecondFrame(wx.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        panel = wx.Panel(self)
        self.SetPosition((0, 0))
        self.SetSize((400, 700))
        self.Show(True)
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack1)
        self.Show()
        Gamebutton = wx.Button(panel,size=(100,50),label="开始游戏",pos=(300,300))
        Gamebutton.Bind(wx.EVT_BUTTON,self.ClickGameButton)
        Gamebutton.Center()
        sizer = wx.BoxSizer(wx.VERTICAL)                                    #使控件垂直布局
        sizer.Add(Gamebutton,0,wx.ALIGN_CENTER,wx.ALL,20)             #添加窗口部件、设置部件大小、部件的对齐方式（中心对称位置）、边界大小（留出20像素空白）
        panel.SetSizer(sizer)                                               #决定panel部件如何布局
        self.SettingButton = wx.Button(panel,label='我的资料',pos=(250,500))
        self.SettingButton.Bind(wx.EVT_BUTTON,self.MyButton)
    def ClickGameButton(self):
        self.GetParent().Enable()                             #GetParent获取当前对象的父对象,Enable启用父对象
        pygame.init()  # 初始化pygame
        size = width, height = 400, 700  # 设置窗口
        gameScreen = pygame.display.set_mode(size)  # 显示窗口
        self.Close()


    def OnEraseBack1(self, event):
        get = event.GetDC()  # 获取上下文
        if not get:
            get = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            get.SetClippingRect(rect)
        get.Clear()
        background = wx.Bitmap("D:\\PC\\Pictures\\beijin.jpg")
        get.DrawBitmap(background, 0, 0)

    def MyButton(self,event):                                               #实现页面跳转
        thirdFrame = ThirdFrame(self)
        thirdFrame.Show()                                                   # 显示主页面
        thirdFrame.Center()                                                 # 第三个页面中心显示
    # self.Disable()

class ThirdFrame(wx.Frame):
    def __init__(self, parent=None, title='Third Frame Title', size=(400, 700)):
        super(ThirdFrame, self).__init__(parent, title=title, size=size)
        panel = wx.Panel(self)
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack2)
        self.username = wx.StaticText(panel, label="用户名:", pos=(100, 20))
        username_text = frame.text_user.GetValue()
        self.text1 = wx.TextCtrl(panel,value=username_text,pos=(150,20))
        self.password = wx.StaticText(panel,label="密  码:",pos=(100,50))
        password_text = frame.text_password.GetValue()
        self.text2 = wx.TextCtrl(panel, value=password_text, pos=(150, 50))
        self.change = wx.Button(panel,label="修改资料",pos=(150,80))
        self.change.Bind(wx.EVT_BUTTON,self.onClickChange)

    def OnEraseBack2(self, event):
        get = event.GetDC()  # 获取上下文
        if not get:
            get = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            get.SetClippingRect(rect)
        get.Clear()
        background = wx.Bitmap(r"D:\PC\Pictures\2.jpg")
        get.DrawBitmap(background, 0, 0)

    def onClickChange(self, event):
        forthFrame = ForthFrame(self)
        forthFrame.Show()               # 显示主页面
        forthFrame.Center()             # 第四个页面中心显示


class ForthFrame(wx.Frame):
    def __init__(self, parent=None,size=(400, 700)):
        super(ForthFrame, self).__init__(parent, size=size)
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel, label="请输入新用户名和新密码", pos=(130, 20))
        self.label_user = wx.StaticText(panel, label="新用户名:", pos=(50, 50))                                # 用户名文本
        self.text_user = wx.TextCtrl(panel, pos=(100, 50), size=(235, 25), style=wx.TE_LEFT)               # 用户名文本，用户在此输入
        self.label_password = wx.StaticText(panel, pos=(50, 90), label="新密 码:")  # 密码文本
        self.text_password = wx.TextCtrl(panel, pos=(100, 90), size=(235, 25), style=wx.TE_PASSWORD)        # 密码文本，用户在此输入
        self.sureButton = wx.Button(panel, label='确定修改', pos=(150, 175))  # 创建确定按钮
        self.sureButton.Bind(wx.EVT_BUTTON, self.OnclickSure)  # 确定按钮的绑定事件

    def OnclickSure(self,event):
        newUsername = self.text_user.GetValue()
        newPassword = self.text_password.GetValue()
        username_text = frame.text_user.GetValue()
        password_text = frame.text_password.GetValue()
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        if newPassword==username_text and newPassword==password_text:
            information = "与原用户名和密码一致！"
            wx.MessageBox(information)
        else:
            cursor.execute("update user set username=? where username=?", (newUsername, username_text))
            cursor.execute("update user set password=? where password=?", (newPassword, password_text))
            conn.commit()  # 提交事务
            # conn.close()  # 关闭数据库连接
            information = "修改成功!"
            wx.MessageBox(information)



if __name__ == '__main__':
    app = wx.App()                                      # 定义窗口
    frame = FirstFrame(parent=None, id=-1)              # 框架
    frame.Show()                                        # 显示窗口
    app.MainLoop()                                      # 一直显示窗口
