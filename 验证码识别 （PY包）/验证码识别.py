# -*- coding:utf-8 -*- 
# -*- coding:utf-8 -*- 

import sys
import urllib2
import time
import re
import os
import string
import urllib
import Image
import pytesser
from pytesser import *

def cancel_zero(str):
    i=0
    num=0
    ansstr=''
    while i<len(str):
        if str[i]=='\n' or str[i]==' ':
            i+=1
            continue
        else:
            ansstr+=str[i]
            num+=1
        i+=1
    return ansstr

def pixfun(r,g,b):
    grey=(r*224 + g*356 + b*114 + 500) / 1000
    #return grey,grey,grey
    if grey < 125:
        return 0,0,0
    return 255,255,255

def under(image,x,y,width,height):
    count=0
    if x<=0 or y<=0 or x>=width-1 or y>=height-1:
        return
    if image[x,y]==(0,0,0):
        if image[x-1,y]==(255,255,255):
            count+=1
        if image[x+1,y]==(255,255,255):
            count+=1
        if image[x,y-1]==(255,255,255):
            count+=1
        if image[x,y+1]==(255,255,255):
            count+=1
        if count >= 3:
            return 1
    if image[x,y]==(255,255,255):
        if image[x-1,y]==(0,0,0):
            count+=1
        if image[x+1,y]==(0,0,0):
            count+=1
        if image[x,y-1]==(0,0,0):
            count+=1
        if image[x,y+1]==(0,0,0):
            count+=1
        if count == 4:
            return 2
    return 0

def get_inside(str):
    im = Image.open(str)
    #dr = ImageDraw.Draw(im)
    im=im.convert('L')
    threshold = 127
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    im = im.point(table, '1')

    pix = im.load()
    width = im.size[0]
    height = im.size[1]
    for x in range(width):
        for y in range(height):
            if under(pix,x,y,width,height)==1:
                im.putpixel((x,y),(255,255,255))
            if under(pix,x,y,width,height)==2:
                im.putpixel((x,y),(0,0,0))

    #im.save('captcha2.png')

    strs = image_to_string(im)
    return cancel_zero(strs)

if __name__=='__main__':
    while 1:
        url=raw_input()
        print get_inside(url)