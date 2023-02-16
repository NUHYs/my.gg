import tkinter
from tkinter import *
from tkinter import filedialog, Text, Image, font, ttk
import tkinter.font as tkFont
import json
import requests
import time
from tkinter import *
from datetime import datetime
import datetime

api_key = 'RGAPI-0e0885f4-a30f-443f-a825-825a927545dd'

option0 = {'font': (None, 16)}
option1 = {'font': (None, 20)}
option2 = {'font': (None, 22)}
option4 = {'font': (None, 10)}
root = Tk()
root.title("MY.GG")

root.geometry("640x480")

root.resizable(True, True)  # x ,y

font1 = tkinter.font.Font(family="맑은 고딕", size=16, slant="italic")

txt1 = Text(root, width=20, height=1, font=font1)
txt1.place(x=160, y=60)
btn1 = Button(root, text="검색", bg='lightgray',
              command=lambda: [CH(), search()])
btn1.place(x=403, y=60, width=40, height=35)

CHBR = False
CHBRNONE = False
CHBF = False
CHBFNONE = False
CHBPLNONE = False
CHBNAME = False


def search():
    global CHBR, name, NEXTBtn, CHBNAME, CHBRNONE, CHBF, CHBFNONE, CHBPLNONE, labelPLNONE, labelNAME, label3, label4, label5, label6, label7, labelF1, labelF2, labelF3, labelF4, labelF5, labelF6, labelF7, labelNONE

    name = str(txt1.get("1.0", 'end-1c'))
    URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name
    res = requests.get(URL, headers={"X-Riot-Token": api_key})
    if res.status_code == 200:
        resobj = json.loads(res.text)
        URL = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + \
            resobj["id"]
        res = requests.get(URL, headers={"X-Riot-Token": api_key})
        rankinfo = json.loads(res.text)
        labelNAME = Label(root, text="닉네임: {0}".format(
            name), **option2, fg="gray")
        labelNAME.place(x=153, y=100)
        CHBNAME = True
        for i in rankinfo:
            if i["queueType"] == "RANKED_SOLO_5x5":
                for i in rankinfo[1: 2]:
                    if i["queueType"] not in "RANKED_FLEX_SR":
                        labelF3 = Label(root, text="자유랭크", **
                                        option1, fg="blue")
                        labelF3.place(x=430, y=200)
                        labelNONE = Label(root, text="검색결과 없음",
                                          **option0, fg="black")
                        labelNONE.place(x=420, y=250)
                        CHBFNONE = True
                label3 = Label(root, text="솔랭", **option1, fg="blue")
                label3.place(x=50, y=200)
                Rcolor = ""
                if i["tier"] == "IRON":
                    Rcolor = "black"
                elif i["tier"] == "BRONZE":
                    Rcolor = "brown"
                elif i["tier"] == "SILVER":
                    Rcolor = "silver"
                elif i["tier"] == "GOLD":
                    Rcolor = "gold"
                elif i["tier"] == "PLATINUM":
                    Rcolor = "lightgreen"
                elif i["tier"] == "DIAMOND":
                    Rcolor = "blue"
                elif i["tier"] == "MASTER":
                    Rcolor = "purple"
                elif i["tier"] == "MASTER":
                    Rcolor = "purple"
                elif i["tier"] == "GRANDMASTER":
                    Rcolor = "darkred"
                elif i["tier"] == "CHALLENGER":
                    Rcolor = "yellow"
                label4 = Label(
                    root, text=f"티어: {i['tier']} {i['rank']}", **option0, fg="{0}".format(Rcolor))
                label4.place(x=30, y=240)
                label5 = Label(
                    root, text=f"점수: {i['leaguePoints']}", **option0, fg="black")
                label5.place(x=30, y=280)
                label6 = Label(
                    root, text=f"승: {i['wins']}판, 패: {i['losses']}판", **option0, fg="black")
                label6.place(x=30, y=320)
                WL = int(i['wins']) / (int(i['wins']) + int(i['losses'])) * 100
                label7 = Label(
                    root, text=f"승률: {round(WL)}%", **option0, fg="black")
                label7.place(x=30, y=360)
                NEXTBtn = Button(root, text="상세정보 보기",
                                 bg='lightgray', command=lambda: page2())
                NEXTBtn.place(x=255, y=350, width=95, height=30)
                CHAR = True
            else:
                for i in rankinfo[0: 1]:
                    if i["queueType"] not in "RANKED_SOLO_5x5":
                        label3 = Label(root, text="솔랭", **option1, fg="blue")
                        label3.place(x=50, y=200)
                        labelNONE = Label(root, text="검색결과 없음",
                                          **option0, fg="black")
                        labelNONE.place(x=22, y=250)
                        CHBRNONE = True
                labelF3 = Label(root, text="자유랭크", **option1, fg="blue")
                labelF3.place(x=430, y=200)
                Rcolor = ""
                if i["tier"] == "IRON":
                    Rcolor = "black"
                elif i["tier"] == "BRONZE":
                    Rcolor = "brown"
                elif i["tier"] == "SILVER":
                    Rcolor = "silver"
                elif i["tier"] == "GOLD":
                    Rcolor = "gold"
                elif i["tier"] == "PLATINUM":
                    Rcolor = "lightgreen"
                elif i["tier"] == "DIAMOND":
                    Rcolor = "blue"
                elif i["tier"] == "MASTER":
                    Rcolor = "purple"
                elif i["tier"] == "MASTER":
                    Rcolor = "purple"
                elif i["tier"] == "GRANDMASTER":
                    Rcolor = "darkred"
                elif i["tier"] == "CHALLENGER":
                    Rcolor = "darkyellow"
                labelF4 = Label(
                    root, text=f"티어: {i['tier']} {i['rank']}", **option0, fg="{0}".format(Rcolor))
                labelF4.place(x=410, y=240)
                labelF5 = Label(
                    root, text=f"점수: {i['leaguePoints']}", **option0, fg="black")
                labelF5.place(x=410, y=280)
                labelF6 = Label(
                    root, text=f"승: {i['wins']}판, 패: {i['losses']}판", **option0, fg="black")
                labelF6.place(x=410, y=320)
                WL = int(i['wins']) / (int(i['wins']) + int(i['losses'])) * 100
                labelF7 = Label(
                    root, text=f"승률: {round(WL)}%", **option0, fg="black")
                labelF7.place(x=410, y=360)
                NEXTBtn = Button(root, text="상세정보 보기",
                                 bg='lightgray', command=lambda: page2())
                NEXTBtn.place(x=255, y=350, width=95, height=30)
                CHBF = True
    else:
        if(str(txt1.get("1.0", 'end-1c')) == ""):
            pass
        labelPLNONE = Label(root, text="소환사가 존재하지 않습니다", **option1, fg="red")
        labelPLNONE.place(x=125, y=100)
        CHBPLNONE = True


