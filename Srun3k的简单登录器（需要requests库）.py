# -*- coding: utf-8 -*-
import requests
import sys
import os
from os import *
username = "username用户名放在引号里面"
password = "密码的MD5，放在引号里面"
payload = {'username': username, 'drop': 0, 'password':password, 'type': 1, 'n': 100}
r = requests.post('http://10.0.0.55/cgi-bin/do_login', data=payload)
