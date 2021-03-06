from tkinter import *
from tkinter import font
from telepot.loop import MessageLoop
import json
import tkinter.messagebox
import webbrowser
import requests
import folium
import urllib.request
import telepot
import tkinter.messagebox


ApiKey = "2EA5653A-003C-3EC5-9B6C-02D8A98D5E40"

g_Tk = Tk()
g_Tk.geometry("900x600+750+200")
DataList = []

with open('정왕동맛집.json', encoding="utf-8") as rstr:
        data = json.load(rstr)

photo = PhotoImage(file="food.gif")
imageLabel=Label(g_Tk,image=photo)
imageLabel.place(x=500, y=200)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        if msg['text'].upper() == '정왕':
            bot.sendMessage(chat_id, con)
        elif msg['text'] == '/start':
            pass
        else:
            bot.sendMessage(chat_id, '지원하지 않는 기능입니다')

bot = telepot.Bot('1305669655:AAEa6-AtWj4H5AYvpCFU37WeS4nNhZqi5ms')
bot.getMe()
MessageLoop(bot, handle).run_as_thread()

def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[맛집 검색 App]")
    MainText.pack()
    MainText.place(x=80)


def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=200, y=50)

    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=15, height=1, borderwidth=12, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(0, "식당이름(상호)")
    SearchListBox.insert(1, "식당주소(도로명)")
    SearchListBox.insert(2, "식당종류(메뉴)")
    SearchListBox.insert(3, "식당정보(상호)")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=50)

    ListBoxScrollbar.config(command=SearchListBox.yview)

def InitGmail():
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    Label(g_Tk, font=TempFont, text="메일").place(x=390, y=30)

    global mailLabel
    mailLabel = Entry(g_Tk, font=TempFont, width=25, borderwidth=5, relief='ridge')
    mailLabel.place(x=390, y=60)

    mailButton = Button(g_Tk, font=TempFont, text="보내기",command=SendGmail)
    mailButton.place(x=687, y=57)

def SendGmail():
    from Read_json import dataLst
    global host, port
    host = "smtp.gmail.com"
    port = "587"
    html = ""
    title2 = "맛집 탐방"
    senderAddr = "qaz0435@gmail.com"
    passwd = "!#!#black951"

    from Read_json import dataLst

    recipientAddr = mailLabel.get()

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg = MIMEMultipart('alternative')
    msg['Subject'] = title2
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgPart = MIMEText(con, 'plain')
    msg.attach(msgPart)

    s = smtplib.SMTP(host, port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)
    s.sendmail(senderAddr, [recipientAddr], msg.as_string(()))
    s.close()

def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(g_Tk, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=10, y=105)

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=110)


def SearchButtonAction():
    global SearchListBox

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    iSearchIndex = SearchListBox.curselection()[0]

    if iSearchIndex == 0:
        SearchLibrary0()
        
    elif iSearchIndex == 1:
        SearchLibrary1()

    elif iSearchIndex == 2:
        SearchLibrary2()

    elif iSearchIndex == 3:
        SearchLibrary3()

    RenderText.configure(state='disabled')


def SearchLibrary0():
    text = InputLabel.get()

    for i in data:
        if text in i['title']:
            RenderText.insert(INSERT, i['title'])
            RenderText.insert(INSERT, "\n\n")

def SearchLibrary1():
    text = InputLabel.get()

    for i in data:
        if text in i['roadAddress']:
            RenderText.insert(INSERT, i['title'])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, i['roadAddress'])
            RenderText.insert(INSERT, "\n\n")

def SearchLibrary2():
    text = InputLabel.get()

    for i in data:
        if text in i['category']:
            RenderText.insert(INSERT, i['title'])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, i['category'])
            RenderText.insert(INSERT, "\n\n")

def SearchLibrary3():
    text = InputLabel.get()

    for i in data:
        if text in i['title']:
            Address = i['roadAddress']
            MarkerName = i['title']
            RenderText.insert(INSERT, i['title'])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, i['roadAddress'])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, i['category'])
            RenderText.insert(INSERT, "\n")
            if i['telephone'] != '':
                RenderText.insert(INSERT, i['telephone'])
            else:
                RenderText.insert(INSERT, '*전화번호 없음!')
            RenderText.insert(INSERT, "\n")
            if i['link'] != '':
                RenderText.insert(INSERT, i['link'])
                webbrowser.open(i['link'])
            else:
                RenderText.insert(INSERT, '*웹사이트 없음!')
            RenderText.insert(INSERT, "\n\n")

            #url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=' + i['title'] + '.jpg'

    r = requests.get('http://apis.vworld.kr/new2coord.do?q=' + 
                     Address + '&apiKey=' + ApiKey + 
                     '&domain=http://map.vworld.kr/&output=json')
    a = r.json()

    m = folium.Map(
    location=[a['EPSG_4326_Y'], a['EPSG_4326_X']], zoom_start=15)
    # 좌표값, 줌 확대 배율

    folium.Marker(  # 마커 추가
      location=[a['EPSG_4326_Y'], a['EPSG_4326_X']],
      popup=MarkerName,
      icon=folium.Icon(color='red',icon='star')
    ).add_to(m)

    m.save('map.html')

    webbrowser.open('map.html')

    

def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=49, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')

    RenderText.insert(INSERT,"FV")


InitTopText()
InitSearchListBox()
InitInputLabel()
InitSearchButton()
InitRenderText()
InitGmail()

#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()

g_Tk.mainloop()