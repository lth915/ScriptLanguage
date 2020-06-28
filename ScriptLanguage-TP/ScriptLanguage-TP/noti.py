#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback


encText="정왕동 맛집"
start = 100

key = 'cf7S5Eg7pymBjoGjsSX_'
TOKEN = '1305669655:AAEa6-AtWj4H5AYvpCFU37WeS4nNhZqi5ms'
MAX_MSG_LENGTH = 300
baseurl = "https://openapi.naver.com/v1/search/local?query=" + encText + "&display=10" + "&start=" + str(start)+key
bot = telepot.Bot(TOKEN)

def getData(loc_param):
    res_list = []
    url = baseurl+'?KEY='+ key + '&SIGUN_CD='+loc_param
    #print(url)
    res_body = urlopen(url).read()
    #print(res_body)
    soup = BeautifulSoup(res_body, 'html.parser')
    #print(soup)
    items = soup.findAll('row')
    #print(items)
    for row in items:
        row = re.sub('<.*?>', '|', row.text)
        parsed = row.split('|')

        try:
            rows = parsed[0]+'  '+parsed[1]+'  '+parsed[2]+'  '+parsed[3]+'  '+parsed[4]+'  '

        except IndexError:
            rows = row.replace('|', ',')


        if rows:
            res_list.append(rows.strip())
    #print(res_list)
    return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)

def run(param='11710'):
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs( user TEXT, log TEXT, PRIMARY KEY(user, log) )')
    conn.commit()

    user_cursor = sqlite3.connect('users.db').cursor()
    user_cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    user_cursor.execute('SELECT * from users')

    for data in user_cursor.fetchall():
        user, param = data[0], data[1]
        print(user, param)
        res_list = getData( param)
        msg = ''
        for r in res_list:
            try:
                cursor.execute('INSERT INTO logs (user,log) VALUES ("%s", "%s")'%(user,r))
            except sqlite3.IntegrityError:
                # 이미 해당 데이터가 있다는 것을 의미합니다.
                pass
            else:
                print( str(datetime.now()).split('.')[0], r )
                if len(r+msg)+1>MAX_MSG_LENGTH:
                    sendMessage( user, msg )
                    msg = r+'\n'
                else:
                    msg += r+'\n'
        if msg:
            sendMessage( user, msg )
    conn.commit()

if __name__=='__main__':
    today = date.today()
    current_month = today.strftime('%Y%m')

    print( '[',today,']received token :', TOKEN )

    pprint( bot.getMe() )

    run(current_month)