Champ = ""


def CHID(id):
    global Champ
    if str(id) == "266":
        Champ = "Aatrox"
    elif str(id) == "103":
        Champ = "Ahri"
    elif str(id) == "84":
        Champ = "Akali"
    elif str(id) == "166":
        Champ = "Akshan"
    elif str(id) == "12":
        Champ = "Alistar"
    elif str(id) == "32":
        Champ = "Amumu"
    elif str(id) == "34":
        Champ = "Anivia"
    elif str(id) == "1":
        Champ = "Annie"
    elif str(id) == "523":
        Champ = "Aphelios"
    elif str(id) == "22":
        Champ = "Ashe"
    elif str(id) == "136":
        Champ = "Aurelion Sol"
    elif str(id) == "268":
        Champ = "Azir"
    elif str(id) == "432":
        Champ = "Bard"
    elif str(id) == "53":
        Champ = "Blitzcrank"
    elif str(id) == "63":
        Champ = "Brand"
    elif str(id) == "201":
        Champ = "Braum"
    elif str(id) == "51":
        Champ = "Caitlyn"
    elif str(id) == "164":
        Champ = "Camille"
    elif str(id) == "69":
        Champ = "Cassiopeia"
    elif str(id) == "31":
        Champ = "Cho'Gath"
    elif str(id) == "42":
        Champ = "Corki"
    elif str(id) == "122":
        Champ = "Darius"
    elif str(id) == "131":
        Champ = "Diana"
    elif str(id) == "119":
        Champ = "Draven"
    elif str(id) == "36":
        Champ = 'Dr. Mundo'
    elif str(id) == "245":
        Champ = "Ekko"
    elif str(id) == "60":
        Champ = "Elise"
    elif str(id) == "28":
        Champ = 'Evelynn'
    elif str(id) == "81":
        Champ = 'Ezreal'
    elif str(id) == "9":
        Champ = "Fiddlesticks"
    elif str(id) == "114":
        Champ = "Fiora"
    elif str(id) == "105":
        Champ = "Fizz"
    elif str(id) == "3":
        Champ = "Galio"
    elif str(id) == "41":
        Champ = "Gangplank"
    elif str(id) == "86":
        Champ = "Garen"
    elif str(id) == "150":
        Champ = "Gnar"
    elif str(id) == "79":
        Champ = "Gragas"
    elif str(id) == "104":
        Champ = "Graves"
    elif str(id) == "887":
        Champ = "Gwen"
    elif str(id) == "120":
        Champ = 'Hecarim'
    elif str(id) == "74":
        Champ = "Heimerdinger"
    elif str(id) == "420":
        Champ = "Illaoi"
    elif str(id) == "39":
        Champ = 'Irelia'
    elif str(id) == "427":
        Champ = "Ivern"
    elif str(id) == "40":
        Champ = "Janna"
    elif str(id) == "59":
        Champ = 'Jarvan IV'
    elif str(id) == "24":
        Champ = "Jax"
    elif str(id) == "126":
        Champ = 'Jayce'
    elif str(id) == "202":
        Champ = "Jhin"
    elif str(id) == "222":
        Champ = 'Jinx'
    elif str(id) == "145":
        Champ = "Kai'Sa"
    elif str(id) == "429":
        Champ = 'Kalista'
    elif str(id) == "43":
        Champ = "Karma"
    elif str(id) == "30":
        Champ = "Karthus"
    elif str(id) == "38":
        Champ = 'Kassadin'
    elif str(id) == "55":
        Champ = 'Katarina'
    elif str(id) == "10":
        Champ = "Kayle"
    elif str(id) == "141":
        Champ = "Kayn"
    elif str(id) == "85":
        Champ = "Kennen"
    elif str(id) == "121":
        Champ = "Kha'Zix"
    elif str(id) == "203":
        Champ = 'Kindred'
    elif str(id) == "240":
        Champ = 'Kled'
    elif str(id) == "96":
        Champ = "Kog'Maw"
    elif str(id) == "7":
        Champ = 'LeBlanc'
    elif str(id) == "64":
        Champ = 'Lee Sin'
    elif str(id) == "89":
        Champ = "Leona"
    elif str(id) == "876":
        Champ = "Lillia"
    elif str(id) == "127":
        Champ = 'Lissandra'
    elif str(id) == "236":
        Champ = "Lucian"
    elif str(id) == "117":
        Champ = 'Lulu'
    elif str(id) == "99":
        Champ = "Lux"
    elif str(id) == "54":
        Champ = 'Malphite'
    elif str(id) == "90":
        Champ = "Malzahar"
    elif str(id) == "57":
        Champ = 'Maokai'
    elif str(id) == "11":
        Champ = "Master Yi"
    elif str(id) == "21":
        Champ = 'Miss Fortune'
    elif str(id) == "62":
        Champ = "Wukong"
    elif str(id) == "82":
        Champ = 'Mordekaiser'
    elif str(id) == "25":
        Champ = "Morgana"
    elif str(id) == "267":
        Champ = 'Nami'
    elif str(id) == "75":
        Champ = "Nasus"
    elif str(id) == "111":
        Champ = 'Nautilus'
    elif str(id) == "518":
        Champ = 'Neeko'
    elif str(id) == "76":
        Champ = 'Nidalee'
    elif str(id) == "56":
        Champ = 'Nocturne'
    elif str(id) == "20":
        Champ = 'Nunu & Willump'
    elif str(id) == "2":
        Champ = 'Olaf'
    elif str(id) == "61":
        Champ = 'Orianna'
    elif str(id) == "516":
        Champ = 'Ornn'
    elif str(id) == "80":
        Champ = 'Pantheon'
    elif str(id) == "78":
        Champ = 'Poppy'
    elif str(id) == "555":
        Champ = 'Pyke'
    elif str(id) == "246":
        Champ = 'Qiyana'
    elif str(id) == "133":
        Champ = 'Quinn'
    elif str(id) == "497":
        Champ = 'Rakan'
    elif str(id) == "33":
        Champ = 'Rammus'
    elif str(id) == "421":
        Champ = "Rek'Sai"
    elif str(id) == "526":
        Champ = 'Rell'
    elif str(id) == "58":
        Champ = 'Renekton'
    elif str(id) == "107":
        Champ = 'Rengar'
    elif str(id) == "92":
        Champ = 'Riven'
    elif str(id) == "68":
        Champ = 'Rumble'
    elif str(id) == "13":
        Champ = 'Ryze'
    elif str(id) == "360":
        Champ = 'Samira'
    elif str(id) == "113":
        Champ = 'Sejuani'
    elif str(id) == "235":
        Champ = 'Senna'
    elif str(id) == "147":
        Champ = 'Seraphine'
    elif str(id) == "875":
        Champ = 'Sett'
    elif str(id) == "35":
        Champ = 'Shaco'
    elif str(id) == "98":
        Champ = 'Shen'
    elif str(id) == "102":
        Champ = 'Shyvana'
    elif str(id) == "27":
        Champ = 'Singed'
    elif str(id) == "14":
        Champ = 'Sion'
    elif str(id) == "15":
        Champ = 'Sivir'
    elif str(id) == "72":
        Champ = 'Skarner'
    elif str(id) == "37":
        Champ = 'Sona'
    elif str(id) == "16":
        Champ = 'Soraka'
    elif str(id) == "50":
        Champ = 'Swain'
    elif str(id) == "517":
        Champ = 'Sylas'
    elif str(id) == "134":
        Champ = 'Syndra'
    elif str(id) == "223":
        Champ = 'Tahm Kench'
    elif str(id) == "163":
        Champ = 'Taliyah'
    elif str(id) == "91":
        Champ = 'Talon'
    elif str(id) == "44":
        Champ = 'Taric'
    elif str(id) == "17":
        Champ = 'Teemo'
    elif str(id) == "412":
        Champ = 'Thresh'
    elif str(id) == "18":
        Champ = 'Tristana'
    elif str(id) == "48":
        Champ = 'Trundle'
    elif str(id) == "23":
        Champ = 'Tryndamere'
    elif str(id) == "4":
        Champ = 'Twisted Fate'
    elif str(id) == "29":
        Champ = 'Twitch'
    elif str(id) == "77":
        Champ = 'Udyr'
    elif str(id) == "6":
        Champ = 'Urgot'
    elif str(id) == "110":
        Champ = 'Varus'
    elif str(id) == "67":
        Champ = 'Vayne'
    elif str(id) == "45":
        Champ = 'Veigar'
    elif str(id) == "161":
        Champ = "Vel'Koz"
    elif str(id) == "254":
        Champ = 'Vi'
    elif str(id) == "234":
        Champ = 'Viego'
    elif str(id) == "112":
        Champ = 'Viktor'
    elif str(id) == "8":
        Champ = 'Vladimir'
    elif str(id) == "106":
        Champ = 'Volibear'
    elif str(id) == "19":
        Champ = 'Warwick'
    elif str(id) == "498":
        Champ = 'Xayah'
    elif str(id) == "101":
        Champ = 'Xerath'
    elif str(id) == "5":
        Champ = 'Xin Zhao'
    elif str(id) == "157":
        Champ = 'Yasuo'
    elif str(id) == "777":
        Champ = 'Yone'
    elif str(id) == "83":
        Champ = 'Yorick'
    elif str(id) == "350":
        Champ = 'Yuumi'
    elif str(id) == "154":
        Champ = 'Zac'
    elif str(id) == "238":
        Champ = 'Zed'
    elif str(id) == "115":
        Champ = 'Ziggs'
    elif str(id) == "26":
        Champ = 'Zilean'
    elif str(id) == "142":
        Champ = 'Zoe'
    elif str(id) == "143":
        Champ = 'Zyra'


def page2():
    global txt1, Champ, btn1, name, NEXTBtn, CHBR, CHBNAME, CHBRNONE, CHBF, CHBFNONE, CHBPLNONE, labelPLNONE, labelNAME, label3, label4, label5, label6, label7, labelF1, labelF2, labelF3, labelF4, labelF5, labelF6, labelF7, labelNONE
    txt1.place_forget()
    btn1.place_forget()
    NEXTBtn.place_forget()
    labelMCM = Label(root, text="모스트 챔피언", **option2, fg="gray")
    labelMCM.place(x=220, y=50)
    if CHBPLNONE == True:
        labelPLNONE.place_forget()
        CHBPLNONE = False
    if CHBNAME == True:
        labelNAME.place_forget()
    if CHBR == True:
        label3.place_forget()
        label4.place_forget()
        label5.place_forget()
        label6.place_forget()
        label7.place_forget()
        CHBR = False
    if CHBRNONE == True:
        label3.place_forget()
        labelF3.place_forget()
        labelF4.place_forget()
        labelF5.place_forget()
        labelF6.place_forget()
        labelF7.place_forget()
        labelNONE.place_forget()
        CHBRNONE = False
    if CHBF == True:
        labelF3.place_forget()
        labelF4.place_forget()
        labelF5.place_forget()
        labelF6.place_forget()
        labelF7.place_forget()
        CHBF = False
    if CHBFNONE == True:
        labelF3.place_forget()
        label3.place_forget()
        label4.place_forget()
        label5.place_forget()
        label6.place_forget()
        label7.place_forget()
        labelNONE.place_forget()
        CHBFNONE = False
    URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name
    res = requests.get(URL, headers={"X-Riot-Token": api_key})
    if res.status_code == 200:
        resobj = json.loads(res.text)
        URL = "https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + \
            resobj["id"]
        res = requests.get(URL, headers={"X-Riot-Token": api_key})
        rankinfo = json.loads(res.text)
        for i in rankinfo[0: 1]:
            # URL2 = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + \
            #     resobj["accountId"] + "?champion=" + str(i['championId'])
            # res = requests.get(URL2, headers={"X-Riot-Token": api_key})
            # rankinfo2 = json.loads(res.text)
            # Kill = 0
            # Death = 0
            # Assist = 0
            # for i in rankinfo2["matches"]:
            #     URL3 = "https://kr.api.riotgames.com/lol/match/v4/matches/" + \
            #         str(i["gameId"])
            #     res = requests.get(URL2, headers={"X-Riot-Token": api_key})
            #     rankinfo3 = json.loads(res.text)
            #     for i in rankinfo3["participantIdentities"]:
            #         if i["player"]["accountId"] in resobj["accountId"]:
            #             print("aa")
            #         else:
            #             print("bb")

            # print(rankinfo2["totalGames"])
            CHID(i['championId'])
            labelMC1 = Label(root, text="챔피언: {0}, 숙련도 레벨{1}".format(
                Champ, i['championLevel']), **option0, fg="gray")
            labelMC1.place(x=40, y=130)
            LTime = int(i['lastPlayTime']) / 1000.0
            date_s = datetime.datetime.fromtimestamp(
                LTime).strftime('%Y-%m-%d %H:%M')
            labelMCD1 = Label(root, text="마지막 플레이시간: {0}분".format(
                date_s), **option4, fg="gray")
            labelMCD1.place(x=40, y=155)
        try:
            for i in rankinfo[1: 2]:
                CHID(i['championId'])
                labelMC1 = Label(root, text="챔피언: {0}, 숙련도 레벨{1}".format(
                    Champ, i['championLevel']), **option0, fg="gray")
                labelMC1.place(x=40, y=180)
                LTime = int(i['lastPlayTime']) / 1000.0
                date_s = datetime.datetime.fromtimestamp(
                    LTime).strftime('%Y-%m-%d %H:%M')
                labelMCD1 = Label(root, text="마지막 플레이시간: {0}분".format(
                    date_s), **option4, fg="gray")
                labelMCD1.place(x=40, y=205)
        except:
            labelMC1 = Label(root, text="검색결과가 없습니다.", **option0, fg="gray")
            labelMC1.place(x=40, y=180)
        try:
            for i in rankinfo[2: 3]:
                CHID(i['championId'])
                labelMC1 = Label(root, text="챔피언: {0}, 숙련도 레벨{1}".format(
                    Champ, i['championLevel']), **option0, fg="gray")
                labelMC1.place(x=40, y=230)
                LTime = int(i['lastPlayTime']) / 1000.0
                date_s = datetime.datetime.fromtimestamp(
                    LTime).strftime('%Y-%m-%d %H:%M')
                labelMCD1 = Label(root, text="마지막 플레이시간: {0}분".format(
                    date_s), **option4, fg="gray")
                labelMCD1.place(x=40, y=255)
        except:
            labelMC1 = Label(root, text="검색결과가 없습니다.", **option0, fg="gray")
            labelMC1.place(x=40, y=230)
        try:
            for i in rankinfo[3: 4]:
                CHID(i['championId'])
                labelMC1 = Label(root, text="챔피언: {0}, 숙련도 레벨{1}".format(
                    Champ, i['championLevel']), **option0, fg="gray")
                labelMC1.place(x=40, y=280)
                LTime = int(i['lastPlayTime']) / 1000.0
                date_s = datetime.datetime.fromtimestamp(
                    LTime).strftime('%Y-%m-%d %H:%M')
                labelMCD1 = Label(root, text="마지막 플레이시간: {0}분".format(
                    date_s), **option4, fg="gray")
                labelMCD1.place(x=40, y=305)
        except:
            labelMC1 = Label(root, text="검색결과가 없습니다.", **option0, fg="gray")
            labelMC1.place(x=40, y=280)
        try:
            for i in rankinfo[4: 5]:
                CHID(i['championId'])
                labelMC1 = Label(root, text="챔피언: {0}, 숙련도 레벨{1}".format(
                    Champ, i['championLevel']), **option0, fg="gray")
                labelMC1.place(x=40, y=330)
                LTime = int(i['lastPlayTime']) / 1000.0
                date_s = datetime.datetime.fromtimestamp(
                    LTime).strftime('%Y-%m-%d %H:%M')
                labelMCD1 = Label(root, text="마지막 플레이시간: {0}분".format(
                    date_s), **option4, fg="gray")
                labelMCD1.place(x=40, y=355)
        except:
            labelMC1 = Label(root, text="검색결과가 없습니다.", **option0, fg="gray")
            labelMC1.place(x=40, y=330)

    else:
        pass


def CH():
    global CHBR, NEXTBtn, CHBNAME, CHBRNONE, CHBF, CHBFNONE, CHBPLNONE, labelPLNONE, labelNAME, label3, label4, label5, label6, label7, labelF1, labelF2, labelF3, labelF4, labelF5, labelF6, labelF7, labelNONE
    if CHBPLNONE == True:
        labelPLNONE.place_forget()
        CHBPLNONE = False
    if CHBNAME == True:
        labelNAME.place_forget()
    if CHBR == True:
        label3.place_forget()
        label4.place_forget()
        label5.place_forget()
        label6.place_forget()
        label7.place_forget()
        NEXTBtn.place_forget()
        CHBR = False
    if CHBRNONE == True:
        label3.place_forget()
        labelF3.place_forget()
        labelF4.place_forget()
        labelF5.place_forget()
        labelF6.place_forget()
        labelF7.place_forget()
        labelNONE.place_forget()
        NEXTBtn.place_forget()
        CHBRNONE = False
    if CHBF == True:
        labelF3.place_forget()
        labelF4.place_forget()
        labelF5.place_forget()
        labelF6.place_forget()
        labelF7.place_forget()
        NEXTBtn.place_forget()
        CHBF = False
    if CHBFNONE == True:
        labelF3.place_forget()
        label3.place_forget()
        label4.place_forget()
        label5.place_forget()
        label6.place_forget()
        label7.place_forget()
        labelNONE.place_forget()
        NEXTBtn.place_forget()
        CHBFNONE = False


root.mainloop()
